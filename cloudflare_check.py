import requests
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Check Cloudflare status of URLs")
    parser.add_argument('--input', '-i', dest='file', help="Check Cloudflare status of URLs from a file")
    parser.add_argument('--domain', '-d', dest='url', help="Check Cloudflare status of a single URL")
    
    args = parser.parse_args()

    if args.url:
        if args.url.startswith('-'):
            print("Hatalı format: URL seçeneği --input veya -i ile başlamalıdır.")
        else:
            cloudflare_status = cloudflare_check(args.url)
            if cloudflare_status is None:
                print(f"Zaman aşımı hatası: {args.url}")
            else:
                status = "YES" if cloudflare_status else "NO"
                print(f"{args.url}: Cloudflare {status}")
    elif args.file:
        try:
            with open(args.file, 'r') as test_file:
                pass
            check_url_list_from_file(args.file)
        except FileNotFoundError:
            print(f"{args.file} dosyası bulunamadı.")
        except Exception as e:
            print("Bir hata oluştu:", e)
            
if __name__ == "__main__":
    main()
