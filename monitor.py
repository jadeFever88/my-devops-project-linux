import requests
import time
import os

URL = "http://localhost:8081"
CONTAINER_NAME = "my-web-app"

def check_and_fix():
    try:
        response = requests.get(URL, timeout=3)
        if response.status_code == 200:
            print(f"✅ [{time.strftime('%H:%M:%S')}] Сайт працює.")
        else:
            print(f"⚠️ [{time.strftime('%H:%M:%S')}] Код {response.status_code}. Спроба перезапуску...")
            os.system(f"docker start {CONTAINER_NAME}")
    except requests.exceptions.ConnectionError:
        print(f"🚨 [{time.strftime('%H:%M:%S')}] Сайт ПАВ! Оживляю контейнер...")
        # Ось тут магія: Python сам пише команду в консоль за тебе
        os.system(f"docker start {CONTAINER_NAME}")

print("👨‍⚕️ Лікар-моніторинг запущено...")
while True:
    check_and_fix()
    time.sleep(5)
