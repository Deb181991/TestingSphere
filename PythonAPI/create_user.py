import requests

payload = {
    "name": "subha",
    "job": "Automation"
}
a = requests.post("https://reqres.in/api/users", data=payload)
print(a)
print(a.json())
assert a.json()['job'] == 'Automation'
