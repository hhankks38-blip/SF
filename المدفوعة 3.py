

import requests
import random
import time
import os
import sys

# ==================== ألوان متناسقة ====================
# أحمر
R1 = '\x1b[1;38;5;196m'  # أحمر فاتح
R2 = '\x1b[1;38;5;160m'  # أحمر غامق

# بنفسجي
P1 = '\x1b[1;38;5;165m'  # بنفسجي فاتح
P2 = '\x1b[1;38;5;129m'  # بنفسجي غامق
P3 = '\x1b[1;38;5;93m'   # بنفسجي متوسط

# سماوي
C1 = '\x1b[1;38;5;51m'   # سماوي فاتح
C2 = '\x1b[1;38;5;45m'   # سماوي غامق
C3 = '\x1b[1;38;5;39m'   # أزرق سماوي

# وردي
PK1 = '\x1b[1;38;5;205m' # وردي فاتح
PK2 = '\x1b[1;38;5;200m' # وردي غامق
PK3 = '\x1b[1;38;5;198m' # وردي أحمر

# ألوان أساسية
G1 = '\x1b[1;38;5;46m'   # أخضر
G2 = '\x1b[1;38;5;82m'   # أخضر فاتح
Y1 = '\x1b[1;38;5;226m'  # أصفر
Y2 = '\x1b[1;38;5;220m'  # أصفر ذهبي
B1 = '\x1b[1;38;5;21m'   # أزرق
B2 = '\x1b[1;38;5;27m'   # أزرق كهربائي
W1 = '\x1b[1;38;5;255m'  # أبيض
W2 = '\x1b[1;38;5;231m'  # أبيض ناصع
N = '\x1b[0m'             # إعادة تعيين
BOLD = '\x1b[1m'

# ==================== شعار  ====================
LOGO_SF = f"""
{C1}╔══════════════════════════════════════════════════════╗
{C1}║{PK1}SF{C1}╗ {PK1}SF{C1}║{P2}          {C1}╔══════════════════╗{C1}║
{C1}║{PK1}SF{C1}╔══{PK1}SF{C1}╗{PK1}sf{C1}╔════╝{P2}          {C1}║{P2}    SF    {C1}║{C1}║
{C1}║{PK1}SF{C1}╔╝{PK1}SF{C1}╗{P2}          {C1}║{P2}  @SF7SF0  {C1}║{C1}║
{C1}║{PK1}SF{C1}╔═══╝ ╚════{PK1}SF{C1}║{P2}          {C1}╚══════════════════╝{C1}║
{C1}║{PK1}SF{C1}║     {PK1}SF{C1}║{P2}  ╔══════════════════════╗{C1}║
{C1}║{PK1}╚═╝     ╚══════{PK1}╝{C1}║{P2}  ║{PK1}https://t.me/DEW_Pess{P2}║{C1}║
{C1}╚═══════════════SF═════════╝{P2}  ╚══════════════════════╝{C1}║
{C1}═══════════════════════════════════════════════════════╝{N}"""

# ==================== قوائم عشوائية ====================
arabic_names = [
    "محمد", "احمد", "علي", "حسين", "عباس", "جواد", "حسن", "مهدي", 
    "رضا", "كرار", "حيدر", "مرتضى", "مصطفى", "محمود", "عبدالله", 
    "ياسر", "عمر", "عثمان", "زينب", "فاطمة", "رقية", "نور", "زهراء",
    "اسراء", "مريم", "سارة", "هدى", "ايمان", "بتول", "كوثر", "حوراء",
    "زكي", "سجاد", "مجتبى", "أمير", "وسام", "علاء", "مهند", "حسام"
]

arabic_lastnames = [
    "العراقي", "البغدادي", "النجفي", "الكربلائي", "البصري", "الموصلي",
    "الكاظمي", "الحلي", "السامرائي", "الفلوجي", "الرمادي", "الكوفي",
    "الزيدي", "الحسني", "الحسيني", "الموسوي", "الصدر", "الحكيم",
    "الشمري", "التميمي", "الأسدي", "الكناني", "الخزرجي", "الازدي",
    "الجبوري", "العامري", "الخفاجي", "الخاقاني", "الطائي", "الربيعي"
]

repeated_numbers = [
    "19801980", "19901990", "20002000", "20102010", "20202020",
    "12341234", "43214321", "11111111", "22222222", "33333333",
    "12qwqw21", "5sdsd678", "66666666", "77777777", "lplp6969",
    "eeee0000", "12121212", "13131313", "14141414", "15151515",
    "12345678", "87654321", "11223344", "55667788", "99887766",
    "19701970", "19851985", "19951995", "20052005", "20152015"
]

# قائمة الأرقام المطلوبة للإرسال
SEND_NUMBERS = [5,7,10,13]

def clear():
    """مسح الشاشة"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """طباعة الشعار"""
    clear()
    print(LOGO_SF)
    print(f"{C1}{BOLD}{'='*60}{N}")
    print(f"{PK1}{BOLD}{' ' * 18} صيد حسابات فيسبوك {N}")
    print(f"{C1}{BOLD}{'='*60}{N}")
    print(f"{P2}{BOLD}المطور:{N} {PK1}{BOLD}SF{N} {P2}{BOLD}|{N} {C1}{BOLD}يوزر:{N} {PK1}{BOLD}@SF7SF0{N} {P2}{BOLD}|{N} {C1}{BOLD}قناة:{N} {PK1}{BOLD}https://t.me/DEW_Pess{N}")
    print(f"{C1}{BOLD}{'='*60}{N}\n")

def parse_account_line(line):
    """تحليل سطر الملف واستخراج الايدي والاسم"""
    line = line.strip()
    if '|' in line:
        parts = line.split('|', 1)
        if len(parts) == 2:
            return parts[0].strip(), parts[1].strip()
    return line.strip(), ""

def main():
    """الدالة الرئيسية"""
    print_banner()
    
    # طلب معلومات البوت والملف
    print(f"{C1}{BOLD}{'─'*60}{N}")
    bot_token = input(f"{PK1}{BOLD}[?]{N} {C1}{BOLD}أدخل توكن البوت: {P2}{BOLD}")
    chat_id = input(f"{PK1}{BOLD}[?]{N} {C1}{BOLD}أدخل ايدي حسابك: {P2}{BOLD}")
    file_path = input(f"{PK1}{BOLD}[?]{N} {C1}{BOLD}أدخل مسار الملف: {P2}{BOLD}")
    print(f"{C1}{BOLD}{'─'*60}{N}\n")
    
    # التحقق من وجود الملف
    if not os.path.exists(file_path):
        print(f"{R1}{BOLD}[✗] الملف غير موجود!{N}")
        time.sleep(2)
        return
    
    # قراءة الايديات من الملف
    accounts = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            account_id, account_name = parse_account_line(line)
            if account_id:
                accounts.append((account_id, account_name))
    
    if not accounts:
        print(f"{R1}{BOLD}[✗] لا توجد ايديات في الملف!{N}")
        time.sleep(2)
        return
    
    total_ids = len(accounts)
    print(f"{G1}{BOLD}[✓] تم تحميل {P2}{BOLD}{total_ids}{C1}{BOLD} ايدي{N}")
    print(f"{G1}{BOLD}[✓] بوت: {P2}{BOLD}{bot_token[:10]}...{N}")
    print(f"{G1}{BOLD}[✓] ايديك: {P2}{BOLD}{chat_id}{N}")
    print(f"{C1}{BOLD}{'─'*60}{N}\n")
    time.sleep(2)
    
    # متغيرات للتتبع
    send_counter = 0
    accounts_sent = []
    send_targets = SEND_NUMBERS.copy()
    
    print(f"\n{PK1}{BOLD}بدء الفحص...{N}\n")
    
    # الفحص لكل ايدي في الملف
    for fhso_number, (account_id, account_name) in enumerate(accounts, 1):
        # حساب النسبة المئوية
        percent = (fhso_number / total_ids) * 100
        
        # أرقام عشوائية للحالة
        secure_num = random.randint(0, 999)
        correct_num = random.randint(0, 99)
        
        # إنشاء باسورد عشوائي
        password_type = random.choice(['name', 'number'])
        
        if password_type == 'name':
            name = random.choice(arabic_names)
            lastname = random.choice(arabic_lastnames)
            password = f"{name} {lastname}"
        else:
            password = random.choice(repeated_numbers)
        
        # ==================== السطر المعدل ====================
        # سطر فحص واحد يحتوي على: النسبة المئوية | العدد الكلي | المرسل | اسم المطور
        sys.stdout.write('\033[K')  # مسح السطر الحالي
        print(f"\r{C1}{BOLD}[{percent:.1f}%] {P2}{BOLD}{fhso_number}/{total_ids} {PK1}{BOLD}| {G1}{BOLD} 𝑲𝑶 : {send_counter} {PK1}{BOLD}| {P2}{BOLD}SF{N}", end='', flush=True)
        # =====================================================
        
        # انتظار ثانية (محاكاة الفحص)
        time.sleep(1)
        
        # التحقق إذا وصلنا لعدد الفحوصات المطلوب للإرسال
        if fhso_number in send_targets:
            send_counter += 1
            
            # اختيار حساب عشوائي لم يتم إرساله من قبل
            if accounts_sent:
                remaining = [acc for acc in accounts if acc not in accounts_sent]
                if remaining:
                    send_acc = random.choice(remaining)
                else:
                    send_acc = random.choice(accounts)
            else:
                send_acc = random.choice(accounts)
            
            accounts_sent.append(send_acc)
            send_id, send_name = send_acc
            
            # تنسيق رسالة التليجرام - بدون كوكيز
            message = f"""
اجاك حساب فيس بوك 
━━━━━━━━⚚❲ SF ⛧ @SF7SF0 ❳⚚━━━━━━━━━━━━━━
  𝑵𝑨𝑴𝑬 : {send_name}
 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {send_id}
 - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {password}
 𝒕𝒉𝒆 𝒂𝒄𝒄𝒐𝒖𝒏𝒕 : htsf://www.facebook.com/{send_id}
━━━━━━━━⚚❲ SF ⛧ @SF7SF0 ❳⚚━━━━━━━━━━━━━━
لاتنساء صور الصيد  
"""
            
            # إرسال إلى التليجرام
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            params = {
                'chat_id': chat_id,
                'text': message
            }
            
            try:
                response = requests.post(url, params=params)
                if response.status_code == 200:
                    # طباعة تأكيد الإرسال في سطر جديد
                    print(f"\n{G1}{BOLD}[✓] تم الإرسال #{send_counter}{N}")
                    print(f"{C1}{BOLD}[i] عداد الفحص: {P2}{BOLD}{fhso_number}{N}")
                    print(f"{C1}{BOLD}[i] إجمالي الايديات: {P2}{BOLD}{total_ids}{N}")
                    print(f"{PK1}{BOLD}{'─'*60}{N}\n")
                else:
                    print(f"\n{R1}{BOLD}[✗] فشل الإرسال: {response.status_code}{N}\n")
            except Exception as e:
                print(f"\n{R1}{BOLD}[✗] خطأ في الإرسال: {e}{N}\n")
            
            # إزالة هذا الرقم من قائمة الأهداف
            if fhso_number in send_targets:
                send_targets.remove(fhso_number)
    
    # سطر جديد بعد انتهاء الحلقة
    print()
    
    # النتيجة النهائية
    print(f"\n{G1}{BOLD}{'='*60}{N}")
    print(f"{G1}{BOLD}[✓] تم الانتهاء من الصيد!{N}")
    print(f"{G1}{BOLD}[✓] إجمالي الأيدييات: {P2}{BOLD}{total_ids}{N}")
    print(f"{G1}{BOLD}[✓] عدد الإرساليات للبوت: {P2}{BOLD}{send_counter}{N}")
    print(f"{G1}{BOLD}{'='*60}{N}")
    
    input(f"\n{PK1}{BOLD}[i] اضغط Enter للعودة...{N}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R1}{BOLD}[!] تم إيقاف الأداة{N}")
        print(f"{PK1}{BOLD}[i] @SF7SF0 | {P2}{BOLD}SF{N}")
        time.sleep(2)
        clear()
        sys.exit(0)