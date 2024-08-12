import requests

responce = requests.post("https://uat-app.lineclearexpressonline.com/Accounts/CreateShipment")
print(responce.content)
