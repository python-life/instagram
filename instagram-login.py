import requests,json
import requests
us = input('ENTER YOUR USERNAME :')
pw = input('ENTER YOUR PASSWORD  :')
login = {
'accept': "*/*",
'accept-encoding': "gzip, deflate, br",
'accept-language': "en-DZ,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5,en-US;q=0.4",
'content-length':"339",
'content-type': "application/x-www-form-urlencoded",
'cookie': 'ig_nrcb=1; ig_did=A577F8CC-7FEF-4958-824F-CA1D5A2C998D; mid=X_I7LgAEAAHqNbPdG_-pVVFVb02A; fbm_124024574287414=base_domain=.instagram.com; shbid=10062; shbts=1610112305.0874965; rur=FRC; csrftoken=wdPwS0TP6Ww01W1EESEST1mwOqJnp5qE; urlgen="{\"105.235.136.51\": 33779\054 \"105.235.134.59\": 33779}:1kxxf4:jx8gQYfyTYSt5lVD5owmMFcqcQA"',
'origin': "https://www.instagram.com",
'referer': "https://www.instagram.com/accounts/login/",
'sec-fetch-dest': "empty",
'sec-fetch-mode':"cors",
'sec-fetch-site':"same-origin",
'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)',
'x-csrftoken': "wdPwS0TP6Ww01W1EESEST1mwOqJnp5qE",
'x-ig-app-id': "936619743392459",
'x-ig-www-claim': "hmac.AR0-KMDK3oo27FfpKawBoo73vi3Y-GHZV8aupjUbzaEpQm6x",
'x-instagram-ajax': "818fed40bc2e",
'x-requested-with': "XMLHttpRequest"
}
loginurl='https://www.instagram.com/accounts/login/ajax/'
data = {
    'username':us,
    'enc_password':'#PWD_INSTAGRAM_BROWSER:0:&:'+pw
}
 r = requests.post(url, data=data, headers=login).text
    if 'userId' in r :
        print('welcome ',us)
        break
    elif  "false" in r:
        print('worng password !')
    else:
        if 'message' in r :
            print('Please wait a few minutes before you try again')
