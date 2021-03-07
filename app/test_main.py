from fastapi.testclient import TestClient
from main import app
from datafortesting import(
    test_main_get_pokemon_by_name_bad_input_js,
    test_main_get_pokemon_by_name_ok_js,
    test_main_get_pokemon_list_ok_js,
    test_main_get_pokemon_list_bad_input_js)

client = TestClient(app)

def test_main_get_pokemon_by_name_bad_input():
    response = client.get("/")
    assert response.status_code == 422
    assert response.json() == test_main_get_pokemon_by_name_bad_input_js

def test_main_get_pokemon_by_name_not_found():
    response = client.get("/dtoo")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokemon name not found"}

def test_main_get_pokemon_by_name_stringnumer_paramenter():
    response = client.get("/3")
    assert response.status_code == 422
    assert response.json() == {"detail": "the parameter must be the name, not the ID"}

def test_main_get_pokemon_by_name_ok():
    response = client.get("/ditto")
    assert response.status_code == 200
    assert response.json() == test_main_get_pokemon_by_name_ok_js

def test_main_get_pokemon_list_bad_input():
    response = client.get("/?q=ch&offset=0&limit=0")
    assert response.status_code == 422
    assert response.json() == test_main_get_pokemon_list_bad_input_js

def test_main_get_pokemon_list_name_not_found():
    response = client.get("/?q=asdasd&offset=1&limit=1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokemon name not found"}

def test_main_get_pokemon_list_ok():
    response = client.get("/?q=cha&offset=5&limit=5")
    assert response.status_code == 200
    assert response.json() == test_main_get_pokemon_list_ok_js