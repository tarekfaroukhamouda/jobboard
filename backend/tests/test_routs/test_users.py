import json

def test_create_user(client):
    data={"username":"Tarek Farouk Hamouda","email":"tarek@yahoo.com","password":"11111111"}
    response=client.post("/users",json.dumps(data))
    assert response.status_code == 200