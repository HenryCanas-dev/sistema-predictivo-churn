from pathlib import Path
from typing import ClassVar

import pandas as pd


class CargadorDatos:
    """Clase encargada de la ingesta y validación de calidad de datos de Telco Churn."""

    COLUMNAS_REQUERIDAS: ClassVar[tuple[str, ...]] = [
        "CustomerID",
        "Tenure Months",
        "Monthly Charges",
        "Total Charges",
        "Contract",
        "Churn Value",
    ]

    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = Path(ruta_archivo)
        self.df = None

    def cargar_datos(self) -> pd.DataFrame:
        """Carga el archivo Excel/CSV y valida las columnas requeridas (US-01)."""
        if not self.ruta_archivo.exists():
            raise FileNotFoundError(f"El archivo {self.ruta_archivo} no existe.")

        if self.ruta_archivo.suffix in [".xlsx", ".xls"]:
            self.df = pd.read_excel(self.ruta_archivo)
        elif self.ruta_archivo.suffix == ".csv":
            self.df = pd.read_csv(self.ruta_archivo)
        else:
            raise ValueError("Formato de archivo no soportado.")

        # Validar columnas (US-01)
        columnas_faltantes = [
            col for col in self.COLUMNAS_REQUERIDAS if col not in self.df.columns
        ]
        if columnas_faltantes:
            raise ValueError(f"Faltan columnas requeridas: {columnas_faltantes}")

        print(f"Ingesta exitosa: {len(self.df)} registros cargados.")
        return self.df

    def limpiar_datos(self) -> pd.DataFrame:
        """Limpia nulos e inconsistencias y genera reporte de calidad (US-02)."""
        if self.df is None:
            raise ValueError("Debe cargar los datos antes de limpiarlos.")

        # Convertir Total Charges a numérico (trata espacios vacíos como NaN)
        self.df["Total Charges"] = pd.to_numeric(
            self.df["Total Charges"], errors="coerce"
        )

        nulos_iniciales = self.df.isnull().sum().to_dict()

        # Imputar valores nulos en Total Charges
        self.df["Total Charges"] = self.df["Total Charges"].fillna(
            self.df["Monthly Charges"] * self.df["Tenure Months"]
        )

        print("Reporte de Calidad de Datos:")
        print(
            f"- Nulos corregidos en Total Charges: {nulos_iniciales.get('Total Charges', 0)}"
        )
        print(f"- Total de registros limpios: {len(self.df)}")

        return self.df
