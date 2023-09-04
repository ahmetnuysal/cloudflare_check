FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir requests

COPY url.txt /app
COPY url2.txt /app

CMD ["python", "cloudflare_check.py"]
