# Este codigo es parte parte de la US-10

from datetime import datetime, timezone
import os
import sys
from pathlib import Path
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Configurar raíz del proyecto
RAIZ = Path(__file__).resolve().parent.parent.parent
if str(RAIZ) not in sys.path:
    sys.path.append(str(RAIZ))


class ConectorMongo:
    """Clase para manejar la persistencia de predicciones en MongoDB (US-10)."""

    def __init__(self, uri: str | None = None, db_name: str = "telco_churn_db"):
        # Usa URI local por defecto o variable de entorno para entornos Docker/Cloud
        self.uri = uri or os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.db_name = db_name
        self.client = None
        self.db = None

    def conectar(self):
        """Establece conexión con el cluster/instancia de MongoDB."""
        try:
            self.client = MongoClient(self.uri, serverSelectionTimeoutMS=3000)
            # Test rápido de conexión
            self.client.admin.command("ping")
            self.db = self.client[self.db_name]
            print(f"✅ Conexión exitosa a MongoDB: {self.db_name}")
        except ConnectionFailure:
            print(
                "⚠️ Advertencia: No se pudo conectar a MongoDB. La API funcionará sin guardar historial."
            )
            self.db = None

    def guardar_prediccion(
        self, datos_cliente: dict, resultado_prediccion: dict
    ) -> str | None:
        """Guarda un registro de predicción en la colección 'predicciones' (US-10)."""
        if self.db is None:
            self.conectar()

        if self.db is not None:
            documento = {
                "fecha_consulta": datetime.now(timezone.utc),
                "cliente_entrada": datos_cliente,
                "resultado": resultado_prediccion,
            }
            resultado = self.db["predicciones"].insert_one(documento)
            return str(resultado.inserted_id)

        return None
