import requests
payload = {
    "name": "morpheus",
    "job": "leader"
}
resp =requests.post("https://reqres.in/api/users", data = payload)
#print(resp.json())
assert resp.json()['job'] == 'leader'
