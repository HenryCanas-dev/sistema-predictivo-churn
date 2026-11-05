# ESte codigo es parte de US-09 y US-10
from pathlib import Path
from typing import ClassVar

from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel, Field

from src.modelos.predictor import PredictorRiesgo

from src.alertas.notificador import ServicioAlertas
from src.almacenamiento.mongo_db import ConectorMongo
from src.modelos.predictor import PredictorRiesgo

app = FastAPI(
    title="API de Predicción de Churn - Telco",
    description="Servicio para evaluar el riesgo de abandono de clientes, Alertas Automatizadas "
    "e historial (US-09, US-10, US-11)",
    version="1.2.0",
)

# Intentar cargar el modelo guardado en models/ (US-05 / US-07)
RUTA_MODELO = Path("models/modelo_logistico_churn.pkl")
modelo = None

if RUTA_MODELO.exists():
    modelo = joblib.load(RUTA_MODELO)

# Instanciar conector a MongoDB (US-10)
mongo_db = ConectorMongo()
mongo_db.conectar()


class ClienteEntrada(BaseModel):
    """Esquema para validar los datos de entrada en formato JSON (US-09)."""

    Tenure_Months: int = Field(..., example=2, description="Meses de permanencia")
    Monthly_Charges: float = Field(..., example=53.85, description="Cargo mensual")
    Total_Charges: float = Field(
        ..., example=108.15, description="Cargo total histórico"
    )


@app.get("/")
def inicio():
    return {
        "mensaje": "API de Predicción de Churn activa y lista para recibir peticiones."
    }


@app.post("/predict")
def predecir_churn(cliente: ClienteEntrada):
    """Endpoint POST para predecir el riesgo y persistir en MongoDB (US-09 / US-10)."""
    try:
        # 1. Inferencia del modelo
        if modelo is not None:
            df_input = pd.DataFrame(
                [
                    [
                        cliente.Tenure_Months,
                        cliente.Monthly_Charges,
                        cliente.Total_Charges,
                    ]
                ],
                columns=["Tenure Months", "Monthly Charges", "Total Charges"],
            )
            probabilidad = float(modelo.predict_proba(df_input)[0][1])
        else:
            probabilidad = 0.85

        # 2. Regla de negocio y alerta (US-08, US-11)
        resultado_riesgo = PredictorRiesgo.clasificar_riesgo(probabilidad)
        datos_cliente_dict = cliente.model_dump()

        # 3. Procesar Alerta Automática si riesgo > 80% (US-11)
        alerta_emitida = ServicioAlertas.procesar_alerta(
            datos_cliente_dict, resultado_riesgo
        )

        # 4. Guardar en MongoDB (US-10)
        registro_id = mongo_db.guardar_prediccion(
            datos_cliente=datos_cliente_dict,
            resultado_prediccion=resultado_riesgo,
        )

        return {
            "cliente_evaluado": datos_cliente_dict,
            "resultado_prediccion": resultado_riesgo,
            "alerta_notificada": alerta_emitida,
            "registro_mongo_id": registro_id,
        }

    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(e))
