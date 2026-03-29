import requests
import time
import os
import logging

# --- НАЛАШТУВАННЯ ТЕЛЕГРАМ ---
TOKEN = "8223278180:AAGWUQ2mDiIbcRC44WRtfT27zbJSYHIMkfI"
CHAT_ID = "392283203"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Помилка відправки в Telegram: {e}")

# --- ЛОГУВАННЯ ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[logging.FileHandler("uptime.log"), logging.StreamHandler()]
)

URL_SITE = "http://localhost:8081"
CONTAINER_WEB = "my-web-app"

def check_infrastructure():
    try:
        res = requests.get(URL_SITE, timeout=3)
        if res.status_code == 200:
            # Додаємо це, щоб бачити активність у терміналі
            logging.info("✅ Все стабільно. Сайт та база в нормі.")
        else:
            msg = f"⚠️ Сайт видав код {res.status_code}. Перезапускаю..."
            logging.warning(msg)
            send_telegram(msg)
            os.system(f"docker start {CONTAINER_WEB}")
    except:
        msg = "🚨 КАТАСТРОФА! Сайт впав. Спроба оживити..."
        logging.error(msg)
        send_telegram(msg)
        os.system(f"docker start {CONTAINER_WEB}")

logging.info("🤖 Бот-моніторинг активовано!")
send_telegram("🚀 Система моніторингу запущена на вашій віртуалці!")

while True:
    check_infrastructure()
    time.sleep(15)
