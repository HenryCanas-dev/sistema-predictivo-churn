# Product Backlog
## Sistema Predictivo de Abandono de Clientes (Customer Churn)

**Proyecto Final** – Bootcamp Python para Ciencia de Datos  
**Kodigo – Academia de Tecnología Creativa**  

**Equipo:**
- Henry Mauricio Cañas Contreras
- Dayana Nicolle Guevara Sigüenza
- Carlos Luis Monchez Cerna
- Christopher Enrique Guerrero Lucero
- William Danilo Quijano Roque

**Fecha:** 25 de octubre de 2026  
**Metodología:** Agile / Scrum (Opción B)

---

### Problema a Resolver
Las empresas de telecomunicaciones, plataformas SaaS y bancos pierden clientes sin anticiparse. El costo de adquirir un nuevo cliente es entre 5 y 25 veces mayor que retener uno existente. Actualmente, la mayoría de las organizaciones se enteran del abandono cuando el cliente ya canceló el servicio.

### Objetivo General
Desarrollar un sistema end-to-end capaz de predecir la probabilidad de abandono (churn) de un cliente en los próximos 30 días, utilizando procesamiento de datos a gran escala, modelos de Machine Learning y Deep Learning, y exponiendo los resultados a través de una API REST lista para producción.

---

## 1. Visión del Producto

Desarrollar un sistema predictivo que identifique con anticipación a los clientes con alto riesgo de abandono (churn) en los próximos 30 días, permitiendo a las empresas ejecutar acciones de retención de forma proactiva. El sistema combinará procesamiento de datos a gran escala, modelos de Machine Learning y Deep Learning, y una API lista para producción.

---

## 2. Definition of Done (DoD)

Una User Story se considera **terminada** cuando cumple todos estos criterios:

- [ ] Código escrito siguiendo buenas prácticas (PEP8)
- [ ] Código revisado por al menos 1 compañero del equipo (Code Review)
- [ ] Pruebas unitarias con `pytest` implementadas y pasando
- [ ] Documentación básica incluida (docstrings + README actualizado si aplica)
- [ ] Subido a la rama correspondiente en GitHub mediante Pull Request
- [ ] Cumple todos los Criterios de Aceptación de la historia
- [ ] No introduce errores en el pipeline existente

---

## 3. Product Backlog (Priorizado)

| ID | User Story | Prioridad | Story Points | Sprint | Criterios de Aceptación |
|----|------------|-----------|--------------|--------|-------------------------|
| **US-01** | Como analista de datos, quiero cargar y explorar el dataset de clientes para entender las variables relacionadas con el churn. | Alta | 5 | 1 | - Dataset cargado correctamente<br>- Análisis exploratorio (EDA) documentado en notebook<br>- Identificación de variables relevantes y nulos |
| **US-02** | Como ingeniero de datos, quiero construir un pipeline de limpieza y transformación de datos usando PySpark o Dask. | Alta | 8 | 1 | - Pipeline reproducible<br>- Manejo de valores nulos y outliers<br>- Datos transformados listos para modelado |
| **US-03** | Como ingeniero de datos, quiero almacenar los perfiles de usuarios y el historial de interacciones en MongoDB. | Alta | 5 | 1 | - Conexión a MongoDB funcionando<br>- Datos insertados y consultables<br>- Esquema documentado |
| **US-04** | Como ingeniero de datos, quiero guardar reportes analíticos periódicos en formato Parquet en S3 (MinIO). | Media | 5 | 2 | - Archivos Parquet generados correctamente<br>- Subida a bucket S3/MinIO exitosa<br>- Lectura de los archivos verificada |
| **US-05** | Como científico de datos, quiero entrenar un modelo de clasificación (XGBoost o Random Forest) para predecir churn. | Alta | 8 | 2 | - Modelo entrenado<br>- Métricas de evaluación (Precision, Recall, F1, AUC) documentadas<br>- Modelo guardado |
| **US-06** | Como científico de datos, quiero entrenar una Red Neuronal (MLP) y compararla con el modelo clásico. | Alta | 8 | 2 | - MLP entrenada<br>- Comparación de métricas entre ambos modelos<br>- Selección del mejor modelo justificada |
| **US-07** | Como científico de datos, quiero crear un sistema de scoring que asigne un nivel de riesgo de churn (Bajo, Medio, Alto). | Alta | 5 | 2 | - Función de scoring implementada<br>- Niveles de riesgo definidos con umbrales claros |
| **US-08** | Como desarrollador backend, quiero crear una API REST con FastAPI que reciba el ID de un cliente y devuelva la probabilidad de churn y la acción recomendada. | Alta | 8 | 3 | - Endpoint `/v1/predict-churn` funcional<br>- Respuesta en formato JSON<br>- Manejo de errores (cliente no encontrado, etc.) |
| **US-09** | Como DevOps, quiero empaquetar la aplicación en un contenedor Docker. | Alta | 5 | 3 | - Dockerfile funcional<br>- Imagen se construye sin errores<br>- Contenedor corre la API correctamente |
| **US-10** | Como desarrollador, quiero escribir pruebas unitarias con pytest para los módulos principales. | Media | 5 | 3 | - Cobertura mínima del 70% en módulos críticos<br>- Tests pasando en CI local |
| **US-11** | Como equipo, quiero tener un README.md completo con instrucciones de instalación, arquitectura y ejemplos de uso. | Alta | 3 | 3 | - README claro y profesional<br>- Incluye arquitectura, cómo levantar el proyecto y ejemplos de peticiones JSON |
| **US-12** | Como Product Owner, quiero documentar el Hito II (Bitácora + Evaluación 
