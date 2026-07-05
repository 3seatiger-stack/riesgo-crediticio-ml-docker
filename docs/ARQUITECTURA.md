# Arquitectura técnica

## 1. Visión general

La solución separa presentación, servicio de inferencia y artefacto de Machine Learning.

```text
┌────────────────────┐
│ Frontend HTML/CSS  │
│ JavaScript         │
└─────────┬──────────┘
          │ fetch POST /predict
          ▼
┌────────────────────┐
│ FastAPI            │
│ Validación Pydantic│
└─────────┬──────────┘
          │ DataFrame ordenado
          ▼
┌────────────────────┐
│ Random Forest      │
│ .joblib            │
└─────────┬──────────┘
          │ predict_proba
          ▼
┌────────────────────┐
│ Umbral 0.62        │
│ Resultado JSON     │
└────────────────────┘
```

## 2. Componentes

### Frontend
Captura diez variables y consume la API mediante `fetch`.

### Backend
FastAPI expone:

- `GET /`: interfaz web;
- `GET /health`: disponibilidad y carga del modelo;
- `GET /model-info`: metadatos;
- `POST /predict`: inferencia.

### Modelo
`model/random_forest_credito.joblib`.

### Validación
Pydantic restringe rangos y tipos antes de invocar el modelo.

## 3. Decisiones de diseño

1. **Una imagen contenedora**: simplifica portabilidad y demostración académica.
2. **Modelo cargado una vez**: se usa caché para evitar recarga por solicitud.
3. **Metadatos externos**: el umbral y el orden de variables quedan explícitos.
4. **Health endpoint**: facilita pruebas locales y despliegue.
5. **OpenAPI**: FastAPI genera `/docs` sin duplicar documentación manual.

## 4. Flujo de predicción

1. Usuario captura datos.
2. JavaScript serializa JSON.
3. FastAPI valida esquema.
4. Backend ordena las diez variables.
5. Random Forest calcula `predict_proba`.
6. Se compara probabilidad con 0.62.
7. API devuelve clasificación, probabilidad y recomendación.

## 5. Consideraciones de producción

Para un sistema real serían necesarios autenticación, TLS gestionado, registro de auditoría, cifrado, secret manager, monitoreo, control de drift, análisis de sesgo, explicabilidad y revisión humana.
