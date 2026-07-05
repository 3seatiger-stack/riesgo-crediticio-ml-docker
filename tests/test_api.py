from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

VALID_PAYLOAD = {
    "ingreso_mensual": 32000,
    "antiguedad_laboral": 5.5,
    "saldo_promedio": 18000,
    "utilizacion_credito": 0.65,
    "historial_moras": 2,
    "relacion_deuda_ingreso": 0.42,
    "edad_cuenta": 6.0,
    "consultas_buro": 3,
    "variabilidad_ingreso": 0.20,
    "monto_solicitado": 85000
}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["model_loaded"] is True


def test_model_info():
    response = client.get("/model-info")
    assert response.status_code == 200
    assert response.json()["threshold"] == 0.62


def test_prediction_valid():
    response = client.post("/predict", json=VALID_PAYLOAD)
    assert response.status_code == 200
    body = response.json()
    assert body["prediccion"] in [0, 1]
    assert 0 <= body["probabilidad_incumplimiento"] <= 1
    assert body["umbral_decision"] == 0.62


def test_negative_income_rejected():
    payload = VALID_PAYLOAD | {"ingreso_mensual": -5000}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_credit_utilization_over_one_rejected():
    payload = VALID_PAYLOAD | {"utilizacion_credito": 1.5}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_missing_field_rejected():
    payload = VALID_PAYLOAD.copy()
    payload.pop("monto_solicitado")
    response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_wrong_type_rejected():
    payload = VALID_PAYLOAD | {"ingreso_mensual": "mucho dinero"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
