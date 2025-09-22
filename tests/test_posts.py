import requests
import jsonschema

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200

    data=response.json()
    print(data)
    assert isinstance(data, list)
    assert "title" in data[0]