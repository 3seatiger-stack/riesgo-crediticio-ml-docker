# Resumen Ejecutivo de Cierre

## Proyecto

**Sistema Inteligente de Evaluación de Riesgo Crediticio**

Autor: **Jorge Arturo Vázquez Meza**

## 1. Objetivo

El proyecto tuvo como propósito transformar un modelo de clasificación previamente construido en una solución técnica completa, portable y desplegable.

El modelo estima la probabilidad de incumplimiento crediticio a 90 días y fue integrado en una arquitectura con frontend web, backend FastAPI, API REST, validación de datos, contenedor Docker, pruebas automatizadas y despliegue en Google Cloud Run.

## 2. Continuidad con la fase previa

La solución conserva la lógica principal del proyecto académico anterior:

- problema: predicción de incumplimiento crediticio a 90 días;
- modelo seleccionado: Random Forest;
- umbral de decisión: 0.62;
- diez variables financieras de entrada;
- salida basada en probabilidad de incumplimiento.

Las métricas académicas históricas de referencia fueron:

| Métrica | Valor |
|---|---:|
| Accuracy | 0.9168 |
| Precision | 0.8589 |
| Recall | 0.8284 |
| F1-score | 0.8434 |
| AUC | 0.9593 |

El artefacto empaquetado se validó por separado, evitando presentar como idénticos resultados obtenidos en entornos o ejecuciones distintas.

## 3. Solución implementada

La solución final integra:

- frontend en HTML, CSS y JavaScript;
- backend con FastAPI;
- API REST;
- validación de entradas con Pydantic;
- modelo Random Forest serializado con Joblib;
- Dockerfile;
- Docker Compose;
- pruebas automatizadas con Pytest;
- workflow de GitHub Actions;
- despliegue en Google Cloud Run;
- documentación técnica.

## 4. Arquitectura

```text
Usuario
  ↓
Frontend web
  ↓ HTTP/JSON
FastAPI
  ↓
Validación Pydantic
  ↓
Random Forest
  ↓
Probabilidad de incumplimiento
  ↓
Umbral 0.62
  ↓
Respuesta JSON
  ↓
Contenedor Docker
  ↓
Google Cloud Run
```

## 5. Evidencia técnica validada

Durante la ejecución se comprobó:

- construcción correcta de la imagen Docker;
- existencia de la imagen `riesgo-crediticio-api:1.0.0`;
- ejecución local del contenedor;
- frontend accesible en `localhost:8080`;
- predicción funcional;
- documentación Swagger/OpenAPI;
- endpoint `POST /predict` con respuesta HTTP 200;
- health check funcional;
- 9 pruebas automatizadas aprobadas;
- GitHub Actions aprobado en la nube;
- despliegue público en Cloud Run.

## 6. URLs del proyecto

Aplicación pública:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app

Documentación de API:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app/docs

Health check:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app/health

Información del modelo:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app/model-info

Repositorio GitHub:

https://github.com/3seatiger-stack/riesgo-crediticio-ml-docker

## 7. Resultado global

El proyecto pasó de un modelo experimental a una solución técnica desplegable y portable. La contenerización permitió asegurar consistencia entre entornos, mientras que GitHub Actions agregó validación automática del código y Cloud Run permitió publicar la aplicación como servicio accesible por Internet.

## 8. Conclusión ejecutiva

La solución cumple el objetivo de integrar Machine Learning con prácticas de ingeniería de software, APIs, contenedores, validación automatizada y despliegue en nube.

El principal valor del proyecto no reside únicamente en la capacidad predictiva del modelo, sino en demostrar el proceso de operacionalización necesario para convertir un experimento de Machine Learning en un sistema utilizable, verificable y desplegable.
