# Manual de despliegue

## 1. Requerimientos técnicos

### Local
- Git
- Docker Desktop o Docker Engine
- 2 GB de RAM disponibles como mínimo recomendado
- Puerto 8080 libre

### Desarrollo sin Docker
- Python 3.12
- `pip`
- entorno virtual recomendado

### Nube
- Cuenta y proyecto de Google Cloud
- facturación habilitada cuando aplique
- Google Cloud CLI (`gcloud`)
- APIs necesarias habilitadas para Artifact Registry, Cloud Build y Cloud Run
- permisos para construir imágenes y desplegar servicios

## 2. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd riesgo-crediticio-ml-docker
```

## 3. Validación local con Python

```bash
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

Validar:

```text
http://localhost:8080
http://localhost:8080/docs
http://localhost:8080/health
```

## 4. Construcción Docker

```bash
docker build -t riesgo-crediticio-api:1.0.0 .
```

Verificar imagen:

```bash
docker images
```

## 5. Ejecución local del contenedor

```bash
docker run --rm -p 8080:8080 --name riesgo-crediticio-api riesgo-crediticio-api:1.0.0
```

Validar:

```bash
curl http://localhost:8080/health
```

## 6. Ejecución con Docker Compose

```bash
docker compose up --build
```

Detener:

```bash
docker compose down
```

## 7. Pruebas

```bash
pytest -v
```

## 8. Estrategia de nube seleccionada

Se propone **Google Cloud Run**, una plataforma administrada para ejecutar contenedores. La misma imagen validada localmente se publica en un registro y después se despliega como servicio.

```text
Repositorio
   ↓
Cloud Build
   ↓
Artifact Registry
   ↓
Cloud Run
   ↓
URL HTTPS
```

## 9. Despliegue paso a paso en Google Cloud Run

### 9.1 Autenticación

```bash
gcloud auth login
```

### 9.2 Seleccionar proyecto

```bash
gcloud config set project ID_PROYECTO
```

### 9.3 Habilitar servicios

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
```

### 9.4 Crear repositorio Docker

Ejemplo con región `us-central1`:

```bash
gcloud artifacts repositories create ml-repo   --repository-format=docker   --location=us-central1   --description="Contenedores de proyectos ML"
```

### 9.5 Construir y publicar

```bash
gcloud builds submit   --tag us-central1-docker.pkg.dev/ID_PROYECTO/ml-repo/riesgo-crediticio:1.0.0
```

### 9.6 Desplegar

```bash
gcloud run deploy riesgo-crediticio   --image us-central1-docker.pkg.dev/ID_PROYECTO/ml-repo/riesgo-crediticio:1.0.0   --region us-central1   --platform managed   --port 8080   --allow-unauthenticated
```

### 9.7 Validar

Abrir la URL devuelta por Cloud Run:

```text
https://URL_DEL_SERVICIO/
https://URL_DEL_SERVICIO/health
https://URL_DEL_SERVICIO/docs
```

## 10. Estrategia alternativa PaaS

Como alternativa se puede utilizar un PaaS compatible con Docker. La decisión debe conservar:

- variable `PORT`;
- escucha en `0.0.0.0`;
- imagen reproducible;
- health check;
- logs centralizados.

## 11. Rollback

Publicar versiones inmutables:

```text
1.0.0
1.0.1
1.1.0
```

Ante una regresión se redirige tráfico a una revisión estable previa.

## 12. Buenas prácticas

- No incluir secretos en Git.
- Fijar versiones de dependencias.
- Ejecutar pruebas antes de construir.
- Etiquetar imágenes.
- Conservar logs.
- Documentar cambios.
- Revalidar el modelo ante cambios de datos.
