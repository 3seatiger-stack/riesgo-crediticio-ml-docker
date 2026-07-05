from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_minimum_valid_values():
    payload = {
        "ingreso_mensual": 0,
        "antiguedad_laboral": 0,
        "saldo_promedio": 0,
        "utilizacion_credito": 0,
        "historial_moras": 0,
        "relacion_deuda_ingreso": 0,
        "edad_cuenta": 0,
        "consultas_buro": 0,
        "variabilidad_ingreso": 0,
        "monto_solicitado": 0
    }
    assert client.post("/predict", json=payload).status_code == 200


def test_upper_valid_boundaries():
    payload = {
        "ingreso_mensual": 1_000_000,
        "antiguedad_laboral": 60,
        "saldo_promedio": 10_000_000,
        "utilizacion_credito": 1,
        "historial_moras": 100,
        "relacion_deuda_ingreso": 1,
        "edad_cuenta": 100,
        "consultas_buro": 100,
        "variabilidad_ingreso": 1,
        "monto_solicitado": 100_000_000
    }
    assert client.post("/predict", json=payload).status_code == 200
