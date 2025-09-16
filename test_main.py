from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_endpoint_rechazo():
    respuesta = client.get("/evaluaciones/tarjetas?edad=17&ingresos=2000")
    assert respuesta.status_code == 200
    assert respuesta.json()["status"] == "RECHAZADO"

def test_endpoint_regular():
    respuesta = client.get("/evaluaciones/tarjetas?edad=24&ingresos=3500")
    assert respuesta.status_code == 200
    body = respuesta.json()
    assert body["status"] == "APROBADO"
    assert body["data"]["categoria"] == "Tarjeta OH"

def test_endpoint_premium():
    respuesta = client.get("/evaluaciones/tarjetas?edad=30&ingresos=7500")
    assert respuesta.status_code == 200
    body = respuesta.json()
    assert body["status"] == "APROBADO"
    assert body["data"]["categoria"] == "Tarjeta OH Premium"

def test_endpoint_datos_invalidos():
    respuesta = client.get("/evaluaciones/tarjetas?edad=-5&ingresos=3000")
    assert respuesta.status_code == 400
    assert respuesta.json()["detail"] == "Datos inválidos"

