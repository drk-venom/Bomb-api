import requests

def run_apis7(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 37: Rappi ---
    try:
        headers37 = {
            'accept': 'application/json',
            'accept-language': 'es-MX',
            'access-control-allow-headers': '*',
            'access-control-allow-origin': '*',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'deviceid': '7174450b-b912-404d-8e72-f95512e404d0',
            'needappsflyerid': 'false',
            'origin': 'https://www.rappi.com.mx',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.rappi.com.mx/',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        }

        json_data37 = {
            'country_code': '+91',
            'phone': number.replace("+91", ""),
        }

        response = requests.post(
            'https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create',
            headers=headers37,
            json=json_data37,
            timeout=10
        )
        results.append({"service": "Rappi", "status": response.status_code, "response": response.text})
        print(f"Rappi: {response.status_code}")
    except Exception as e:
        results.append({"service": "Rappi", "status": "Error", "response": str(e)})
        print(f"Rappi Error: {e}")

    # --- API 38: Univest ---
    try:
        headers38 = {
            'Host': 'api.univest.in',
            'user-agent': 'okhttp/3.9.1',
            'x-forwarded-for': '12.241.103.59',
            'client-ip': '12.241.103.59',
        }

        params38 = {
            'type': 'web4',
            'countryCode': '91',
            'contactNumber': number.replace("+91", ""),
        }

        response = requests.get('https://api.univest.in/api/auth/send-otp', params=params38, headers=headers38, timeout=10)
        results.append({"service": "Univest", "status": response.status_code, "response": response.text})
        print(f"Univest: {response.status_code}")
    except Exception as e:
        results.append({"service": "Univest", "status": "Error", "response": str(e)})
        print(f"Univest Error: {e}")

    # --- API 39: Jockey ---
    try:
        headers39 = {
            'Host': 'www.jockey.in',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
            'accept': '*/*',
            'referer': 'https://www.jockey.in/',
            'accept-language': 'en-US,en;q=0.9,bn;q=0.8,hi;q=0.7,zh-CN;q=0.6,zh;q=0.5',
            'x-forwarded-for': '12.241.103.59',
            'client-ip': '12.241.103.59',
        }

        params39 = {
            'whatsapp': 'false',
        }

        response = requests.get(f'https://www.jockey.in/apps/jotp/api/login/send-otp/+91{number.replace("+91", "")}', params=params39, headers=headers39, timeout=10)
        results.append({"service": "Jockey", "status": response.status_code, "response": response.text})
        print(f"Jockey: {response.status_code}")
    except Exception as e:
        results.append({"service": "Jockey", "status": "Error", "response": str(e)})
        print(f"Jockey Error: {e}")

    # --- API 40: GetSwipe ---
    try:
        headers40 = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'devicehash': '70815629-21a0-457f-b321-6263437fda85',
            'origin': 'https://app.getswipe.in',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://app.getswipe.in/auth/login?country_code=IN',
            'request-timestamp': 'Mon, 22 Sep 2025 17:49:04 GMT',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sentry-trace': '30c7279a645a4a9abf89b783e6107bb8-ae639886aac5d499-1',
            'source': 'web',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'web_version': 'v1.15.4',
            'x-request-id': 'web-7b6662a6-b19b-4b9b-9d2c-30126277371a',
        }

        json_data40 = {
            'mobile': number.replace("+91", ""),
            'otp': '',
            'params': '',
            'email': '',
            'country_code': 'IN',
        }

        response = requests.post('https://app.getswipe.in/api/user/app_login', headers=headers40, json=json_data40, timeout=10)
        results.append({"service": "GetSwipe", "status": response.status_code, "response": response.text})
        print(f"GetSwipe: {response.status_code}")
    except Exception as e:
        results.append({"service": "GetSwipe", "status": "Error", "response": str(e)})
        print(f"GetSwipe Error: {e}")

    # --- API 41: NuvamaWealth ---
    try:
        headers41 = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'api-key': 'c41121ed-b6fb-c9a6-bc9b-574c82929e7e',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://onboarding.nuvamawealth.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://onboarding.nuvamawealth.com/',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        }

        json_data41 = {
            'contactInfo': number.replace("+91", ""),
            'mode': 'SMS',
        }

        response = requests.post('https://nwaop.nuvamawealth.com/mwapi/api/Lead/GO', headers=headers41, json=json_data41, timeout=10)
        results.append({"service": "NuvamaWealth", "status": response.status_code, "response": response.text})
        print(f"NuvamaWealth: {response.status_code}")
    except Exception as e:
        results.append({"service": "NuvamaWealth", "status": "Error", "response": str(e)})
        print(f"NuvamaWealth Error: {e}")

    # --- API 42: Shopsy ---
    try:
        headers42 = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.shopsy.in',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.shopsy.in/login?ret=%2F',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-full-version': '"140.0.7339.129"',
            'sec-ch-ua-full-version-list': '"Chromium";v="140.0.7339.129", "Not=A?Brand";v="24.0.0.0", "Google Chrome";v="140.0.7339.129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-partner-context': '{"source":"reseller"}',
            'x-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 FKUA/msite/0.0.4/msite/Mobile',
        }

        json_data42 = {
            'actionRequestContext': {
                'loginIdPrefix': '+91',
                'loginId': number.replace("+91", ""),
                'clientQueryParamMap': {
                    'ret': '/',
                    'entryPage': 'HEADER_ACCOUNT',
                },
                'loginType': 'MOBILE',
                'verificationType': 'OTP',
                'screenName': 'LOGIN_V4_MOBILE',
                'sourceContext': 'DEFAULT',
                'type': 'LOGIN_IDENTITY_VERIFY',
            },
        }

        response = requests.post('https://www.shopsy.in/2.rome/api/1/action/view',headers=headers42, json=json_data42, timeout=10)
        results.append({"service": "Shopsy", "status": response.status_code, "response": response.text})
        print(f"Shopsy: {response.status_code}")
    except Exception as e:
        results.append({"service": "Shopsy", "status": "Error", "response": str(e)})
        print(f"Shopsy Error: {e}")

    return results
