import requests
from urllib.parse import urlencode

def run_apis3(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 13: Lenskart ---
    try:
        headers13 = {
            'authority': 'api-gateway.juno.lenskart.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.lenskart.com',
            'referer': 'https://www.lenskart.com/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'x-accept-language': 'en',
            'x-api-client': 'mobilesite',
            'x-b3-traceid': '991757133531310',
            'x-country-code': 'IN',
            'x-country-code-override': 'IN',
            'x-session-token': '542cdf49-0851-40fb-af7f-c921e3e261d4',
        }
        json_data13 = {
            'captcha': None,
            'phoneCode': '+91',
            'telephone': number.replace("+91", ""),
        }
        r13 = requests.post('https://api-gateway.juno.lenskart.com/v3/customers/sendOtp', 
                           headers=headers13, json=json_data13, timeout=10)
        results.append({"service": "Lenskart", "status": r13.status_code, "response": r13.text})
        print(f"Lenskart: {r13.status_code}")
    except Exception as e:
        results.append({"service": "Lenskart", "status": "Error", "response": str(e)})
        print(f"Lenskart Error: {e}")

    # --- API 14: Food Stories ---
    try:
        headers14 = {
            'authority': 'www.foodstories.shop',
            'accept': 'text/x-component',
            'accept-language': 'en-IN,en;q=0.9',
            'content-type': 'text/plain;charset=UTF-8',
            'next-action': '4088dec131e19c1a992694ec851e74e3f778b4ffa1',
            'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(pages)%22%2C%7B%22children%22%3A%5B%22shop%22%2C%7B%22children%22%3A%5B%5B%22slug%22%2C%22%22%2C%22oc%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
            'origin': 'https://www.foodstories.shop',
            'referer': 'https://www.foodstories.shop/shop/?' + urlencode({
                'utm_source': 'Google',
                'utm_medium': 'CPC_PMax',
                'utm_campaign': 'PMax_AllProducts_16thSept',
                'gad_source': '1',
                'gad_campaignid': '21328373430',
                'gbraid': '0AAAAA9TONpRbYAGmUf35Q-__ixHBbrftd',
                'gclid': 'EAIaIQobChMIjdP4oOy_jwMVifRMAh2b3hSAEAAYASAAEgJnavD_BwE'
            }),
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }
        
        params14 = {
            'utm_source': 'Google',
            'utm_medium': 'CPC_PMax',
            'utm_campaign': 'PMax_AllProducts_16thSept',
            'gad_source': '1',
            'gad_campaignid': '21328373430',
            'gbraid': '0AAAAA9TONpRbYAGmUf35Q-__ixHBbrftd',
            'gclid': 'EAIaIQobChMIjdP4oOy_jwMVifRMAh2b3hSAEAAYASAAEgJnavD_BwE',
        }
        
        data14 = '[{"mobilenumber":"' + number.replace("+91", "") + '"}]'
        
        r14 = requests.post(
            'https://www.foodstories.shop/shop/',
            params=params14,
            headers=headers14,
            data=data14,
            timeout=10
        )
        results.append({"service": "Food Stories", "status": r14.status_code, "response": r14.text})
        print(f"Food Stories: {r14.status_code}")
    except Exception as e:
        results.append({"service": "Food Stories", "status": "Error", "response": str(e)})
        print(f"Food Stories Error: {e}")

    # --- API 15: Cars24 ---
    try:
        headers15 = {
            'authority': 'pvt-product.cars24.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en;q=0.9',
            'origin': 'https://www.cars24.com',
            'phone_number': number.replace("+91", ""),
            'referer': 'https://www.cars24.com/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'x-api-key': 'qGuMZcWGxZpgd8uSH4rgkal4v1evAlCd',
            'x_country': '',
        }

        r15 = requests.post(
            'https://pvt-product.cars24.com/pp/auth/mobile/otp/send/',
            headers=headers15,
            json={'mobile': number.replace("+91", "")},
            timeout=10
        )
        results.append({"service": "Cars24", "status": r15.status_code, "response": r15.text})
        print(f"Cars24: {r15.status_code}")
    except Exception as e:
        results.append({"service": "Cars24", "status": "Error", "response": str(e)})
        print(f"Cars24 Error: {e}")

    # --- API 16: Anthe ---
    try:
        headers16 = {
            "authority": "anthe.aakash.ac.in",
            "accept": "*/*",
            "accept-language": "en-IN,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://anthe.aakash.ac.in",
            "referer": "https://anthe.aakash.ac.in/anthe",
            "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }

        data16 = {
            "mobileparam": number.replace("+91", ""),
            "global_data_id": "anthe-otp-verify",
            "student_name": "",
            "corpid": ""
        }

        session = requests.Session()
        r16 = session.post('https://anthe.aakash.ac.in/anthe/global-otp-verify', 
                          headers=headers16, data=data16, timeout=10)
        results.append({"service": "Anthe", "status": r16.status_code, "response": r16.text})
        print(f"Anthe: {r16.status_code}")
    except Exception as e:
        results.append({"service": "Anthe", "status": "Error", "response": str(e)})
        print(f"Anthe Error: {e}")

    # --- API 17: Eat Anytime ---
    try:
        headers17 = {
            'authority': 'sotp-api.lucentinnovation.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en;q=0.9',
            'action': 'sendOTP',
            'content-type': 'application/json',
            'origin': 'https://eatanytime.in',
            'referer': 'https://eatanytime.in/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'shop_name': 'eat-anytime.myshopify.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }

        json_data17 = {
            'username': number,
            'type': 'mobile',
            'domain': 'eatanytime.in',
        }

        r17 = requests.post(
            'https://sotp-api.lucentinnovation.com/v6/otp',
            headers=headers17,
            json=json_data17,
            timeout=10
        )
        results.append({"service": "Eat Anytime", "status": r17.status_code, "response": r17.text})
        print(f"Eat Anytime: {r17.status_code}")
    except Exception as e:
        results.append({"service": "Eat Anytime", "status": "Error", "response": str(e)})
        print(f"Eat Anytime Error: {e}")

    # --- API 18: Pantaloons ---
    try:
        headers18 = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlblBheWxvYWQiOnsiZGV2aWNlSWQiOiJlYTFkZDQ3YS00ZGI5LTRhZmMtYTlmZC1mODJhMzA2Y2Q4ZmIifSwiaWF0IjoxNzU3MDEyNjkzfQ.OKeRLCKBP3jAka6N_YOqi5rK2N8s7EzcHpKLycI-tNU',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'origin': 'https://www.pantaloons.com',
            'referer': 'https://www.pantaloons.com/',
            'securekey': 'SuEFE2fooK9DlsIDAvaICJsxEJr1qjRP',
            'source': 'mobile',
        }

        json_data18 = {
            'brand': 'pantaloons',
            'validateHash': False,
            'utmSource': '-1',
            'version': 3.4,
            'geoLocation': {
                'latitude': 343,
            },
            'deviceType': 'mobile',
            'fcmToken': '111',
            'mobile': number.replace("+91", ""),
            'mode': 'verify',
            'cartId': 0,
            'customerId': 0,
            'sliderSource': '-1',
            'cartOperation': 'add',
            'deviceId': 'ea1dd47a-4db9-4afc-a9fd-f82a306cd8fb',
            'deviceToken': 'cef5f364dcdce7fb722187800f0466ee.1757012693',
            'sessionId': 'cef5f364dcdce7fb722187800f0466ee',
            'hash': 'c9e5eafc4163f586b6ecbdabe7d9a284',
        }

        r18 = requests.post(
            'https://apigateway.pantaloons.com/common/sendOTP',
            headers=headers18,
            json=json_data18,
            timeout=10
        )
        results.append({"service": "Pantaloons", "status": r18.status_code, "response": r18.text})
        print(f"Pantaloons: {r18.status_code}")
    except Exception as e:
        results.append({"service": "Pantaloons", "status": "Error", "response": str(e)})
        print(f"Pantaloons Error: {e}")

    return results
