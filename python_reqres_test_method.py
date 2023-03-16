import requests
p = {"page":5}
resp = requests.get("https://reqres.in/api/users?page=2",params = p)
#print(resp.url)
#print(resp)
#print(type(resp))#object of response class
#code = resp.status_code
#assert code == 200, "code doesn't match"
#print(resp.text)
#print(resp.content)

#print(resp.json())
#print(resp.headers)
#print(type(resp.headers))#dict
#print(resp.encoding)
#print(resp.cookies)
#print(resp.url)
#json_response = resp.json()
#print(json_response['total'])
#assert json_response['total'] == 12
#print(json_response['total_pages'])
#assert json_response['total_pages'] == 2
#print(json_response["data"][0]["id"])

