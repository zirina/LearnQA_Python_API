import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect")
redirect_num = len(response.history)

print("number of redirect steps is " + str(redirect_num))