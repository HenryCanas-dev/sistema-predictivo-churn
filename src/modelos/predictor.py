class PredictorRiesgo:
    """Clase para clasificar el riesgo de abandono y sugerir acciones de negocio (US-08)."""

    @staticmethod
    def clasificar_riesgo(probabilidad_churn: float) -> dict:
        """Clasifica la probabilidad en Alto, Medio o Bajo y determina si activa alerta (US-08 / US-11)."""
        porcentaje = round(probabilidad_churn * 100, 2)

        # Criterio de la US-11: Probabilidad >= 80% activa Alerta Automática
        alerta_urgente = probabilidad_churn >= 0.80

        if probabilidad_churn >= 0.80:
            categoria = "Alto"
            accion = "Ofrecer descuento inmediato y llamada urgente de retención."
        elif probabilidad_churn >= 0.40:
            categoria = "Medio"
            accion = "Enviar encuesta de satisfacción y promoción ligera."
        else:
            categoria = "Bajo"
            accion = "Sin acción requerida. Cliente fidelizado."

        return {
            "porcentaje_riesgo": f"{porcentaje}%",
            "probabilidad_raw": probabilidad_churn,
            "categoria_riesgo": categoria,
            "alerta_retencion": alerta_urgente,
            "prioridad": "URGENTE" if alerta_urgente else "NORMAL",
            "accion_sugerida": accion,
        }
