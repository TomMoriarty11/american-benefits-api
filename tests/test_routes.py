from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_ca_benefits():
    response = client.get("/benefits/CA")
    assert response.status_code == 200
    assert "programs" in response.json()
