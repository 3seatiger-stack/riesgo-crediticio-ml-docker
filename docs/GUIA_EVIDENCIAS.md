# Guía de evidencias para la entrega académica

La carpeta `evidence/` contiene subcarpetas vacías para colocar capturas reales. No se incluyen capturas simuladas.

## Evidencia 1 — Docker build

Guardar en:

```text
evidence/docker_build/
```

Capturar terminal mostrando:

```bash
docker build -t riesgo-crediticio-api:1.0.0 .
```

y el mensaje final de construcción exitosa.

## Evidencia 2 — Imagen creada

Capturar:

```bash
docker images
```

Debe verse `riesgo-crediticio-api`.

## Evidencia 3 — Contenedor local

Guardar en:

```text
evidence/local_execution/
```

Capturar:

```bash
docker ps
```

y el navegador en:

```text
http://localhost:8080
```

## Evidencia 4 — API

Guardar en:

```text
evidence/api_tests/
```

Capturar:

- `/docs`;
- ejecución de `POST /predict`;
- respuesta JSON;
- `/health`.

## Evidencia 5 — Pytest

Capturar:

```bash
pytest -v
```

con todas las pruebas aprobadas.

## Evidencia 6 — Nube

Guardar en:

```text
evidence/cloud/
```

Capturar:

- servicio Cloud Run;
- URL pública;
- `/health`;
- aplicación desplegada.

## Regla de integridad

Las evidencias deben provenir de ejecuciones reales. No deben fabricarse ni alterarse para aparentar resultados.
