from functools import lru_cache
from pathlib import Path
import json
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "random_forest_credito.joblib"
METADATA_PATH = BASE_DIR / "model" / "metadata.json"


@lru_cache(maxsize=1)
def load_resources():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"No se encontró el modelo en {MODEL_PATH}. "
            "Ejecute: python training/train_model.py"
        )
    model = joblib.load(MODEL_PATH)
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    return model, metadata


def predict_risk(payload: dict) -> dict:
    model, metadata = load_resources()
    features = metadata["feature_names"]
    frame = pd.DataFrame([[payload[name] for name in features]], columns=features)

    probability = float(model.predict_proba(frame)[0, 1])
    threshold = float(metadata["threshold"])
    prediction = int(probability >= threshold)

    if prediction == 1:
        classification = "Riesgo de incumplimiento"
        recommendation = "Enviar a revisión adicional antes de la decisión crediticia."
    else:
        classification = "Bajo riesgo"
        recommendation = "Continuar con el flujo normal, sujeto a políticas y revisión humana."

    return {
        "prediccion": prediction,
        "clasificacion": classification,
        "probabilidad_incumplimiento": round(probability, 4),
        "umbral_decision": threshold,
        "modelo": metadata["model_type"],
        "recomendacion": recommendation,
    }
