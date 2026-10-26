# sistema-predictivo-churn
Sistema Predictivo de Abandono de Clientes (Customer Churn) - Proyecto Final Bootcamp Python para Ciencia de Datos - Kodigo
## Problema a resolver
Las empresas de telecomunicaciones, plataformas SaaS y bancos pierden clientes sin anticiparse. El costo de adquirir un nuevo cliente es entre 5 y 25 veces mayor que retener uno existente. Actualmente, la mayoría de las organizaciones se enteran del abandono cuando el cliente ya canceló el servicio.

La solución propuesta es desarrollar un sistema end-to-end capaz de predecir la probabilidad de abandono (churn) de un cliente en los próximos 30 días, utilizando procesamiento de datos a gran escala, modelos de Machine Learning y Deep Learning, y exponiendo los resultados a través de una API REST lista para producción.

---

## Integrantes del equipo
| Integrante | Rol principal | User Stories asignadas (sugeridas) |
|------------|---------------|------------------------------------|
| Christopher Enrique Guerrero Lucero | Product Owner + Coordinador | US-01, US-12, priorización general |
| Dayana Nicolle Guevara Sigüenza | Ingeniera de Datos | US-02, US-03, US-04 |
| Carlos Luis Monchez Cerna | Científico de Datos (ML) | US-05, US-07 |
| Henry Mauricio Canas Contreras | Científico de Datos (DL) | US-06 |
| William Danilo Quijano Roque | Backend + DevOps | US-08, US-09, US-10, US-11 |

---

## Consultar Backlog
Para consultar el Product Backlog completo y las User Stories del Hito I, ver docs/hito-1-product-backlog.md

---

## Estructura del repositorio
La organización del código sigue el estándar internacional *Cookiecutter Data Science*:
sistema-predictivo-churn/
│
├── README.md               # Portada del proyecto e instrucciones principales
├── LICENSE                 # Licencia de código abierto (MIT)
├── .gitignore              # Archivos y carpetas excluidos del control de versiones
├── .dockerignore           # Exclusiones para la construcción de la imagen Docker
├── requirements.txt        # Dependencias del proyecto con versiones fijadas
├── Dockerfile              # Script para la contenedorización de la API
│
├── data/                   # Gestión de datos (no versionados en Git)
│   ├── raw/                # Datos crudos originales
│   ├── processed/          # Datos limpios y transformados
│   └── muestra/            # Muestra reducida para pruebas rápidas
│
├── notebooks/              # Cuadernos Jupyter de exploración (EDA) y experimentos
│
├── src/                    # Código fuente modular en Python
│   ├── ingesta/            # Scripts de ingesta y procesamiento con PySpark y Dask
│   ├── almacenamiento/     # Conectores para MongoDB y S3 simulado (boto3)
│   ├── modelos/            # Clases POO para entrenamiento y evaluación ML/DL
│   └── api/                # Definición de la API REST con FastAPI y esquemas Pydantic
│
├── tests/                  # Pruebas unitarias automatizadas con pytest y mocks
│
└── docs/                   # Registro de decisiones técnicas (decisiones.md) y Hitos
    └── hito-1-product-acklog.md    # Product Backlog y Historias de Usuario (Hito I)

---

## Stack Tecnológico
- Procesamiento de Datos Masivos: PySpark / Dask
- Bases de Datos & Almacenamiento: MongoDB (NoSQL) / AWS S3 Simulado (boto3 / moto)
- Machine Learning & Deep Learning: Scikit-Learn / XGBoost / TensorFlow / PyTorch
- Servicio Web & MLOps: FastAPI / Pydantic / Docker
- Pruebas y Calidad: Pytest / Flake8

(actualización 25 de octubre del 2026). 
