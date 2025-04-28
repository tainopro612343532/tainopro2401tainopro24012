CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

import threading
import time
import os, random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore, Style
from rich.console import Console
from selenium.webdriver.chrome.options import Options
os.system("")
console = Console()
frames = ['|', '/', '-', '\\']  

# Hàm delay chung với tham số cho hành động và thời gian
def delay_action(second, action_text, is_error=False):
    for i in range(second * 10, 0, -1):
        icon = frames[i % len(frames)]  # Chọn icon theo bước
        color = RED if is_error else CYAN if i % 2 == 0 else BLUE
        bracket_color = YELLOW if i % 2 == 0 else MAGENTA
        print(f"{color}{icon} {action_text} {bracket_color}[{i//10}.{i%10}s] {RESET}", end="\r")
        time.sleep(0.1)
    print(" " * 60, end="\r")   
def delay(second):
    delay_action(second, "Đang chạy job")
def delay_laplai(second):
    delay_action(second, "Đang lấy job")
def delay_die(second):
    delay_action(second, "Job die => Đang bỏ qua", is_error=True)
def delay_anti(second):
    delay_action(second, "Đang chạy antiband")
def delay_xoa(second):
    delay_action(second, "Đang Chuẩn Bị Tài Nguyên Vào Tool") 
def delay_kt(second):
    delay_action(second, "Không Thao Tác Trên Luồng Mở Ra") 
# Tạo profile
def tao_profile_moi():
    index = 1
    while True:
        new_profile_path = os.path.join(base_path, f"chrome_profile_{index}")
        if not os.path.exists(new_profile_path):
            break
        index += 1

    print(f"{CYAN}➡️ Đang tạo profile chrome_profile_{index}, vui lòng đăng nhập GoLike{RESET}")
    driver = kt_driver(new_profile_path)
    driver.set_window_size(500, 700)
    delay_kt(2)
    driver.get("https://app.golike.net/login")
    delay_kt(2)
    input("👉 Sau khi đăng nhập xong GoLike, nhấn Enter để tiếp tục...")
    delay_kt(2)
    driver.execute_script("window.open('https://m.facebook.com/login');")
    input("👉 Sau khi đăng nhập xong Facebook, nhấn Enter để tiếp tục...")
    driver.quit()
    print(f"{GREEN}✅ Đã tạo và lưu chrome_profile_{index}{RESET}")
    return new_profile_path 
base_path = os.path.dirname(os.path.abspath(__file__))
profiles = []        
def load_profiles_from_file():
    profiles = []
    if os.path.exists('profiles.txt'):
        with open('profiles.txt', 'r') as file:     
            profiles = [line.strip().split("\\")[-1] for line in file.readlines()]
    return profiles
profiles = load_profiles_from_file()
def save_profiles_to_file(profiles):
    with open('profiles.txt', 'w') as file:
        for profile in profiles:
            file.write(f"{profile}\n")

def kiem_tra_profile(profiles):
    os.system("cls")
    giaodien()
    print("")
    console.print("[bold magenta]                      Welcome to[/bold magenta][bold yellow] the 𝓑𝓞𝓢𝓢 [/bold yellow]")
    console.print("[bold magenta]                 ╚═╦════════════[/bold magenta][bold yellow]══════════╦═╝")
    console.print("[bold magenta]═════════════════════[ Golike Fa[/bold magenta][bold yellow]cebook ]═══════════════════════[/bold yellow]")
    print("")# 18
    console.print("[bold magenta]                  ╔═════════════[/bold magenta][bold yellow]════════════╗       ")
    console.print("[bold magenta]              ╔═══╝ Danh sách cá[/bold magenta][bold yellow]c tài khoản ╚═══╗")
    console.print("[bold magenta]             ╙║                               [/bold magenta][bold yellow]  ║╜ ")
    for idx, profile in enumerate(profiles, start=1):
        console.print(f"            [bold magenta] ╙║  [/bold magenta]    [bold yellow][{idx}][/bold yellow] [bold magenta]{profile}[/bold magenta]       [bold yellow]║╜")
    console.print("[bold magenta]             ╙║                               [/bold magenta][bold yellow]  ║╜ ")
    console.print("[bold magenta]              ╚═════════════════[/bold magenta][bold yellow]════════════════╝       ")
    print("")
    lua_chon = console.input("  [[bold yellow]𝓑𝓞𝓢𝓢[/bold yellow]|[bold magenta]Nhập sô[/bold magenta]][bold green]#   ").strip()
    if lua_chon.lower() == 'x':
        return
    
    try:
        lua_chon = int(lua_chon)
        if 1 <= lua_chon <= len(profiles):
            profile_path = profiles[lua_chon - 1]
            print(f"{CYAN}➡️ Đang kiểm tra tài khoản: {profile_path}{RESET}", end="\r")
            
            driver = kt_driver(profile_path)
            driver.set_window_size(500,700)
            # Kiểm tra GoLike
            driver.get("https://app.golike.net/home")
            delay_kt(2)
            if "golike.net" in driver.current_url:
                print(f"{Fore.GREEN}[✅] Đã đăng nhập GoLike: {profile_path}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[...] Chưa đăng nhập GoLike: {profile_path}{Style.RESET_ALL}")
                input("Vui lòng đăng nhập GoLike rồi bấm Enter...")
            delay_kt(1)
            driver.execute_script("window.open('https://m.facebook.com/login');")
            # Kiểm tra Facebook
            all_windows = driver.window_handles
            driver.switch_to.window(all_windows[1])
            driver.get("https://www.facebook.com/friends")
            delay_kt(2)
            if "facebook.com" in driver.current_url:
                print(f"{Fore.GREEN}[✅] Đã đăng nhập Facebook: {profile_path}{Style.RESET_ALL}")
            else:
                input("Vui lòng đăng nhập Facebook, sau đó bấm Enter...")
            delay_kt(5)
            driver.get("https://www.facebook.com/")
            delay_kt(2)
            driver.find_element(By.XPATH, '//div[@id="screen-root"]/div/div/div[5]/div/div').click()
            delay_kt(5)
            driver.execute_script("window.scrollBy(0, 1000);")
            driver.execute_script("window.scrollBy(0, -1000);")
            driver.execute_script("window.scrollBy(0, 1000);")
            driver.execute_script("window.scrollBy(0, -1000);")
            driver.execute_script("window.scrollBy(0, 1000);")  
            driver.execute_script("window.scrollBy(0, -1000);")
            kt_fb = driver.find_element(By.XPATH, '//div[@id="screen-root"]/div/div[2]/div[13]/div/div[2]/div[4]/div/div/span')
            kt_fb_ten = kt_fb.text.strip()
            print(kt_fb_ten)
            all_windows = driver.window_handles
            driver.switch_to.window(all_windows[0])
            driver.get("https://app.golike.net/jobs/facebook?load_job=false")
            delay_kt(2)
            kt_gl = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/span')
            kt_gl_ten = kt_gl.text.strip()
            delay_kt(2)
            if kt_fb_ten == kt_gl_ten:
                print(f"{Fore.GREEN}[✅] Đã kiểm tra xong {profile_path}! Với acc chạy có tên là {kt_gl_ten}{Style.RESET_ALL}")
            else:
                all_windows = driver.window_handles
                driver.switch_to.window(all_windows[1])
                print(f"{Fore.YELLOW}[...] Hãy chuyển đúng acc Facebook ở trong Golike với tên là {kt_gl_ten}{Style.RESET_ALL}")
                input("Đăng nhập xong bấm Enter...")
            driver.quit()
            print(f"{CYAN}➡️ Đã hoàn thành kiểm tra tài khoản.{RESET}")

        else:
            print(f"{RED}⚠️ Số tài khoản không hợp lệ!{RESET}")
    except ValueError:
        print(f"{RED}⚠️ Vui lòng nhập số hợp lệ!{RESET}")
        
User_Agent=random.choice([
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N910V Build/LRX22C) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/54.0.1548.302 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/53.0.2480.357 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 7 Build/NME91E) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/55.0.1165.180 Mobile Safari/535.4",
"android|Mozilla/5.0 (Android; Android 4.4.4; IQ4502 Quad Build/KOT49H) AppleWebKit/603.22 (KHTML, like Gecko) Chrome/55.0.3246.371 Mobile Safari/535.0",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G925FQ Build/KOT49H) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/49.0.2349.273 Mobile Safari/533.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935S Build/LMY47X) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/51.0.1541.177 Mobile Safari/603.6",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 6 Build/NME91E) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/52.0.3581.331 Mobile Safari/602.0",
"android|Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NME91E) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/47.0.2862.396 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; Android 5.0.1; LG-D725 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko) Chrome/54.0.3919.385 Mobile Safari/601.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/600.8 (KHTML, like Gecko) Chrome/47.0.1683.316 Mobile Safari/534.4",
"android|Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925M Build/LRX22G) AppleWebKit/533.12 (KHTML, like Gecko) Chrome/48.0.3195.222 Mobile Safari/534.1",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; MOTOROLA XT1021 Build/LXB22) AppleWebKit/602.21 (KHTML, like Gecko) Chrome/51.0.3324.323 Mobile Safari/536.2",
"android|Mozilla/5.0 (Linux; Android 4.4; LG-D350 Build/KOT49I) AppleWebKit/601.4 (KHTML, like Gecko) Chrome/50.0.1490.201 Mobile Safari/602.6",
"android|Mozilla/5.0 (Linux; Android 7.0; Xperia Build/NDE63X) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/48.0.3885.393 Mobile Safari/602.7",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 9X Build/NPD90G) AppleWebKit/536.38 (KHTML, like Gecko) Chrome/52.0.2441.242 Mobile Safari/601.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9600 Build/KTU84P) AppleWebKit/602.14 (KHTML, like Gecko) Chrome/53.0.2318.108 Mobile Safari/534.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTO XT1570 MOTO X STYLE Build/LMY47Z) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/55.0.1855.292 Mobile Safari/602.5",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/50.0.1695.312 Mobile Safari/535.3",
"android|Mozilla/5.0 (Android; Android 4.4; MOTOROLA MOTOG Build/KVT49L) AppleWebKit/533.8 (KHTML, like Gecko) Chrome/55.0.3923.147 Mobile Safari/600.9",
"android|Mozilla/5.0 (Linux; U; Android 6.0; HTC One801e dual sim Build/MRA58K) AppleWebKit/536.39 (KHTML, like Gecko) Chrome/47.0.3811.339 Mobile Safari/601.7",
"android|Mozilla/5.0 (Linux; Android 6.0.1; HTC OneS Build/MRA58K) AppleWebKit/600.47 (KHTML, like Gecko) Chrome/51.0.1432.312 Mobile Safari/535.4",
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; LG-H220 Build/KOT49H) AppleWebKit/600.42 (KHTML, like Gecko) Chrome/48.0.2208.322 Mobile Safari/601.2",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 6 Build/NME91E) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/54.0.3774.223 Mobile Safari/600.6",
"android|Mozilla/5.0 (Linux; U; Android 7.0; GT-I9800 Build/KTU84P) AppleWebKit/601.41 (KHTML, like Gecko) Chrome/50.0.1638.368 Mobile Safari/536.0",
"android|Mozilla/5.0 (Linux; Android 6.0; SM-D925S Build/MDB08I) AppleWebKit/533.20 (KHTML, like Gecko) Chrome/47.0.2004.347 Mobile Safari/537.9",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; LG-H900 Build/NRD90C) AppleWebKit/536.25 (KHTML, like Gecko) Chrome/48.0.2443.138 Mobile Safari/601.6",
"android|Mozilla/5.0 (Linux; Android 6.0; HTC One_M8 Build/MRA58K) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/47.0.3998.201 Mobile Safari/603.7",
"android|Mozilla/5.0 (Linux; U; Android 5.0; Nokia 1100 wifi Build/GRK39F) AppleWebKit/533.11 (KHTML, like Gecko) Chrome/54.0.1361.195 Mobile Safari/602.4",
"android|Mozilla/5.0 (Linux; U; Android 4.4.4; SGH-I337 Build/KOT49H) AppleWebKit/536.23 (KHTML, like Gecko) Chrome/51.0.1317.102 Mobile Safari/603.0",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N915G Build/LRX22C) AppleWebKit/533.5 (KHTML, like Gecko) Chrome/50.0.2825.177 Mobile Safari/602.4",
"android|Mozilla/5.0 (Android; Android 5.1; SM-G9350FG Build/LMY47X) AppleWebKit/533.11 (KHTML, like Gecko) Chrome/53.0.2999.116 Mobile Safari/601.3",
"android|Mozilla/5.0 (Android; Android 5.1; SAMSUNG SM-G9350M Build/LMY47X) AppleWebKit/534.37 (KHTML, like Gecko) Chrome/51.0.3632.269 Mobile Safari/533.2",
"android|Mozilla/5.0 (Linux; U; Android 5.1; Nexus 8 Build/LRX22C) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/47.0.3223.257 Mobile Safari/536.7",
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; XT1045 Build/[KXB20.9|KXC21.5]) AppleWebKit/601.38 (KHTML, like Gecko) Chrome/48.0.2780.100 Mobile Safari/535.6",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; Xperia Build/NDE63X) AppleWebKit/601.40 (KHTML, like Gecko) Chrome/48.0.1946.380 Mobile Safari/537.1",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTO X PLAY XT1562 Build/LPC23) AppleWebKit/533.10 (KHTML, like Gecko) Chrome/54.0.3715.270 Mobile Safari/537.6",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTOROLA MOTO E XT1021 Build/LPK23) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/48.0.1929.112 Mobile Safari/603.2",
"android|Mozilla/5.0 (Linux; Android 7.1.1; GT-I9700 Build/KTU84P) AppleWebKit/535.35 (KHTML, like Gecko) Chrome/48.0.3232.317 Mobile Safari/537.8",
"android|Mozilla/5.0 (Linux; Android 5.0.2; LG-D710 Build/LRX22G) AppleWebKit/535.36 (KHTML, like Gecko) Chrome/48.0.1427.177 Mobile Safari/535.9",
"android|Mozilla/5.0 (Android; Android 4.4.4; SAMSUNG SM-T534 Build/KTU84P) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/55.0.1653.292 Mobile Safari/536.3",
"android|Mozilla/5.0 (Android; Android 7.1; SAMSUNG GT-I9700 Build/KTU84P) AppleWebKit/602.46 (KHTML, like Gecko) Chrome/51.0.2298.210 Mobile Safari/603.2",
"android|Mozilla/5.0 (Linux; Android 4.4.4; SM-T534 Build/KOT49H) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/48.0.2865.177 Mobile Safari/601.4",
"android|Mozilla/5.0 (Android; Android 6.0.1; SAMSUNG SM-G925F Build/MMB29K) AppleWebKit/603.6 (KHTML, like Gecko) Chrome/52.0.1707.337 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; Android 6.0; HTC One_M9 Build/MRA58K) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/51.0.1871.148 Mobile Safari/603.9",
"android|Mozilla/5.0 (Linux; Android 6.0.1; SM-D920M Build/MDB08I) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/52.0.1990.397 Mobile Safari/536.9",
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; Nexus5 V7.1 Build/KOT49H) AppleWebKit/602.45 (KHTML, like Gecko) Chrome/55.0.2720.129 Mobile Safari/534.2",
"android|Mozilla/5.0 (Android; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/602.15 (KHTML, like Gecko) Chrome/52.0.2125.398 Mobile Safari/603.2",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SM-G838K Build/LRX22G) AppleWebKit/601.15 (KHTML, like Gecko) Chrome/51.0.3404.311 Mobile Safari/601.3",
"android|Mozilla/5.0 (Linux; U; Android 5.0; SAMSUNG SM-G490 Build/LRX22C) AppleWebKit/536.29 (KHTML, like Gecko) Chrome/48.0.1322.228 Mobile Safari/533.5",
"android|Mozilla/5.0 (Linux; Android 5.1.1; SM-G9350FQ Build/LMY47X) AppleWebKit/602.46 (KHTML, like Gecko) Chrome/55.0.1253.269 Mobile Safari/534.2",
"android|Mozilla/5.0 (Android; Android 7.1.1; Xperia V Build/NDE63X) AppleWebKit/533.20 (KHTML, like Gecko) Chrome/47.0.1025.370 Mobile Safari/602.9",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; SAMSUNG SM-G9358 Build/MMB29M) AppleWebKit/535.4 (KHTML, like Gecko) Chrome/47.0.3983.116 Mobile Safari/535.5",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; Nexus 5 Build/LRX22C) AppleWebKit/600.24 (KHTML, like Gecko) Chrome/53.0.3063.165 Mobile Safari/602.0",
"android|Mozilla/5.0 (Android; Android 6.0.1; SAMSUNG SM-G925F Build/MDB08I) AppleWebKit/536.4 (KHTML, like Gecko) Chrome/50.0.1745.361 Mobile Safari/534.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; SAMSUNG-SM-N910F Build/LRX22C) AppleWebKit/601.39 (KHTML, like Gecko) Chrome/47.0.3525.232 Mobile Safari/536.8",
"android|Mozilla/5.0 (Linux; U; Android 6.0.1; HTC OneS Build/MRA58K) AppleWebKit/600.11 (KHTML, like Gecko) Chrome/48.0.1277.258 Mobile Safari/534.7",
"android|Mozilla/5.0 (Linux; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTET) AppleWebKit/600.12 (KHTML, like Gecko) Chrome/53.0.2390.359 Mobile Safari/537.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/603.49 (KHTML, like Gecko) Chrome/49.0.3944.138 Mobile Safari/533.9",
"android|Mozilla/5.0 (Linux; Android 4.4.4; MOTOROLA MSM8960 Build/KVT49L) AppleWebKit/537.41 (KHTML, like Gecko) Chrome/52.0.3875.248 Mobile Safari/533.5",
"android|Mozilla/5.0 (Android; Android 4.4.1; SM-E500F Build/KTU84P) AppleWebKit/535.49 (KHTML, like Gecko) Chrome/51.0.3420.118 Mobile Safari/533.4",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; Ascend G310 Build/JLS36I) AppleWebKit/536.9 (KHTML, like Gecko) Chrome/51.0.2591.258 Mobile Safari/533.1",
"android|Mozilla/5.0 (Linux; Android 4.4; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/601.29 (KHTML, like Gecko) Chrome/54.0.2437.145 Mobile Safari/600.5",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; Samsung Galaxy S4 Mega GT-I8900 Build/JDQ39) AppleWebKit/603.41 (KHTML, like Gecko) Chrome/53.0.2227.349 Mobile Safari/535.9",
"android|Mozilla/5.0 (Android; Android 7.0; Xperia V Build/NDE63X) AppleWebKit/535.50 (KHTML, like Gecko) Chrome/48.0.1213.228 Mobile Safari/534.9",
"android|Mozilla/5.0 (Android; Android 5.1; SAMSUNG SM-G920T Build/LRX22G) AppleWebKit/600.9 (KHTML, like Gecko) Chrome/55.0.1773.347 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; U; Android 5.0; LG-D325 Build/LRX22G) AppleWebKit/602.12 (KHTML, like Gecko) Chrome/52.0.1615.322 Mobile Safari/603.3",
"android|Mozilla/5.0 (Android; Android 4.4.1; XT1030 Build/[KXB20.9|KXC21.5]) AppleWebKit/602.41 (KHTML, like Gecko) Chrome/54.0.3368.257 Mobile Safari/537.0",
])
def kt_driver(profile_path):
    options = uc.ChromeOptions()
    options.add_argument(f"--user-data-dir={os.path.abspath(profile_path)}")
    #mobile_ua = "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    options.add_argument(f"--user-agent={User_Agent}")
    options.add_argument("--disable-popup-blocking")
    driver = uc.Chrome(options=options , use_subprocess=True)
    return driver
# Hàm tạo driver với profile
def create_driver(profile_path, headless=False):
    
    options = uc.ChromeOptions()
    options.add_argument(f"--user-data-dir={os.path.abspath(profile_path)}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--force-device-scale-factor=0.4")
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    #mobile_ua = "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    #options.add_argument(f"--user-agent={mobile_ua}")
    if headless:
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--log-level=3')  # Chỉ hiện lỗi nghiêm trọng
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')

    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver
tongxu= 0
biendem = 0
dem_loi = 0
#da_dong = False 
def lam_job_facebook_like(driver, index=0):
    global biendem, tongxu, dem_loi
    try:
        driver.get("https://app.golike.net/jobs/facebook?load_job=false")
        driver.execute_script("document.body.style.zoom = '0.50';")
        delay_laplai(5)
        # Kiểm tra xu
        kt = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/span/div[1]/div/div/div/div/div[1]/h6/span/span')
        delay(2)
        text = kt.text.strip()
        delay(1)
        xu = int(text) if text.isdigit() else 35
        delay(3)
        kt.click()
        delay(2)
        # chuyển snag 
        laylink = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a[1]/div[3]/i')
        delay(2)
        laylink.click()
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        handles = driver.window_handles
        if len(handles) > 1:  
            driver.switch_to.window(handles[1])
        delay(20)
        # main
        
        driver.execute_script("window.scrollBy(0, 500);")
        driver.execute_script("window.scrollBy(0, -500);")
        driver.execute_script("window.scrollBy(0, 500);")
        driver.execute_script("window.scrollBy(0, -500);")
        driver.execute_script("window.scrollBy(0, 500);")  
        driver.execute_script("window.scrollBy(0, -500);")
        
        found = False
        try:
            
            try:
                # like
                modal = driver.find_element(By.XPATH, '//div[@role="dialog"]//div[@aria-label="Đóng"]').find_element(By.XPATH, "./ancestor::div[@role='dialog']")
                like = WebDriverWait(modal, 5).until(EC.presence_of_element_located((By.XPATH, './/div[@aria-label="Thích"]')))
            except:
                like = driver.find_element(By.XPATH, '//div[@aria-label="Thích"]')
            try:
                found = True
                delay(3)
                ActionChains(driver).move_to_element(like).perform()
                delay(3)
                ActionChains(driver).move_to_element(like).click().perform()
                delay(3)
            except:
                time.sleep(0.1)
            
                
            if found:
                handles = driver.window_handles
                driver.switch_to.window(handles[1])
                driver.close()
                driver.switch_to.window(handles[0])
                delay(1)
                # hoàn thành job golike
                
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div').click()
                delay(2)
                WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
                ).click()
        # Xu li lai job loi + in ra
                delay_anti(1)
                biendem += 1
                tongxu += xu
                print(f" [Luồng {index}] {CYAN}| {biendem} |  FACEBOOK  | {RED} Ẩn ID {RESET} |{GREEN} Hoàn Thành {RESET}| {YELLOW}+{xu}{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} | ")
                
                #print(f"{CYAN}{NGHIENG}[ FACEBOOK ] {RESET} | {RED} Ẩn ID {RESET} |{GREEN} Hoàn Thành {RESET}| {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} | ")
        except:
            delay_die(1)
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

            all_windows = driver.window_handles
            driver.switch_to.window(all_windows[1])
            driver.close()
            driver.switch_to.window(all_windows[0])
            delay_die(1)
                            
            element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[1]')
            delay_die(1)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            delay_die(1)
            element.click()
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/button').click()
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
            ).click()
            print(f"{RED}[Luồng {index}] Bỏ qua job thành công{RESET}", end="\r")
            #print(""*20, end="\r")
    except:
        # Thêm xem lỗi và tự đóng luồng
        dem_loi += 1
        delay_die(1)
        print(f"{RED}[Luồng {index}] Lỗi luồng {RESET}", end="\r")
        #print(f"{RED}[Luồng {index}] Lỗi luồng ({dem_loi}/20) => Đạt 20 lỗi sẽ tự động dừng  {RESET}", end="\r")
        #if dem_loi >= 20 :
        #    print(f"\n{RED}[Luồng {index}] Quá 20 lỗi => Đã đóng{RESET}")
        #    driver.quit()
        #    return
        #else:
        #    delay_laplai(1)
            
        #print(""*20, end="\r")
        
# Hàm làm nhiệm vụ Facebook Like cho mỗi profile
def lam_job(profile_path, index=0):
    driver = create_driver(profile_path, headless=False)
    driver.set_window_size(500, 700)
    driver.set_window_position(x=550 * index, y=0 )
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        delay_laplai(1)
        lam_job_facebook_like(driver, index)
# Hàm chạy đa luồng với delay giữa các luồng
def chay_da_luong(profile_paths, delay=5):
    threads = []
    for index, profile_path in enumerate(profile_paths):
        time.sleep(delay * index)
        t = threading.Thread(target=lam_job, args=(profile_path, index))
        t.daemon = True 
        print(f"Đang mở: {profile_path} [Luồng {index}] ")
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
def tat_chrome_hieu_ung():
    os.system('taskkill /f /im chrome.exe >nul 2>&1')
def giaodien():
    console.print("[bold magenta]                      Welcome to[/bold magenta][bold yellow] the 𝓑𝓞𝓢𝓢[/bold yellow]")
    console.print("[bold magenta]                 ╚═╦════════════[/bold magenta][bold yellow]══════════╦═╝")
    console.print("[bold magenta]═════════════════════[ Golike Fa[/bold magenta][bold yellow]cebook ]═══════════════════════[/bold yellow]")
 #Menu UI
def ui():
    while True:
        tat_chrome_hieu_ung()
        delay_xoa(15)
        os.system('cls')
        giaodien()
        print("")
        console.print("[bold magenta][[bold yellow]1[/bold yellow]]  Thêm tài khoản[/bold magenta]")
        console.print("[bold magenta][[bold yellow]2[/bold yellow]]  Kiểm tra đăng nhập[/bold magenta]")
        console.print("[bold magenta][[bold yellow]3[/bold yellow]]  Làm nhiệm vụ (đồng thời)[/bold magenta]")
        console.print("[bold magenta][[bold yellow]X[/bold yellow]]  Thoát[/bold magenta]")
        print("")
        lua_chon = console.input("  [[bold yellow]𝓑𝓞𝓢𝓢[/bold yellow]|[bold magenta]Nhập sô[/bold magenta]][bold green]#   ")
        profiles = load_profiles_from_file()  # Đọc lại danh sách profile từ file

        if lua_chon == "1":
            profile_path = tao_profile_moi()
            if profile_path not in profiles:
                profiles.append(profile_path)
                save_profiles_to_file(profiles)  # Lưu lại danh sách profile vào file
        elif lua_chon == "2":
            kiem_tra_profile(profiles)

        elif lua_chon == "3":
            
            try:
        
                chay_da_luong(profiles)
            except Exception as e:
                print(e)
                break
        elif lua_chon.lower() == "x":
            break
# Thực thi chương trình với 3 profile
if __name__ == "__main__":
    ui()







