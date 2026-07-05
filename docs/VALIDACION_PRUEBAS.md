# Documento de validación y pruebas

## 1. Objetivo

Comprobar el funcionamiento del sistema de evaluación de riesgo crediticio en sus capas de API, validación de datos, inferencia del modelo, interfaz y portabilidad mediante contenedor.

## 2. Entorno de referencia

- Python: 3.13.5
- scikit-learn: 1.8.0
- pandas: 2.2.3
- numpy: 2.3.5
- Modelo: RandomForestClassifier
- Umbral: 0.62
- Datos: sintéticos, 2,500 observaciones

## 3. Pruebas funcionales definidas

| ID | Prueba | Entrada | Esperado |
|---|---|---|---|
| CP-01 | Health check | GET `/health` | HTTP 200 |
| CP-02 | Información modelo | GET `/model-info` | umbral 0.62 |
| CP-03 | Predicción válida | POST JSON completo | HTTP 200 |
| CP-04 | Ingreso negativo | ingreso -5000 | HTTP 422 |
| CP-05 | Utilización > 1 | 1.5 | HTTP 422 |
| CP-06 | Campo faltante | sin monto | HTTP 422 |
| CP-07 | Tipo incorrecto | texto en ingreso | HTTP 422 |
| CP-08 | Límites mínimos | valores mínimos válidos | HTTP 200 |
| CP-09 | Límites superiores | valores máximos permitidos | HTTP 200 |

## 4. Casos extremos

### 4.1 Valor negativo
Se espera rechazo previo a inferencia.

### 4.2 Proporción fuera de rango
`utilizacion_credito > 1` debe producir HTTP 422.

### 4.3 Payload incompleto
La ausencia de cualquier variable obligatoria debe producir HTTP 422.

### 4.4 Tipo incompatible
Texto no numérico en una variable cuantitativa debe producir HTTP 422.

### 4.5 Valores de frontera
Los límites explícitamente permitidos deben ser procesables y devolver HTTP 200.

## 5. Validación del artefacto empaquetado

Métricas obtenidas durante la generación de este paquete:

| Métrica | Resultado |
|---|---:|
| Accuracy | 0.9040 |
| Precision | 0.9360 |
| Recall | 0.6923 |
| F1 | 0.7959 |
| AUC | 0.9687 |

Matriz de confusión del artefacto:

```text
[[448, 8], [52, 117]]
```

Las métricas académicas históricas de referencia se conservan por separado en `model/metadata.json`; esto evita presentar como idénticos resultados provenientes de artefactos o entornos distintos.

## 6. Pruebas automatizadas

Ejecutar:

```bash
pytest -v
```

Criterio de aceptación:

```text
100% de pruebas automatizadas aprobadas.
```

## 7. Prueba de integración frontend-backend

1. Abrir `/`.
2. Capturar diez variables.
3. Pulsar **Evaluar riesgo**.
4. Verificar llamada `POST /predict`.
5. Confirmar respuesta visible con probabilidad, clasificación, umbral y recomendación.

## 8. Prueba Docker

```bash
docker build -t riesgo-crediticio-api:1.0.0 .
docker run --rm -p 8080:8080 riesgo-crediticio-api:1.0.0
curl http://localhost:8080/health
```

Criterios:

- imagen construida sin error;
- contenedor en ejecución;
- puerto 8080 accesible;
- health check HTTP 200;
- `/docs` disponible;
- `/predict` funcional.

## 9. Resultados y conclusiones

La solución incorpora validación de esquema, endpoints operativos, integración frontend-backend y un artefacto serializado. Los casos extremos son rechazados antes de la inferencia cuando incumplen rangos o tipos.

La validación local del código debe complementarse con evidencia visual del equipo donde se ejecute Docker, ya que la entrega académica debe demostrar la construcción real de la imagen y la ejecución real del contenedor.

## 10. Limitaciones

- Datos sintéticos.
- No existe validación externa con cartera real.
- No se implementa autenticación.
- No se incluye monitoreo de drift.
- No se ha realizado análisis formal de equidad.
- La salida no sustituye decisión humana.
