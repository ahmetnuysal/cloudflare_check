import requests

def cloudflare_check(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        server_header = response.headers.get('Server', '').lower()
        return 'cloudflare' in server_header
    except requests.exceptions.Timeout:
        return None 

def check_url_list_from_file(file_path):
    try:
        with open(file_path, 'r') as notdosyasi:
            for line in notdosyasi:
                url = line.strip()  
                cloudflare_status = cloudflare_check(url)
                if cloudflare_status is None:
                    print(f"Zaman aşımı hatası: {url}")
                else:
                    status = "YES" if cloudflare_status else "NO"
                    print(f"{url} Cloudflare: {status}")
    except FileNotFoundError:
        print(f"{file_path} dosyası bulunamadı.")
    except Exception as e:
        print("Bir hata oluştu:", e)
