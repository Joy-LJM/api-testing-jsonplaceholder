import requests
import jsonschema

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200

    data=response.json()
    print(data)
    assert data['id'] == 1
    assert "username" in data # check key in dictionary