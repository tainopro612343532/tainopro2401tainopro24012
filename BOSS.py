import os
import sys
import subprocess
import random
import string
import requests
import time
import webbrowser
from datetime import datetime
from rich.console import Console
from rich.text import Text
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import dns.resolver
import socket

# Danh sách thư viện cần kiểm tra
libraries = [
    "requests",
    "tabulate",
    "art",
    "colorama",
    "random_user_agent",
    "dnspython",
    "pystyle",
    "rich"
]

# Hàm kiểm tra và cài đặt thư viện
def install_libraries():
    missing_libraries = []
    for lib in libraries:
        try:
            __import__(lib)
        except ImportError:
            missing_libraries.append(lib)

    if missing_libraries:
        print(f"🔧 Đang cài đặt các thư viện: {', '.join(missing_libraries)} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_libraries])
        print("✅ Cài đặt hoàn tất!")
        os.system("cls" if os.name == "nt" else "clear")

# Hàm xóa màn hình
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Kiểm tra và cài đặt các thư viện nếu cần
try:
    import os, random, string, requests, time, webbrowser
    from rich.console import Console
    from datetime import datetime
    from rich.text import Text
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
    import dns.resolver
    import socket
except:
    install_libraries()

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
org_socket = socket.getaddrinfo
os.system('cls' if os.name == 'nt' else 'clear')

def google_socket(host, port, family=0, type=0, proto=0, flags=0):
    try:
        info = resolver.resolve(host)
        ip_address = info[0].to_text()
        return org_socket(ip_address, port, family, type, proto, flags)
    except:
        return org_socket(host, port, family, type, proto, flags)

socket.getaddrinfo = google_socket
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

# Hàm tạo key ngẫu nhiên
def generate_random_key(length=8):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_key(is_admin=False):
    if is_admin:
        return "DCN-ADMIN"
    else:
        return f"DCN-{generate_random_key(6)}"

def save_key_to_file(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("key.txt", "w") as f:
        f.write(f"{key} | {timestamp}\n")

def clean_expired_key():
    if not os.path.exists("key.txt"):
        return
    
    updated_lines = []
    current_time = datetime.now()
    current_date = current_time.date()
    
    with open("key.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                key, timestamp = line.strip().split(" | ")
                key_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()
                if not key.startswith("DCN-ADMIN") and key_date == current_date:
                    updated_lines.append(line)
                elif key.startswith("DCN-ADMIN"):
                    updated_lines.append(line)
            except:
                continue
    
    with open("key.txt", "w") as f:
        f.writelines(updated_lines)

def is_valid_key(key, expected_key):
    clean_expired_key()
    if key == "DCN-ADMIN":
        return True
    elif key == expected_key:
        return True
    return False

def check_stored_key():
    clean_expired_key()
    
    if not os.path.exists("key.txt"):
        return None, None
    
    current_time = datetime.now()
    current_date = current_time.date()
    with open("key.txt", "r") as f:
        for line in f:
            try:
                stored_key, timestamp = line.split(" | ")
                stored_key = stored_key.strip()
                key_time = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()
                if stored_key == "DCN-ADMIN":
                    return stored_key, stored_key
                elif stored_key.startswith("DCN-"):
                    if key_date == current_date:
                        return stored_key, stored_key
            except:
                continue
    return None, None

# Hàm rút gọn link
def get_shortened_link_yeumoney(url):
    token = "937b0d085b9a3ff89dee018458db398cdd36e6c44fb7236267714894315bd895"
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"

    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Lỗi khi kết nối API!"
    except Exception as e:
        return f"Lỗi: {e}"

# Giao diện người dùng
console = Console()

print("")
console.print("[bold red]                                 Tool Đang Chạy...[/bold red]")

# Kiểm tra key và link
try:
    admin_key = "DCN-ADMIN"
    stored_key, user_key = check_stored_key()

    if not stored_key:
        user_key = generate_key(is_admin=False)
        link_can_rut = f"https://hanniee12.github.io/key-war/?key={user_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red]LINK VƯỢT LINK ĐỂ LẤY KEY: {short_link}[/bold red]")

        while True:
            nhap_key = console.input("[bold red]Nhập Key:[/bold red]").strip()

            if is_valid_key(nhap_key, user_key):
                save_key_to_file(nhap_key)
                console.print("[bold green]Key hợp lệ! Đang xác nhận key...[/bold green]")
                time.sleep(3)
                break
            else:
                console.print("[bold red]Key không hợp lệ. Vui lòng vượt link để lấy key![/bold red]")
                time.sleep(2)
    else:
        link_can_rut = f"https://hanniee12.github.io/key-war/?key={stored_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red]LINK VƯỢT LINK ĐỂ LẤY KEY: {short_link}[/bold red]")
        console.print(f"[bold green]Key còn hạn: {stored_key}. Đang xác nhận key...[/bold green]")
        time.sleep(3)

except NameError as e:
    console.print(f"[bold red]Lỗi: Biến hoặc thư viện chưa được định nghĩa - {e}[/bold red]")
except Exception as e:
    console.print(f"[bold red]Lỗi không xác định: {e}[/bold red]")

# Chạy tool chính
while True:
    input_choice = console.input("[bold red]Nhập số lựa chọn: [/bold red]")

    if input_choice == "1":
        url = "https://raw.githubusercontent.com/tainopro612343532/tainopro2401tainopro24012/refs/heads/master/FB_%C4%90A_LU%E1%BB%92NG_LIKE"
        try:
            response = requests.get(url)
            response.raise_for_status()
            exec(response.text)
            console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
            time.sleep(0.5)
            print("                                         ", end="\r")
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Lỗi khi tải URL: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Đã xảy ra lỗi: {e}[/bold red]")

    if input_choice == "2":
        break

    else:
        console.print("[bold red]Vui lòng nhập đúng lựa chọn![/bold red]")

console.print("[bold red]═════════════════════════════════════════════════════════════════════════════════════[/bold red]")
