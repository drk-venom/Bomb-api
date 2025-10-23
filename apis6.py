import requests

def run_apis6(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 31: GoPink Cabs ---
    try:
        headers31 = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.gopinkcabs.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.gopinkcabs.com/app/cab/customer/step1.php',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data31 = {
            'check_mobile_number': '1',
            'contact': number.replace("+91", ""),
        }

        response = requests.post('https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php', headers=headers31, data=data31, timeout=10)
        results.append({"service": "GoPink Cabs", "status": response.status_code, "response": response.text})
        print(f"GoPink Cabs: {response.status_code}")
    except Exception as e:
        results.append({"service": "GoPink Cabs", "status": "Error", "response": str(e)})
        print(f"GoPink Cabs Error: {e}")

    # --- API 32: CaratLane ---
    try:
        headers32 = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'e57868edb066b4e04cbf0de4679acc3d3739d1ec0479fdccec2a5c6ff0b919',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'cookieenabled': 'true',
            'cs-request': 'true',
            'ib': 'false',
            'origin': 'https://www.caratlane.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.caratlane.com/register',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'setsamesite': 'true',
            'uniqid': 'eexbsimfvbi09c-1758557144321',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-amzn-trace-id': 'uniqid=eexbsimfvbi09c-1758557144321',
            'x-authorization': 'e57868edb066b4e04cbf0de4679acc3d3739d1ec0479fdccec2a5c6ff0b919',
        }

        json_data32 = {
            'query': 'mutation SendOtp($mobile:String, $isdCode:String, $otpType:String, $email:String){\n  SendOtp(input:{mobile:$mobile, isdCode:$isdCode, otpType:$otpType, email:$email}){\n          status{\n              message\n              code\n          }\n      }\n  }\n',
            'variables': {
                'mobile': number.replace("+91", ""),
                'isdCode': '91',
                'otpType': 'registerOtp',
            },
        }

        response = requests.post('https://www.caratlane.com/cg/dhevudu', headers=headers32, json=json_data32, timeout=10)
        results.append({"service": "CaratLane", "status": response.status_code, "response": response.text})
        print(f"CaratLane: {response.status_code}")
    except Exception as e:
        results.append({"service": "CaratLane", "status": "Error", "response": str(e)})
        print(f"CaratLane Error: {e}")

    # --- API 33: Shemaroome ---
    try:
        headers33 = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.shemaroome.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.shemaroome.com/users/sign_in',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data33 = {
            'mobile_no': f'+91{number.replace("+91", "")}',
            'registration_source': 'organic',
        }

        response = requests.post('https://www.shemaroome.com/users/mobile_no_signup', headers=headers33, data=data33, timeout=10)
        results.append({"service": "Shemaroome", "status": response.status_code, "response": response.text})
        print(f"Shemaroome: {response.status_code}")
    except Exception as e:
        results.append({"service": "Shemaroome", "status": "Error", "response": str(e)})
        print(f"Shemaroome Error: {e}")

    # --- API 34: MyBharat ---
    try:
        headers34 = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://mybharat.gov.in',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://mybharat.gov.in/yuva_register',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data34 = {
            'user_phone': number.replace("+91", ""),
        }

        response = requests.post('https://mybharat.gov.in/pages/sendGuestUserOtp', headers=headers34, data=data34, timeout=10)
        results.append({"service": "MyBharat", "status": response.status_code, "response": response.text})
        print(f"MyBharat: {response.status_code}")
    except Exception as e:
        results.append({"service": "MyBharat", "status": "Error", "response": str(e)})
        print(f"MyBharat Error: {e}")

    # --- API 35: Lenskart ---
    try:
        headers35 = {
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.lenskart.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.lenskart.com/',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-accept-language': 'en',
            'x-api-client': 'desktop',
            'x-b3-traceid': '991758558728627',
            'x-country-code': 'IN',
            'x-country-code-override': 'IN',
            'x-session-token': '441def2c-7f4c-407d-ba7a-f97b5d078bec',
        }

        json_data35 = {
            'captcha': None,
            'phoneCode': '+91',
            'telephone': number.replace("+91", ""),
        }

        response = requests.post('https://api-gateway.juno.lenskart.com/v3/customers/sendOtp', headers=headers35, json=json_data35, timeout=10)
        results.append({"service": "Lenskart", "status": response.status_code, "response": response.text})
        print(f"Lenskart: {response.status_code}")
    except Exception as e:
        results.append({"service": "Lenskart", "status": "Error", "response": str(e)})
        print(f"Lenskart Error: {e}")

    # --- API 36: Smytten ---
    try:
        headers36 = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://smytten.com',
            'Pragma': 'no-cache',
            'Referer': 'https://smytten.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'desktop_request': 'true',
            'request_type': 'web',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'uuid': 'cf98ed0b-366e-46db-91e6-ebb9a024c602',
            'web_version': '1',
        }

        json_data36 = {"ad_id":"","device_info":{},"device_id":"","app_version":"","device_token":"","device_platform":"web","phone": number.replace("+91", ""),"email":"sdhabai09@gmail.com"}

        response = requests.post('https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode', headers=headers36, json=json_data36, timeout=10)
        results.append({"service": "Smytten", "status": response.status_code, "response": response.text})
        print(f"Smytten: {response.status_code}")
    except Exception as e:
        results.append({"service": "Smytten", "status": "Error", "response": str(e)})
        print(f"Smytten Error: {e}")

    return results
