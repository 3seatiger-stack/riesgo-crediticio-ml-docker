from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.schemas import CreditApplication, PredictionResponse
from app.model_service import load_resources, predict_risk

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_resources()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="API de Riesgo Crediticio",
    version="1.0.0",
    description=(
        "API REST para estimar la probabilidad de incumplimiento crediticio a 90 días "
        "mediante un modelo Random Forest y umbral de decisión 0.62."
    ),
)

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/health", tags=["Operación"])
def health():
    _, metadata = load_resources()
    return {
        "status": "ok",
        "model_loaded": True,
        "model_type": metadata["model_type"],
        "threshold": metadata["threshold"],
    }


@app.get("/model-info", tags=["Modelo"])
def model_info():
    _, metadata = load_resources()
    return metadata


@app.post("/predict", response_model=PredictionResponse, tags=["Predicción"])
def predict(application: CreditApplication):
    return predict_risk(application.model_dump())
