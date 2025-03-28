from api.endpoints.get import GetAPI

def test_get_character_returns_data():
    api = GetAPI()
    response = api.get_character(page=1)

    assert response.status_code == 200
    body = response.json()
    assert "results" in body
    assert isinstance(body["results"], list)
    assert len(body["results"]) > 0
