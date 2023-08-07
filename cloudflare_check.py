import requests
import sys

def cloudflare_check(url):
    response = requests.head(url, allow_redirects=True)
    server_header = response.headers.get('Server', '').lower()
    return 'cloudflare' in server_header

url = sys.argv[2]
cloudflare_status = "YES" if cloudflare_check(url) else "NO"
print(f"{url}: Cloudflare {cloudflare_status}")
      
