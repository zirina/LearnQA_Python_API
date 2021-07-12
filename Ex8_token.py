import requests
import json
import time

# 1 запрос API начинает выполнения задачи, создает задачу
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
json_data = json.loads(response1.text)
token_value = json_data["token"]
waiting_time = json_data["seconds"]

# 2 запрос вызвает метод, УКАЗАВ GET-параметром token
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token_value})
if  ("error" in json.loads(response2.text)):
    print("для token: " + token_value + " задача не создавалась")
else:
    status_value = json.loads(response2.text)["status"]
    if status_value=="Job is NOT ready":
        print("задача еще не готова, время ожидания " + str(waiting_time) + " секунд")
        time.sleep(waiting_time)
    # 3 запрос c token ПОСЛЕ того, как задача готова, убеждается в правильности поля status и наличии поля result
    response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token_value})
    if ("result" in json.loads(response3.text) and json.loads(response3.text)["status"] == "Job is ready"):
        print("задача готова, поля status и result в наличии,  status: " + json.loads(response3.text)[
            "status"] + ", result: " + str(json.loads(response3.text)["result"]))
    else:
        print("unexpected error")
