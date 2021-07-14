import requests

class TestCookies:
    def test_cookies(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = dict(response1.cookies)
        print(cookie)

        response2 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        assert response2.cookies == cookie, "endpoint returns incorrect cookies"
