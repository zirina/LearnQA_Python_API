import requests

tested_endpoint = "https://playground.learnqa.ru/ajax/api/compare_query_type"
paramsList = ["GET", "PUT", "POST", "DELETE"]

#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response_delete = requests.delete(tested_endpoint)
output_delete = response_delete.text
if not output_delete:
    print("Output_delete is empty")
else:
    print(f"{output_delete=}")
print('')

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response_head = requests.head(tested_endpoint, data={"method":"HEAD"})
output_head = response_head.text
if not output_head:
    print("Output_head is empty")
else:
    print(f"{output_head=}")
print('')

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response_post = requests.post(tested_endpoint, data={"method": "POST"})
print("response POST " + response_post.text)
response_get = requests.get(tested_endpoint, params={"method": "GET"})
print("response GET " + response_get.text)
response_put = requests.put(tested_endpoint, data={"method": "PUT"})
print("response PUT " + response_put.text)
response_delete = requests.delete(tested_endpoint, data={"method": "DELETE"})
print("response DELETE " + response_delete.text)
print('')

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method
for i in range(len(paramsList)):
    print("GET-запрос передает значения параметра method равное " + paramsList[i])
    response = requests.get(tested_endpoint, params={"method": paramsList[i]})
    print(response.text)
    paramsList = ["GET", "PUT", "POST", "DELETE"]
print('')

for i in range(len(paramsList)):
    print("PUT-запрос передает значения параметра method равное " + paramsList[i])
    response = requests.put(tested_endpoint, data={"method": paramsList[i]})
    print(response.text)
print('')

for i in range(len(paramsList)):
    print("POST-запрос передает значения параметра method равное " + paramsList[i])
    response = requests.post(tested_endpoint, data={"method": paramsList[i]})
    print(response.text)
print('')

for i in range(len(paramsList)):
    print("DELETE-запрос передает значения параметра method равное " + paramsList[i])
    response = requests.delete(tested_endpoint, params={"method": paramsList[i]})
    print(response.text)

