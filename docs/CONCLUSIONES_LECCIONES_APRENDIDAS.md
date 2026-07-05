# Conclusiones y Lecciones Aprendidas

## 1. Conclusión general

El proyecto permitió transformar un modelo de Machine Learning previamente construido en una solución técnica completa y desplegable.

El resultado final demuestra que el desarrollo de un modelo predictivo constituye sólo una parte del ciclo de vida de una solución de inteligencia artificial. Para que el modelo pueda utilizarse en un entorno real o demostrable, es necesario integrar componentes de software, APIs, validación de entradas, pruebas, portabilidad y despliegue.

## 2. Principales logros

### 2.1 Operacionalización del modelo

El Random Forest dejó de depender de un notebook y fue integrado como artefacto serializado dentro de un servicio de inferencia.

### 2.2 Integración frontend-backend

Se implementó una interfaz web capaz de enviar datos a la API mediante JSON y presentar la respuesta del modelo al usuario.

### 2.3 API REST

FastAPI permitió exponer endpoints claros y verificables, además de documentación interactiva mediante Swagger/OpenAPI.

### 2.4 Portabilidad

Docker permitió empaquetar aplicación, dependencias y modelo en una imagen reproducible.

### 2.5 Automatización de pruebas

Pytest permitió validar casos funcionales y extremos.

### 2.6 Integración continua

GitHub Actions permitió ejecutar pruebas automáticamente ante cambios en el repositorio.

### 2.7 Despliegue en nube

Cloud Run permitió convertir el contenedor en un servicio público accesible mediante HTTPS.

## 3. Lecciones aprendidas

### 3.1 Un modelo no equivale a una solución

Un modelo con buenas métricas no es suficiente. Para generar valor debe integrarse en una arquitectura utilizable.

### 3.2 La reproducibilidad es crítica

Las dependencias, versiones y artefactos deben estar explícitamente documentados.

### 3.3 La validación debe incluir errores

Los casos extremos y entradas inválidas son tan importantes como los casos exitosos.

### 3.4 El entorno importa

Durante la implementación se identificó un problema de importación relacionado con `PYTHONPATH`. El mismo error apareció en pruebas dentro de contenedor y en GitHub Actions.

La corrección permitió comprender la importancia de controlar el contexto de ejecución.

### 3.5 La evidencia debe ser real

Las capturas y resultados deben provenir de ejecuciones verificables. No se deben simular construcciones, despliegues o pruebas.

### 3.6 La nube requiere decisiones de arquitectura

El despliegue exigió definir región, acceso público, escalamiento, integración continua y estrategia de construcción.

## 4. Limitaciones

- Los datos son sintéticos.
- No existe validación con cartera real.
- No se implementa autenticación.
- No se incorpora monitoreo de drift.
- No existe análisis formal de equidad.
- No se ha implementado explicabilidad individual.
- El sistema no debe utilizarse para decisiones crediticias reales sin gobierno y validación adicional.

## 5. Trabajo futuro

Como evolución se propone:

- incorporar autenticación;
- registrar predicciones y auditoría;
- implementar monitoreo del modelo;
- detectar drift;
- evaluar sesgo;
- incorporar explicabilidad con SHAP;
- separar frontend y backend en servicios independientes;
- agregar base de datos;
- implementar versionado de modelos;
- integrar MLOps.

## 6. Reflexión final

La principal enseñanza fue comprender que la inteligencia artificial aplicada requiere la convergencia de análisis, ingeniería de software, infraestructura, validación y comunicación técnica.

El proyecto demuestra una transición completa desde experimentación hasta despliegue y constituye una base sólida para soluciones de IA más avanzadas.
