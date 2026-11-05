# Hito II – Bitácora de avances y evaluación multidimensional

**Proyecto:** Sistema Predictivo de Abandono de Clientes (Customer Churn)  
**Bootcamp:** Python para Ciencia de Datos – Kodigo  
**Equipo:** Henry Mauricio Cañas Contreras, Dayana Nicolle Guevara Sigüenza, Carlos Luis Monchez Cerna, Christopher Enrique Guerrero Lucero y William Danilo Quijano Roque  
**Fecha de corte:** 4 de noviembre de 2026  
**Metodología:** Agile / Scrum (Opción B)

---

## 1. Objetivo del Hito II

Documentar el avance del proyecto durante los sprints de trabajo, evaluar la solución desde las perspectivas de Design Thinking, tecnológica y financiera, e identificar los pendientes necesarios para completar la integración y entrega del sistema.

El producto busca estimar la probabilidad de abandono de un cliente de telecomunicaciones durante los próximos 30 días y clasificar su riesgo para apoyar acciones de retención.

## 2. Bitácora de avances

| Fecha / periodo | Actividades y avances | Evidencia / estado |
|---|---|---|
| 25 de octubre de 2026 | Definición del problema, objetivo, integrantes, roles, historias de usuario, prioridades y sprints. | Product Backlog documentado en `docs/hito-1-product-backlog.md`. |
| 25–31 de octubre | Preparación de la base de datos, exploración y limpieza inicial. | Dataset original en `data/raw/`; notebooks de exploración y limpieza en `notebooks/`; archivo procesado Parquet en `data/processed/telco_limpio.parquet`. |
| 1–4 de noviembre | Desarrollo de modelos de clasificación y red neuronal, y preparación de artefactos para su reutilización. | Notebooks US-05 y US-06; modelo MLP guardado en `models/modelo_mlp_churn.pkl`. |
| 4 de noviembre | Incorporación de un notebook adicional de red neuronal y continuación del desarrollo de scoring e integración. | `notebooks/US07Modelo_red_neuronal.ipynb` publicado. Su contenido actual entrena y evalúa otra red neuronal; todavía debe verificarse/completarse la función de scoring de riesgo definida para US-07. |
| 4 de noviembre | Desarrollo de API, Docker, pruebas y documentación final en curso. | US-08 a US-11 se encuentran en desarrollo según la coordinación del equipo; al corte de esta revisión sus archivos todavía no estaban visibles en el repositorio. |

### 2.1 Estado de las historias de usuario al corte

Los estados siguientes se basan en los archivos visibles en el repositorio al 4 de noviembre. La publicación de un notebook no implica por sí sola que todos los criterios de aceptación estén cumplidos.

| Historia | Resultado / evidencia | Estado al corte |
|---|---|---|
| US-01 – Exploración de datos | Notebook de análisis exploratorio disponible. | Avance documentado |
| US-02 – Limpieza y transformación | Notebook de limpieza y dataset Parquet procesado disponibles. | Avance documentado |
| US-03 – Almacenamiento en MongoDB | No se encontró evidencia verificable de conexión, inserción y consulta en MongoDB. | Pendiente de validar |
| US-04 – Reportes Parquet en S3/MinIO | Existe un archivo Parquet procesado; no se encontró evidencia de carga y lectura desde S3/MinIO. | Parcial / pendiente de validar |
| US-05 – Modelo clásico | Notebook de entrenamiento disponible. La implementación documentada usa Regresión Logística, mientras que el criterio del backlog solicita XGBoost o Random Forest. | Parcial; requiere resolver la diferencia con el criterio |
| US-06 – Red neuronal MLP | Notebook MLP, comparación de métricas y artefacto `.pkl` disponibles. | Avance documentado |
| US-07 – Scoring de riesgo | El notebook publicado actualmente implementa otra red neuronal y compara accuracy; no se identificó en él una función que asigne niveles Bajo, Medio y Alto con umbrales claros. | Pendiente de completar/verificar |
| US-08 – API FastAPI | En desarrollo por el equipo; no visible en el repositorio al corte. | En progreso |
| US-09 – Docker | En desarrollo por el equipo; no se encontró Dockerfile al corte. | En progreso |
| US-10 – Pruebas pytest | En desarrollo por el equipo; no se encontró carpeta de pruebas al corte. | En progreso |
| US-11 – README e instrucciones | README inicial disponible; todavía debe incluir instrucciones completas de instalación, ejecución, arquitectura y ejemplos de petición/respuesta. | Parcial |
| US-12 – Hito II | Este documento registra la bitácora y evaluación multidimensional. | Documentado en este archivo |

## 3. Evaluación desde Design Thinking

### 3.1 Empatizar

Se identificó como contexto general que las empresas que ofrecen servicios por suscripción o telecomunicaciones pueden perder clientes sin contar con suficiente anticipación para intentar retenerlos. El problema afecta tanto a las organizaciones —por la pérdida de ingresos y el costo de adquirir nuevos clientes— como a los usuarios, que pueden experimentar una atención reactiva en lugar de recibir ofertas o soluciones oportunas.

**Limitación:** en el repositorio no se encontró evidencia de entrevistas, encuestas o sesiones de observación con clientes o personal de retención. Por tanto, esta etapa se basa en la definición inicial del problema y no debe interpretarse como investigación de usuarios ya realizada.

### 3.2 Definir

Se definió el problema como la necesidad de anticipar qué clientes presentan mayor probabilidad de abandonar el servicio. El objetivo del producto es generar una predicción de churn para los próximos 30 días y convertirla en niveles de riesgo comprensibles para facilitar la priorización de acciones de retención.

### 3.3 Idear

Se propuso una solución compuesta por:
- Preparación y análisis de datos históricos de clientes.
- Entrenamiento y comparación de modelos de Machine Learning y Deep Learning.
- Conversión de la probabilidad de churn en categorías de riesgo Bajo, Medio y Alto.
- Exposición de resultados mediante una API REST para facilitar su consumo por otras aplicaciones.

### 3.4 Prototipar

Se construyeron notebooks para explorar y preparar los datos y entrenar modelos. También se guardó un artefacto del modelo MLP para su posible reutilización. La API y la integración del scoring forman parte del trabajo de backend en curso.

### 3.5 Probar

Se realizaron evaluaciones iniciales de modelos con datos de prueba. Para completar esta etapa se requiere ejecutar pruebas de extremo a extremo: enviar datos de un cliente a la API, verificar la probabilidad devuelta, comprobar la categoría de riesgo y validar el manejo de entradas incorrectas o clientes inexistentes.

**Conclusión de Design Thinking:** la solución propuesta responde al problema identificado y cuenta con prototipos analíticos. La validación con usuarios reales y la demostración integral del flujo siguen siendo oportunidades de mejora y no se consideran completadas con la evidencia disponible.

## 4. Evaluación tecnológica

### 4.1 Tecnologías consideradas

| Área | Tecnología | Uso previsto |
|---|---|---|
| Análisis y manipulación | Python, Pandas y NumPy | Carga, exploración y preparación de datos |
| Procesamiento de datos | PySpark / Dask | Procesamiento escalable contemplado en el backlog |
| Formatos de datos | CSV y Parquet | Datos originales y datos procesados |
| Machine Learning | Scikit-learn | Preparación, entrenamiento y evaluación de modelos |
| Deep Learning | TensorFlow / Keras | Desarrollo de redes neuronales |
| API | FastAPI y Pydantic | Exposición de predicciones mediante endpoints REST |
| Contenedores | Docker | Empaquetado y despliegue reproducible |
| Pruebas | Pytest | Validación automatizada de módulos |

### 4.2 Avances y fortalezas

- El repositorio mantiene una separación inicial entre datos, notebooks, código fuente, modelos y documentación.
- Se conservan los archivos originales y un dataset procesado en Parquet.
- Se desarrollaron modelos iniciales y se guardó el pipeline MLP en un archivo reutilizable.
- La comparación de modelos permite discutir el desempeño y justificar la selección del modelo.

### 4.3 Riesgos y aspectos por completar

1. **Alineación de US-05:** el backlog solicita XGBoost o Random Forest, pero el notebook actual documenta Regresión Logística. Se debe entrenar uno de los modelos solicitados o dejar documentada y aprobada cualquier modificación del criterio.
2. **US-07:** se debe implementar y probar explícitamente la función que recibe una probabilidad y devuelve Bajo, Medio o Alto, definiendo umbrales. El notebook publicado actualmente corresponde a entrenamiento de otra red neuronal, no demuestra por sí mismo el scoring solicitado.
3. **Consistencia de preprocesamiento:** la API debe aplicar las mismas transformaciones, orden de variables y escalado usados durante el entrenamiento.
4. **Integración:** la API debe cargar el modelo correcto y devolver una respuesta JSON consistente.
5. **Reproducibilidad:** deben documentarse dependencias, versiones e instrucciones de ejecución.
6. **Calidad:** deben agregarse pruebas automatizadas y comprobar que los archivos necesarios estén en GitHub.

### 4.4 Evaluación tecnológica general

La selección de tecnologías es adecuada para construir un prototipo de predicción y exponerlo mediante una API. Sin embargo, al corte de este documento la solución todavía no puede considerarse completamente integrada ni lista para producción: faltan evidencias de ejecución conjunta de API, modelo, scoring, contenedor y pruebas.

## 5. Evaluación financiera

### 5.1 Recursos utilizados

El proyecto se desarrolla principalmente con herramientas de software de código abierto y entornos de desarrollo/notebooks. Entre los recursos considerados se encuentran Python, bibliotecas de análisis y modelado, TensorFlow/Keras, FastAPI, pytest, GitHub y Google Colab.

### 5.2 Costos y viabilidad

No se dispone de comprobantes ni de un registro de gastos reales del equipo en el repositorio. Por ello, no se afirma que el costo total haya sido cero. El desarrollo puede mantenerse con un costo monetario directo bajo mientras se utilicen versiones gratuitas o locales de las herramientas y no se contraten servicios de infraestructura.

Los posibles costos futuros corresponden a:
- Hospedaje de la API y capacidad de cómputo.
- Almacenamiento y servicios administrados de bases de datos.
- Servicios cloud o límites de uso superiores.
- Mantenimiento, monitoreo y soporte.

### 5.3 Evaluación financiera

Para un prototipo académico, la solución es financieramente viable si se priorizan herramientas gratuitas y recursos locales. Para una implementación productiva se necesitaría estimar el costo de infraestructura, almacenamiento, tráfico, seguridad y mantenimiento según la cantidad de clientes y solicitudes.

**Limitación:** no se cuenta con cotizaciones, presupuesto aprobado ni medición del costo de operación. La evaluación es cualitativa y deberá actualizarse si se decide desplegar el sistema en la nube.

## 6. Conclusiones generales del Hito II

Durante el proyecto se estableció una base de trabajo colaborativa, se organizó el Product Backlog y se avanzó en la exploración y preparación de datos y en el entrenamiento inicial de modelos. El repositorio contiene evidencia de notebooks, datos procesados y un artefacto MLP.

La evaluación multidimensional muestra que la propuesta es técnicamente viable para un prototipo académico y aborda un problema relevante para empresas con clientes por suscripción. No obstante, todavía hay diferencias entre algunos criterios originales y las implementaciones publicadas, especialmente US-05 y US-07. También se requiere completar la integración y validar el sistema completo.

El siguiente paso es finalizar y publicar US-08 a US-11, completar el scoring de US-07, resolver la alineación de US-05 y ejecutar una prueba integral antes de presentar el proyecto como un sistema funcional.

## 7. Acciones prioritarias antes de la entrega

- [ ] Confirmar que US-08, US-09, US-10 y US-11 estén publicados en GitHub.
- [ ] Verificar que US-07 incluya la función de scoring Bajo/Medio/Alto y umbrales explícitos.
- [ ] Resolver/documentar la diferencia entre el criterio de US-05 y la Regresión Logística implementada.
- [ ] Confirmar que el modelo y el preprocesamiento usados por la API sean compatibles.
- [ ] Ejecutar al menos una prueba de predicción de extremo a extremo y guardar el ejemplo de entrada y salida.
- [ ] Actualizar el README con instalación, ejecución, endpoint y ejemplo JSON.
- [ ] Revisar que no se hayan subido credenciales, claves o archivos sensibles.

---

**Nota de transparencia:** este documento refleja el estado y la evidencia disponible en el repositorio al 4 de noviembre de 2026. Los puntos marcados como pendientes o en progreso deben actualizarse cuando el equipo publique y verifique sus entregables.
