import requests

def run_apis10(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 51: Additional Swiggy API ---
    try:
        headers51 = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'profile.swiggy.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data51 = {
            'mobile': number.replace("+91", "")
        }

        r51 = requests.post(
            'https://profile.swiggy.com/api/v3/app/request_call_verification',
            headers=headers51,
            json=json_data51,
            timeout=10
        )
        results.append({"service": "Swiggy Final", "status": r51.status_code, "response": r51.text})
        print(f"Swiggy Final: {r51.status_code}")
    except Exception as e:
        results.append({"service": "Swiggy Final", "status": "Error", "response": str(e)})
        print(f"Swiggy Final Error: {e}")

    # --- API 52: Additional Proptiger API ---
    try:
        headers52 = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'www.proptiger.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data52 = {
            'contactNumber': number.replace("+91", ""),
            'domainId': '2'
        }

        r52 = requests.post(
            'https://www.proptiger.com/madrox/app/v2/entity/login-with-number-on-call',
            headers=headers52,
            json=json_data52,
            timeout=10
        )
        results.append({"service": "Proptiger Final", "status": r52.status_code, "response": r52.text})
        print(f"Proptiger Final: {r52.status_code}")
    except Exception as e:
        results.append({"service": "Proptiger Final", "status": "Error", "response": str(e)})
        print(f"Proptiger Final Error: {e}")

    return results
