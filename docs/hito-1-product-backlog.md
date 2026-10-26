# Product Backlog  
## Sistema Predictivo de Abandono de Clientes (Customer Churn)

**Proyecto Final** – Bootcamp Python para Ciencia de Datos  
**Kodigo – Academia de Tecnología Creativa**  
**Equipo:**
-Henry Mauricio Cañas Contreras, 
-Dayana Nicolle Guevara Sigüenza, 
-Carlos Luis Monchez Cerna,
-Christopher Enrique Guerrero Lucero,
-William Danilo Quijano Roque.

**Fecha:** 25 de octubre de 2026  
**Metodología:** Agile / Scrum

---

## 1. Visión del Producto

Desarrollar un sistema predictivo que identifique con anticipación a los clientes con alto riesgo de abandono (churn) en los próximos 30 días, permitiendo a las empresas de telecomunicaciones, SaaS o banca ejecutar acciones de retención de forma proactiva. El sistema combinará procesamiento de datos a gran escala, modelos de Machine Learning y Deep Learning, y una API lista para producción.

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

| ID     | User Story                                                                 | Prioridad | Story Points | Sprint | Criterios de Aceptación |
|--------|-----------------------------------------------------------------------------|-----------|--------------|--------|-------------------------|
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
| **US-12** | Como Product Owner, quiero documentar el Hito II (Bitácora + Evaluación Multidimensional). | Media | 5 | 2 | - Bitácora de avances actualizada<br>- Evaluación de Design Thinking, Tecnológica y Financiera incluida |

---

## 4. Mapa de Sprints

### Sprint 1 (25 – 31 de octubre) – Fundación de Datos
**Objetivo:** Tener los datos limpios, explorados y almacenados.

- US-01: Exploración del dataset
- US-02: Pipeline de limpieza (PySpark/Dask)
- US-03: Almacenamiento en MongoDB

**Total Story Points:** 18

---

### Sprint 2 (1 – 5 de noviembre) – Modelado y Persistencia
**Objetivo:** Modelos entrenados, comparados y reportes guardados.

- US-04: Guardado de reportes en S3/MinIO
- US-05: Modelo clásico (XGBoost/Random Forest)
- US-06: Red Neuronal (MLP) + comparación
- US-07: Sistema de scoring de riesgo
- US-12: Documentación Hito II

**Total Story Points:** 31

---

### Sprint 3 (5 – 6 de noviembre) – API, Docker y Entrega Final
**Objetivo:** Sistema funcional, contenedorizado y documentado.

- US-08: API FastAPI
- US-09: Docker
- US-10: Pruebas unitarias
- US-11: README profesional

**Total Story Points:** 21

---

## 5. Roles del Equipo (sugeridos)

| Integrante | Rol principal              | User Stories asignadas (sugeridas) |
|------------|----------------------------|------------------------------------|
| Persona 1  | Product Owner + Coordinador| US-01, US-12, priorización general |
| Persona 2  | Ingeniero de Datos         | US-02, US-03, US-04                |
| Persona 3  | Científico de Datos (ML)   | US-05, US-07                       |
| Persona 4  | Científico de Datos (DL)   | US-06                              |
| Persona 5  | Backend + DevOps           | US-08, US-09, US-10, US-11         |

---

## 6. Notas

- Las estimaciones (Story Points) son iniciales y se pueden ajustar en la planificación de cada Sprint.
- El equipo realizará Daily Syncs cortos (15 min) para sincronizar avances.
- Todas las User Stories deben pasar por Pull Request + Code Review antes de considerarse Done.
