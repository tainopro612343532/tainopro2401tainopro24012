import os
import sys
import subprocess
import dns
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
        

# Chạy kiểm tra và cài đặt nếu cần
try:
    import os, random, string, requests, time, webbrowser
    from rich.console import Console
    from datetime import datetime, timedelta
    from rich.text import Text
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
    import dns.resolver
    import socket
except:
    install_libraries()
os.system("")
# Hàm xóa màn hình
def clear():
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình tùy theo hệ điều hành
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
clear()
console = Console()
text = Text("MENU", style="bold")
colors = ["red", "orange", "yellow", "green"]  # Không có màu trắng

for i, char in enumerate(text.plain):
    text.stylize(colors[i % len(colors)], i, i + 1)





# Hiển thị banner
from rich.console import Console

console = Console()

print("")
console.print("[bold red]                                                                                       [/bold red]")
console.print("[bold red]                                _          _                  ___ _____                 [/bold red]")      
console.print("[bold magenta]                               / \\   _ __ (_)_ __ ___   ___  |_ _|_   _|              [/bold magenta]") 
console.print("[bold red]                              / _ \\ | '_ \\| | '_ ` _ \\ / _ \\  | |  | |                  [/bold red]")   
console.print("[bold magenta]                             / ___ \\| | | | | | | | | |  __/  | |  | |               [/bold magenta]")  
console.print("[bold red]                            /_/   \\_\\_| |_|_|_| |_| |_|\\___| |___| |_|               [/bold red]")  
console.print("[bold magenta]                      ╚════╦════════════════════════════════════╦════╝          [/bold magenta]")
console.print("[bold magenta]                           ║[/bold magenta][bold yellow]                                      ║[/bold yellow]")
console.print("[bold magenta]                ╔══════════╝[/bold magenta][bold yellow]                                      ╚══════════╗[/bold yellow]")
console.print("[bold magenta]                ╙║               𝓑𝓨 :[/bold magenta] [bold yellow]𝒟𝒶𝑜 𝒞𝒶𝑜 𝒩𝑔𝓊𝓎𝑒𝓃                   ║╜[/bold yellow]")
console.print("[bold magenta]                 ╙║                                        [/bold magenta][bold yellow]║╜[/bold yellow]")
console.print(f"[bold magenta]     ╔════════════╩═════════════════════[ [/bold magenta]", end="")
console.print("[bold cyan]TEXT Ở ĐÂY[/bold cyan]", end="")  # bạn cần thay biến `text` vào đây
console.print("[bold yellow] ]═══════════════════╩═══════════╗[/bold yellow]")
console.print("[bold magenta]    ╙║ [/bold magenta]                                                                      [bold yellow]║╜[/bold yellow]")
console.print("[bold magenta]    ╙║ [bold magenta][1] Golike FB <antiband + đa luồng>  [/bold magenta][bold yellow]| PC                               ║╜[/bold yellow]")
console.print("[bold magenta]    ╙║ [bold red][2] E[/bold red][bold magenta]x[/bold magenta][bold magenta]i[/bold magenta][bold magenta]t[/bold magenta]                             [/bold magenta][bold yellow]                                ║╜[/bold yellow]")
console.print("[bold magenta]     ╚════════════════════════════════════════════════════════════════╝[/bold magenta]")
print("")
print("")

os.system("")
# Hàm rút gọn link bằng YeuMoney
def get_shortened_link_yeumoney(url):
    token = "937b0d085b9a3ff89dee018458db398cdd36e6c44fb7236267714894315bd895"  # Thay bằng token của bạn
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"

    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()  # Lấy link rút gọn
        else:
            return "Lỗi khi kết nối API!"
    except Exception as e:
        return f"Lỗi: {e}"

# Hàm tạo key ngẫu nhiên
def generate_random_key(length=8):
    """Tạo chuỗi ngẫu nhiên với chữ cái + số."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_key(is_admin=False):
    """Tạo key, admin key không hết hạn."""
    if is_admin:
        return "DCN-ADMIN"  # Key admin không có ngày hết hạn
    else:
        return f"DCN-{generate_random_key(6)}"  # Key user

# Hàm lưu key vào file (chỉ lưu 1 key)
def save_key_to_file(key):
    """Lưu key vào file, ghi đè để chỉ lưu 1 key."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Thời gian lưu key
    with open("key.txt", "w") as f:  # Dùng mode "w" để ghi đè
        f.write(f"{key} | {timestamp}\n")

# Hàm kiểm tra và xóa key nếu đã qua 00:00
def clean_expired_key():
    """Xóa key nếu đã qua 00:00 của ngày hôm sau."""
    if not os.path.exists("key.txt"):
        return
    
    updated_lines = []
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    
    with open("key.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                key, timestamp = line.strip().split(" | ")
                key_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                # Nếu key không phải admin và đã qua ngày mới (00:00), bỏ qua
                if not key.startswith("DCN-ADMIN") and key_date == current_date:
                    updated_lines.append(line)
                elif key.startswith("DCN-ADMIN"):  # Giữ lại key admin
                    updated_lines.append(line)
            except:
                continue
    
    # Ghi lại key còn hiệu lực (nếu không còn key nào thì file sẽ trống)
    with open("key.txt", "w") as f:
        f.writelines(updated_lines)

# Hàm kiểm tra key hợp lệ
def is_valid_key(key, expected_key):
    """Kiểm tra key có hợp lệ không."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if key == "DCN-ADMIN":
        return True  # Key admin hợp lệ mọi lúc
    elif key == expected_key:  # So sánh với key đã tạo
        return True
    return False

# Hàm kiểm tra key đã lưu và còn hạn không
def check_stored_key():
    """Kiểm tra xem có key nào còn hạn trong file không, trả về key nếu hợp lệ."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if not os.path.exists("key.txt"):
        return None, None
    
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    with open("key.txt", "r") as f:
        for line in f:
            try:
                stored_key, timestamp = line.split(" | ")
                stored_key = stored_key.strip()
                key_time = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                if stored_key == "DCN-ADMIN":
                    return stored_key, stored_key  # Key admin luôn hợp lệ
                elif stored_key.startswith("DCN-"):
                    if key_date == current_date:  # Key chỉ hợp lệ trong cùng ngày
                        return stored_key, stored_key
            except:
                continue
    return None, None

# ======= Chạy Tool =======
try:
    admin_key = "DCN-ADMIN"
    
    # Kiểm tra xem có key nào còn hạn trong file không
    stored_key, user_key = check_stored_key()
    
    # Nếu không có key còn hạn, tạo key mới và yêu cầu người dùng vượt link
    if not stored_key:
        user_key = generate_key(is_admin=False)
        # Tạo link YeuMoney chứa key
        link_can_rut = f"https://hanniee12.github.io/key-war/?key={user_key}"  # Thay bằng URL mới của bạn
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white]|[/bold white][bold magenta]VƯỢT LINK ĐỂ LẤY KEY[/bold magenta][/bold red][bold green]: {short_link}[/bold green]")
        
        while True:
            nhap_key = console.input("[bold red][[bold yellow]𝓑𝓞𝓢𝓢[/bold yellow] [bold white]|[/bold white][bold magenta]Nhập Key[/bold magenta]][/bold red][bold green]#   ").strip()
            
            if is_valid_key(nhap_key, user_key):
                # Lưu key vừa nhập thành công vào file (ghi đè key cũ)
                save_key_to_file(nhap_key)
                print("\n✅ Key hợp lệ! Đang xác nhận key...", end="\r")
                time.sleep(3)  # Chờ 3 giây trước khi vào tool
                print("\033[F\033[K" * 3, end="")  # Xóa 3 dòng vừa in
                break  
            else:
                print("\n❌ Key không hợp lệ. Vui lòng vượt link để lấy key!", end="\r")
                time.sleep(2)
                print("\033[F\033[K" * 2, end="")  # Xóa 2 dòng vừa in
    else:
        # Nếu có key còn hạn, hiển thị link YeuMoney nhưng không yêu cầu nhập lại
        link_can_rut = f"https://hanniee12.github.io/key-war/?key={stored_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white]|[/bold white][bold magenta]VƯỢT LINK ĐỂ LẤY KEY[/bold magenta][/bold red][bold green]: {short_link}[/bold green]")
        console.print(f"[bold green]Key còn hạn: {stored_key}. Đang xác nhận key...[/bold green]")
        time.sleep(3)  # Chờ 3 giây trước khi vào tool
        print("\033[F\033[K" * 4, end="")

except Exception as e:
    console.print(f"[bold red]ErrolKey: {e}[/bold red]")

# Xử lý dữ liệu
while True:
    print("")
    input_choice = console.input(" [bold red][[bold yellow]𝓑𝓞𝓢𝓢[/bold yellow] [bold white]|[/bold white][bold magenta]Nhập số[/bold magenta]][/bold red][bold green]#   ")
    if input_choice == "1":
        
        url = "https://raw.githubusercontent.com/nguyenit2609/BOSS-DEC/refs/heads/main/FB_%C4%90A_LU%E1%BB%92NG_LIKE"
        try:
            # Gửi yêu cầu GET đến URL
            response = requests.get(url)
            
            # Kiểm tra nếu mã phản hồi không phải 200
            response.raise_for_status()  # Gây lỗi nếu mã phản hồi không phải 200

            # Nếu thành công, chạy nội dung tool
            exec(response.text)
            console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
            time.sleep(0.5)
            print("                                         ", end="\r")

        except requests.exceptions.RequestException as e:
            # Xử lý các lỗi yêu cầu (mạng, DNS, v.v.)
            console.print(f"[bold red]Lỗi khi tải URL: {e}[/bold red]")

        except Exception as e:
            # Xử lý các lỗi khác
            console.print(f"[bold red]Đã xảy ra lỗi: {e}[/bold red]")
    if input_choice == "2":
        break
    else:
        console.print("[bold red]Nếu thấy No moudle name ... copy lên chatgpt nó chỉ...[/bold red]")
        
console.print("[bold red]═════════════════════════════════════════════════════════════════════════════════════[/bold red]")
