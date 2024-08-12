import requests

a = requests.get("https://reqres.in/api/users?page=2")
print(a)
# print(type(a))
# print(dir(a))
code = a.status_code
assert code == 200, "code doesn't matched"
# print(a.text)
# print(a.content)
print(a.json())
print(type(a.headers))
print(a.headers)
print(a.cookies)
print(a.encoding)
print(a.url)
json_responce = a.json()
print(json_responce['total_pages'])
print(json_responce['total'])
