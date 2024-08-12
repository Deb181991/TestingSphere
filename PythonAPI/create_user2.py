import json

import requests

# url = "https://reqres.in/api/users"
# "https://uat-app.lineclearexpressonline.com/Accounts/CreateShipment"
url = "https://uat-app.lineclearexpressonline.com/Accounts/CreateShipment"
user = "suraj.parida71@gmail.com"
passwd = "Test@1234"
auth_value = (user, passwd)
# mydata = open("data.json", "r").read()
a = requests.post(url, data=json.loads(open("data.json", "r").read()))
print(a)
print(a.json())
print(a.headers)
print(a.content)
# assert a.json()['job'] == 'Automation developer'
