from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.preprocessing import QuantileTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix
)

ROOT = Path(__file__).resolve().parent.parent
MODEL_DIR = ROOT / "model"
MODEL_DIR.mkdir(exist_ok=True)

FEATURES = [
    "ingreso_mensual","antiguedad_laboral","saldo_promedio",
    "utilizacion_credito","historial_moras","relacion_deuda_ingreso",
    "edad_cuenta","consultas_buro","variabilidad_ingreso","monto_solicitado"
]
THRESHOLD = 0.62


def build_dataset():
    np.random.seed(42)
    X, y = make_classification(
        n_samples=2500, n_features=10, n_informative=6, n_redundant=2,
        weights=[0.74, 0.26], flip_y=0.04, class_sep=1.05, random_state=42
    )
    qt = QuantileTransformer(output_distribution="normal", random_state=42)
    raw = pd.DataFrame(qt.fit_transform(X), columns=FEATURES)

    raw["ingreso_mensual"] = np.round(
        25000 + raw["ingreso_mensual"]*9000 + np.random.normal(0,2500,len(raw))
    ).clip(6000,90000)
    raw["antiguedad_laboral"] = np.round((4 + raw["antiguedad_laboral"]*2.2).clip(0,20),1)
    raw["saldo_promedio"] = np.round((15000 + raw["saldo_promedio"]*7000).clip(0,60000))
    raw["utilizacion_credito"] = np.round((0.52 + raw["utilizacion_credito"]*0.18).clip(0.05,0.98),2)
    raw["historial_moras"] = np.round((1.2 + raw["historial_moras"]*0.9).clip(0,7)).astype(int)
    raw["relacion_deuda_ingreso"] = np.round((0.36 + raw["relacion_deuda_ingreso"]*0.12).clip(0.02,0.95),2)
    raw["edad_cuenta"] = np.round((5 + raw["edad_cuenta"]*2.3).clip(0,25),1)
    raw["consultas_buro"] = np.round((2 + raw["consultas_buro"]*1.2).clip(0,12)).astype(int)
    raw["variabilidad_ingreso"] = np.round((0.20 + raw["variabilidad_ingreso"]*0.08).clip(0.01,0.75),2)
    raw["monto_solicitado"] = np.round((70000 + raw["monto_solicitado"]*25000).clip(5000,250000))
    return raw, y


def main():
    X, y = build_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=300, class_weight="balanced", random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train)

    probability = model.predict_proba(X_test)[:,1]
    prediction = (probability >= THRESHOLD).astype(int)
    cm = confusion_matrix(y_test, prediction)

    metrics = {
        "accuracy": float(accuracy_score(y_test, prediction)),
        "precision": float(precision_score(y_test, prediction)),
        "recall": float(recall_score(y_test, prediction)),
        "f1": float(f1_score(y_test, prediction)),
        "auc": float(roc_auc_score(y_test, probability)),
        "confusion_matrix": cm.tolist()
    }

    joblib.dump(model, MODEL_DIR / "random_forest_credito.joblib")
    metadata = {
        "project_name": "Sistema Inteligente de Evaluación de Riesgo Crediticio",
        "model_type": "RandomForestClassifier",
        "threshold": THRESHOLD,
        "target": "incumplimiento_90d",
        "positive_class": 1,
        "feature_names": FEATURES,
        "dataset": {"type": "synthetic", "records": 2500, "random_state": 42},
        "reference_academic_metrics": {
            "accuracy": 0.9168, "precision": 0.8589, "recall": 0.8284,
            "f1": 0.8434, "auc": 0.9593
        },
        "packaged_model_validation_metrics": metrics
    }
    (MODEL_DIR / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("Modelo guardado correctamente.")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
