# Sistema Inteligente de Evaluación de Riesgo Crediticio

Proyecto académico desplegable que operacionaliza un modelo previo de clasificación para estimar el **incumplimiento crediticio a 90 días**.

## Objetivo

Integrar un modelo `RandomForestClassifier` en una solución completa con:

- frontend web;
- backend FastAPI;
- API REST;
- validación de entradas;
- contenedor Docker;
- pruebas automatizadas;
- documentación técnica;
- estrategia de despliegue en Google Cloud Run.

## Continuidad con la fase previa

La fase anterior evaluó baseline, Regresión Logística y Random Forest. El modelo seleccionado fue Random Forest y se utilizó un **umbral de decisión 0.62**. Las métricas académicas de referencia fueron:

| Métrica | Valor |
|---|---:|
| Accuracy | 0.9168 |
| Precision | 0.8589 |
| Recall | 0.8284 |
| F1-score | 0.8434 |
| AUC | 0.9593 |

> Nota: `model/metadata.json` distingue entre las métricas académicas de referencia y las métricas del artefacto empaquetado generado por `training/train_model.py`.

## Arquitectura

```text
Navegador
   │
   │ HTTP / JSON
   ▼
FastAPI ───────────────► /health
   │                    /model-info
   │                    /predict
   ▼
Random Forest (.joblib)
   │
   ▼
Probabilidad de incumplimiento
   │
   ▼
Regla: probabilidad >= 0.62
```

## Estructura

```text
.
├── app/
├── frontend/
├── model/
├── training/
├── tests/
├── docs/
├── evidence/
├── .github/workflows/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Ejecución local sin Docker

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Instalación:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

Abrir:

- Aplicación: `http://localhost:8080`
- Swagger/OpenAPI: `http://localhost:8080/docs`
- Health check: `http://localhost:8080/health`

## Docker

Construcción:

```bash
docker build -t riesgo-crediticio-api:1.0.0 .
```

Ejecución:

```bash
docker run --rm -p 8080:8080 riesgo-crediticio-api:1.0.0
```

Alternativa:

```bash
docker compose up --build
```

## Pruebas

```bash
pytest -v
```

## Ejemplo API

```bash
curl -X POST "http://localhost:8080/predict"   -H "Content-Type: application/json"   -d '{
    "ingreso_mensual": 32000,
    "antiguedad_laboral": 5.5,
    "saldo_promedio": 18000,
    "utilizacion_credito": 0.65,
    "historial_moras": 2,
    "relacion_deuda_ingreso": 0.42,
    "edad_cuenta": 6.0,
    "consultas_buro": 3,
    "variabilidad_ingreso": 0.20,
    "monto_solicitado": 85000
  }'
```

## Documentación de entrega

- `docs/ARQUITECTURA.md`
- `docs/MANUAL_DESPLIEGUE.md`
- `docs/VALIDACION_PRUEBAS.md`
- `docs/USO_IA_DOCUMENTACION.md`
- `docs/GUIA_EVIDENCIAS.md`

## Limitaciones

El conjunto de datos es sintético y la solución es académica. No debe utilizarse para aprobar o rechazar créditos reales sin validación externa, análisis de sesgo, explicabilidad, seguridad, monitoreo de drift, gobierno del modelo y supervisión humana.

## Autor

Jorge Arturo Vázquez Meza  
Proyecto académico de Maestría en Inteligencia Artificial
