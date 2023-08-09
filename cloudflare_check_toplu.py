import requests
import sys

def cloudflare_check(url):
    response = requests.head(url, allow_redirects=True)
    server_header = response.headers.get('Server', '').lower()
    return 'cloudflare' in server_header

notdosyasi_adi = 'url.txt'

try:
    with open(notdosyasi_adi, 'r') as notdosyasi:
        for line in notdosyasi:
            url = line.strip()  
            cloudflare_status = "YES" if cloudflare_check(url) else "NO"
            print(f"{url} Cloudflare: {cloudflare_status}")
except FileNotFoundError:
    print(f"{notdosyasi_adi} dosyası bulunamadı.")
except Exception as e:
    print("Bir hata oluştu:", e)
