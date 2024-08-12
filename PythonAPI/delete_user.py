import requests

c = requests.delete("https://reqres.in/api/users/2")
# print(c.json())
print(c.status_code)
assert c.status_code == 204, "user deletation failed"
