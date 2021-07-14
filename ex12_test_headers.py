import requests

class TestCookies:
    def test_cookies(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers = dict(response1.headers)
        print(headers)

        response2 = requests.get("https://playground.learnqa.ru/api/homework_header")
        assert response2.headers.keys() == headers.keys(), "Headers mismatching"
