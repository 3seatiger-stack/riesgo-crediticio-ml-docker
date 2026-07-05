# Matriz de Cumplimiento de la Rúbrica

## Proyecto

**Sistema Inteligente de Evaluación de Riesgo Crediticio**

## 1. Repositorio en GitHub

| Requisito | Evidencia | Estado |
|---|---|---|
| Código fuente completo | `app/`, `frontend/`, `training/` | Cumplido |
| Dockerfile funcional | `Dockerfile` | Cumplido |
| Configuración | `requirements.txt`, `.dockerignore`, `docker-compose.yml` | Cumplido |
| Evidencia API | `/docs`, `/predict`, `/health` | Cumplido |

Repositorio:

https://github.com/3seatiger-stack/riesgo-crediticio-ml-docker

## 2. Contenedor Docker funcional

| Requisito | Evidencia | Estado |
|---|---|---|
| Imagen construida | `docker build` exitoso | Cumplido |
| Imagen visible | `docker images` | Cumplido |
| Ejecución local | `docker run` | Cumplido |
| Servicio accesible | `localhost:8080` | Cumplido |

## 3. Manual de despliegue en nube

| Requisito | Evidencia | Estado |
|---|---|---|
| Paso a paso | `docs/MANUAL_DESPLIEGUE.md` | Cumplido |
| Requerimientos técnicos | Sección de requerimientos | Cumplido |
| Estrategia | Docker + Cloud Run | Cumplido |
| Herramientas de documentación | `docs/USO_IA_DOCUMENTACION.md` | Cumplido |
| Despliegue público | URL Cloud Run | Cumplido |

URL pública:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app

## 4. Documento de validación y pruebas

| Requisito | Evidencia | Estado |
|---|---|---|
| Pruebas funcionales | `tests/test_api.py` | Cumplido |
| Casos extremos | `tests/test_cases.py` | Cumplido |
| Resultados | `9 passed` | Cumplido |
| Conclusiones | `docs/VALIDACION_PRUEBAS.md` | Cumplido |

## 5. Evidencia adicional

| Elemento | Evidencia | Estado |
|---|---|---|
| Swagger | `/docs` | Cumplido |
| POST /predict | HTTP 200 | Cumplido |
| CI | GitHub Actions verde | Cumplido |
| Despliegue continuo | GitHub + Cloud Build | Cumplido |
| Escalamiento | Cloud Run automático | Cumplido |
| Acceso público | URL HTTPS | Cumplido |

## 6. Evaluación global

La solución cubre los cuatro componentes principales solicitados:

1. repositorio;
2. contenedor;
3. despliegue;
4. validación.

Además, incorpora integración continua y despliegue público, elevando la madurez técnica de la entrega.
