# Docker taban imajını belirle (python sürümüne göre değiştirin)
FROM python:3.8

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli dosyaları kopyala
COPY . .

# Gerekli Python bağımlılıklarını yükle
RUN pip install --no-cache-dir requests

# .txt dosyalarını konteynere kopyala
COPY url.txt /app
COPY url2.txt /app

# Ana kodu çalıştır
CMD ["python", "cloudflare_check.py"]
