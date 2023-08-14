import argparse
from lib import cloudflare_check, check_url_list_from_file

def main():
    parser = argparse.ArgumentParser(description="Check Cloudflare status of URLs")
    parser.add_argument('--input', '-i', dest='file', help="Check Cloudflare status of URLs from a file")
    parser.add_argument('--domain', '-d', dest='url', help="Check Cloudflare status of a single URL")

    args, unknown_args = parser.parse_known_args()

    if unknown_args:
        print("Hatalı format: URL seçeneği --domain veya -d ile, Dosya seçeneği --input veya -i ile başlamalıdır.")
        return 

    if args.url:
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
    else:
        print("Hatalı format: Bir URL veya dosya seçeneği belirtmelisiniz.")

if __name__ == "__main__":
    main()
