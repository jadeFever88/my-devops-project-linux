import requests
import time

# URL твого сайту (порт 8081 ми вказали в deploy.sh)
URL = "http://localhost:8081"

def check_site():
    try:
        response = requests.get(URL, timeout=3)
        if response.status_code == 200:
            print(f"✅ [{time.strftime('%H:%M:%S')}] Все супер! Сайт відповідає.")
        else:
            print(f"⚠️ [{time.strftime('%H:%M:%S')}] Упс! Код помилки: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"🚨 [{time.strftime('%H:%M:%S')}] КАТАСТРОФА! Сайт не працює. Перевір Docker!")

print("🕵️ Моніторинг запущено... (Ctrl+C щоб вийти)")
while True:
    check_site()
    time.sleep(5)
