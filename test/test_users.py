import json
from app import schema
from jose import jwt
from app.config import setting

def test_getmethod(client):
    res = client.get("/")
    print(res.json().get("msg"))
    assert res.json().get("msg") == "Hai Mylu Iam Juju"
    assert res.status_code == 200


# def test_create_user(client):
#     res = client.post("/reg",json ={"firstname":"Mercy","lastname":"Angelin","phone":"8765432876","email":"mercy@gmail.com","dob":"2000-08-04","gender":"female","pwd":"mylu"})
#     print(res.json())
#     assert res.json().get('detail') == "Email id already registered"

def test_login(client,test_user):
    res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
    login_res = schema.Token(**res.json())
    payload = jwt.decode(login_res.access_token,setting.secret_key,setting.algorithm)
    id:str = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

def test_wrong_user(client,test_user):
    res = client.post("/login",data={"username":test_user['email'],"password":"myklihiholu"})
    print(test_user['password'])
    print(res.json())
    assert res.status_code == 403

