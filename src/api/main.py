
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.modelos.predictor import PredictorRiesgo
from src.alertas.notificador import ServicioAlertas
from src.almacenamiento.mongo_db import ConectorMongo


app = FastAPI(
    title="API de Predicción de Churn - Telco",
    description="Servicio para evaluar el riesgo de abandono de clientes.",
    version="1.2.0",
)

# Localizar la carpeta principal del proyecto
RAIZ_PROYECTO = Path(__file__).resolve().parents[2]

# Cargar el modelo MLP entrenado en US-06
RUTA_MODELO = RAIZ_PROYECTO / "models" / "modelo_mlp_churn.pkl"

modelo = None

if RUTA_MODELO.exists():
    modelo = joblib.load(RUTA_MODELO)
    print("Modelo MLP cargado correctamente.")
else:
    print(f"No se encontró el modelo en: {RUTA_MODELO}")


# Conectar con MongoDB
mongo_db = ConectorMongo()
mongo_db.conectar()


class ClienteEntrada(BaseModel):
    """Datos necesarios para realizar una predicción."""

    Tenure_Months: int = Field(
        ..., example=2, description="Meses de permanencia"
    )
    Monthly_Charges: float = Field(
        ..., example=53.85, description="Cargo mensual"
    )
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
    """Predice el riesgo de abandono y guarda el resultado."""

    # No generar predicciones si el modelo no está disponible
    if modelo is None:
        raise HTTPException(
            status_code=503,
            detail="El modelo de predicción no está disponible.",
        )

    try:
        # Preparar los datos para el modelo
        df_input = pd.DataFrame(
            [
                [
                    cliente.Tenure_Months,
                    cliente.Monthly_Charges,
                    cliente.Total_Charges,
                ]
            ],
            columns=[
                "Tenure Months",
                "Monthly Charges",
                "Total Charges",
            ],
        )

        # Calcular la probabilidad de abandono
        probabilidad = float(modelo.predict_proba(df_input)[0][1])

        # Clasificar el riesgo
        resultado_riesgo = PredictorRiesgo.clasificar_riesgo(
            probabilidad
        )

        datos_cliente_dict = cliente.model_dump()

        # Procesar alerta automática
        alerta_emitida = ServicioAlertas.procesar_alerta(
            datos_cliente_dict,
            resultado_riesgo,
        )

        # Guardar predicción en MongoDB
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

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar la predicción: {str(e)}",
        )
