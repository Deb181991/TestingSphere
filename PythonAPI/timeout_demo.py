import requests

a = requests.get("https://httpbin.org/delay/5", timeout=5)
print(a.status_code)
