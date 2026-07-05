# Evidencias de Despliegue y Validación

## 1. Repositorio

Repositorio público:

https://github.com/3seatiger-stack/riesgo-crediticio-ml-docker

Rama principal:

```text
main
```

## 2. Construcción Docker

Comando ejecutado:

```bash
docker build -t riesgo-crediticio-api:1.0.0 .
```

Resultado esperado y validado:

- construcción sin errores;
- imagen registrada localmente;
- etiqueta `1.0.0`.

Evidencia sugerida:

```text
evidence/docker_build/01_docker_build_exitoso.png
```

## 3. Imagen Docker

Comando:

```bash
docker images
```

Resultado validado:

```text
riesgo-crediticio-api:1.0.0
```

Evidencia sugerida:

```text
evidence/docker_build/02_docker_images.png
```

## 4. Ejecución local

Comando:

```bash
docker run --rm -p 8080:8080 --name riesgo-crediticio-api riesgo-crediticio-api:1.0.0
```

Resultado validado:

```text
Application startup complete
Uvicorn running on http://0.0.0.0:8080
```

Evidencia sugerida:

```text
evidence/local_execution/01_contenedor_ejecucion.png
```

## 5. Frontend funcional

URL local:

```text
http://localhost:8080
```

Se validó:

- carga de interfaz;
- captura de diez variables;
- envío al backend;
- respuesta visible.

Evidencias sugeridas:

```text
evidence/local_execution/02_frontend.png
evidence/local_execution/03_resultado_prediccion.png
```

## 6. API documentada

URL local:

```text
http://localhost:8080/docs
```

Endpoints visibles:

```text
GET  /health
GET  /model-info
POST /predict
```

Evidencia sugerida:

```text
evidence/api_tests/01_swagger_endpoints.png
```

## 7. Prueba de POST /predict

Se ejecutó una solicitud real desde Swagger.

Resultado validado:

```text
HTTP 200
```

Ejemplo de respuesta observada:

```json
{
  "prediccion": 0,
  "clasificacion": "Bajo riesgo",
  "probabilidad_incumplimiento": 0.4,
  "umbral_decision": 0.62,
  "modelo": "RandomForestClassifier",
  "recomendacion": "Continuar con el flujo normal, sujeto a políticas y revisión humana."
}
```

Evidencia sugerida:

```text
evidence/api_tests/02_predict_200.png
```

## 8. Pruebas automatizadas

Comando ejecutado dentro de contenedor:

```bash
docker run --rm -v "${PWD}:/app" -w /app -e PYTHONPATH=/app python:3.12-slim sh -c "pip install -r requirements.txt && pytest -v"
```

Resultado validado:

```text
9 passed in 3.65s
```

Evidencia sugerida:

```text
evidence/api_tests/03_pytest_9_passed.png
```

## 9. Integración continua

Se configuró GitHub Actions.

Workflow:

```text
.github/workflows/tests.yml
```

Resultado final:

```text
Workflow aprobado con marca verde
```

Evidencia sugerida:

```text
evidence/api_tests/04_github_actions_green.png
```

## 10. Despliegue en Google Cloud Run

URL pública:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app

Región:

```text
us-central1
```

Configuración aplicada:

- despliegue continuo desde repositorio;
- Cloud Build;
- Dockerfile;
- facturación basada en solicitudes;
- ajuste de escala automático;
- acceso público;
- ingress permitido para todo el tráfico.

Evidencias sugeridas:

```text
evidence/cloud/01_cloud_run_servicio.png
evidence/cloud/02_cloud_run_url_publica.png
evidence/cloud/03_app_publica.png
```

## 11. Validación pública

Aplicación:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app

Swagger:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app/docs

Health:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app/health

Model info:

https://riesgo-crediticio-ml-docker-602622367890.us-central1.run.app/model-info

## 12. Conclusión

Las evidencias demuestran la correcta integración entre código fuente, API, modelo, contenedor, pruebas, repositorio y plataforma de nube.
