import requests
import re

def run_apis1(mobile_no):
    results = []
    
    # Ensure number starts with +91
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 1: Hoichoi ---
    try:
        url1 = "https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code"
        headers1 = {
            "accept": "*/*",
            "accept-language": "en-IN,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.hoichoi.tv",
            "referer": "https://www.hoichoi.tv/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
        }
        payload1 = {"phoneNumber": number}
        r1 = requests.post(url1, headers=headers1, json=payload1, timeout=10)
        results.append({"service": "Hoichoi", "status": r1.status_code, "response": r1.text})
        print(f"Hoichoi: {r1.status_code}")
    except Exception as e:
        results.append({"service": "Hoichoi", "status": "Error", "response": str(e)})
        print(f"Hoichoi Error: {e}")

    # --- API 2: ShemarooMe ---
    try:
        url2 = "https://www.shemaroome.com/users/mobile_no_signup"
        headers2 = {
            "authority": "www.shemaroome.com",
            "accept": "*/*",
            "accept-language": "en-IN,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.shemaroome.com",
            "referer": "https://www.shemaroome.com/users/sign_in",
            "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        data2 = {"mobile_no": number, "registration_source": "organic"}
        r2 = requests.post(url2, headers=headers2, data=data2, timeout=10)
        results.append({"service": "ShemarooMe", "status": r2.status_code, "response": r2.text})
        print(f"ShemarooMe: {r2.status_code}")
    except Exception as e:
        results.append({"service": "ShemarooMe", "status": "Error", "response": str(e)})
        print(f"ShemarooMe Error: {e}")

    # --- API 3: Hathway ---
    try:
        session = requests.Session()
        homepage_url = "https://www.hathway.com/Home/NewConnection"
        home = session.get(homepage_url, timeout=10)
        match = re.search(r'name="csrf-token" content="(.*?)"', home.text)
        if not match:
            results.append({"service": "Hathway", "status": "Error", "response": "CSRF token not found"})
        else:
            csrf_token = match.group(1)
            headers3 = {
                'authority': 'www.hathway.com',
                'accept': '*/*',
                'accept-language': 'en-IN,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.hathway.com',
                'referer': homepage_url,
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
                'x-csrf-token': csrf_token,
                'x-requested-with': 'XMLHttpRequest',
            }
            data3 = {'c_contact': number.replace("+91", "")}
            r3 = session.post("https://www.hathway.com/api/sendOtp", headers=headers3, data=data3, timeout=10)
            results.append({"service": "Hathway", "status": r3.status_code, "response": r3.text})
            print(f"Hathway: {r3.status_code}")
    except Exception as e:
        results.append({"service": "Hathway", "status": "Error", "response": str(e)})
        print(f"Hathway Error: {e}")

    # --- API 4: Licious ---
    try:
        url4 = "https://www.licious.in/api/login/signup"
        headers4 = {
            "accept": "*/*",
            "accept-language": "en-IN,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.licious.in",
            "referer": "https://www.licious.in/profile",
            "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "serverside": "false",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        }
        json_data = {"phone": number.replace("+91", ""), "captcha_token": ""}
        r4 = requests.post(url4, headers=headers4, json=json_data, timeout=10)
        results.append({"service": "Licious", "status": r4.status_code, "response": r4.text})
        print(f"Licious: {r4.status_code}")
    except Exception as e:
        results.append({"service": "Licious", "status": "Error", "response": str(e)})
        print(f"Licious Error: {e}")

    # --- API 5: Box8 ---
    try:
        url5 = "https://accounts.box8.co.in/customers/sign_up"
        headers5 = {
            'authority': 'accounts.box8.co.in',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en;q=0.9',
            'authorization': 'Bearer eyJraWQiOiIxZWQ1ZDFiNjI5NDY0MmFlOWEyZGU2NDQzZWZlZmI2Y2I8OTRkMjAwNjU0NGUzYzljOWE3N2JkM2UwYzkyNThhIiwiYWxnIjoiUlMyNTYifQ.eyJpYXQiOjE3NTcwODU4MjcsImV4cCI6MTc1NzIwNTAwMCwic3NpZCI6IjRiNzg3NWMxLTE4MzctNDg3MS05MmI4LTFmN2RmMDc5NzUzYzE3NTcwODU4MjciLCJhY2Nfd3lwZSI6IkFub255bW91c0FjY291bnQiLCJwbGF0Zm9ybSI6IndlYiIsImRldmljZV9pZCI6ImFqdHU2ZnhhLWhhY2stOXQ4ei14enB2LXBoeXA0czdzZTd1OSIsImJyYW5kX2lkIjoxLCJhdWQiOiJjdXN0b21lciIsImlzcyI6ImFjY291bnRzLmJveDguY28uaW4ifQ.Zycdly8bvjNtJGk2UKH-vxcMc8JS11pNhGV9mJff0BgN7lkSgBqWds95-dsrvlQ3fBw3Fzf0nwojxbqra1OBK9ATL5g8f3AI2iEZk0bhI2wNivt1tJ8hLMxWu3wK5TTHtDsoj6MYh85pVXgH00TNYMARUyOQFNuqeMBLpWIqASBe-6CJlSosTqvcu1XMvBr7Ie1nPBL4ZDR3ZIbLAp6HQ-PVxKKrhdEn_lzOk0NqCow2SZZbG7BSn8E16nDTW6YvEi2-HFYdbWgcY-vDiQUhl-nves4RRz9LiAvr6X3ZYed7CteGa4X4LSGlmf5jl1KHM7NwEeoZwbYDVVIaFQc5xPNVKCFvdFhU9rDfO-G_ytz8lbqA3qMnLp56Vcp38eACzKAKVN3my946kGOQiOV80lxuswUIb32ZXAG6GiKbT-REau76CGHwm0wjqWRmNVNhedUPWAo-Mv86-PB4yLVksedNJK5Q5Sgm0VVra_TWNcZkwKqtYIzSM15pLTbOgEeUkRRBQjmyyLw7o_j8BjdYTSo5RjyeTbYG9AjzLz7dfJPVybwuel5cLggtnET4jWzPlm42fJj3aeqcjhsdKMKS3yhvV65zrzGYLsMc4xqsGIW1b2ZBPcFC1z6zWG1tX0ENOQnR2E_gAG6OThbkhIeRf5Y58yBgfFFSZTbT4hfrqwM',
            'content-type': 'application/json',
            'origin': 'https://box8.in',
            'referer': 'https://box8.in/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }
        params5 = {'origin': 'box8', 'platform': 'web'}
        json_data5 = {
            'phone_no': number.replace("+91", ""),
            'name': 'Karatos',
            'email': 'lustion@gmail.com',
            'password': 'karatospy@',
        }
        r5 = requests.post(url5, params=params5, headers=headers5, json=json_data5, timeout=10)
        results.append({"service": "Box8", "status": r5.status_code, "response": r5.text})
        print(f"Box8: {r5.status_code}")
    except Exception as e:
        results.append({"service": "Box8", "status": "Error", "response": str(e)})
        print(f"Box8 Error: {e}")
        
    # --- API 6: LazyPay ---
    try:
        headers6 = {
            'authority': 'api.lazypay.in',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en;q=0.9',
            'content-type': 'application/json',
            'context': 'dashboard',
            'fingerprintid': '3419544578',
            'origin': 'https://lazypay.in',
            'referer': 'https://lazypay.in/',
            'sec-ch-ua': '"Chromium";v"137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'tab-identifier': '1JDHapypRVqPeWaTReSa9Y0o',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }
        json_data6 = {
            'username': number.replace("+91", ""),
        }
        r6 = requests.post('https://api.lazypay.in/api/lazypay/v0/userportal/sendOtp', 
                          headers=headers6, json=json_data6, timeout=10)
        results.append({"service": "LazyPay", "status": r6.status_code, "response": r6.text})
        print(f"LazyPay: {r6.status_code}")
    except Exception as e:
        results.append({"service": "LazyPay", "status": "Error", "response": str(e)})
        print(f"LazyPay Error: {e}")

    return results
