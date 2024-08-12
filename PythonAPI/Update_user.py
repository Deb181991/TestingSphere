import requests

payload = {
    "name": "morpheus",
    "job": "zion resident"
}
# mydata = open("data.json", "r").read()
# a = requests.post("https://reqres.in/api/users", data=json.loads(open("data.json", "r").read()))
# b = requests.put("https://reqres.in/api/users/2", data=payload)
b = requests.patch("https://reqres.in/api/users/2", data=payload)
# a = requests.post("https://reqres.in/api/register", data=payload)
print(b)
print(b.json())
print(b.headers.get("Content-Type"))
