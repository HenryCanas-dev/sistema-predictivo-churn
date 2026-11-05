import logging

# Configurar logging para registrar alertas de retención comercial
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("AlertasChurn")


class ServicioAlertas:
    """Módulo encargado de notificar a los gestores comerciales ante alto riesgo (US-11)."""

    @staticmethod
    def procesar_alerta(cliente_datos: dict, resultado_riesgo: dict):
        """Verifica si se debe emitir una alerta comercial inmediata."""
        if resultado_riesgo.get("alerta_retencion"):
            mensaje_alerta = (
                f"🚨 ALERTA DE CHURN HIGH-RISK (>80%) DETECTADA! "
                f"Cliente (Tenure: {cliente_datos.get('Tenure_Months')} meses, "
                f"Cargo Mensual: ${cliente_datos.get('Monthly_Charges')}) "
                f"con riesgo del {resultado_riesgo.get('porcentaje_riesgo')}. "
                f"Acción requerida: {resultado_riesgo.get('accion_sugerida')}"
            )
            # Imprimir en consola de servidor con nivel de advertencia
            logger.warning(mensaje_alerta)
            return True
        return False
