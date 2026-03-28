import requests
import time
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("uptime.log"), logging.StreamHandler()]
)

# Налаштування
URL_SITE = "http://localhost:8081"
CONTAINER_WEB = "my-web-app"
CONTAINER_DB = "my-db"

def check_infrastructure():
    # 1. Перевірка сайту (HTTP)
    try:
        web_res = requests.get(URL_SITE, timeout=3)
        if web_res.status_code == 200:
            logging.info("🌐 Сайт: OK")
        else:
            logging.warning(f"🌐 Сайт: Помилка {web_res.status_code}. Перезапуск...")
            os.system(f"docker start {CONTAINER_WEB}")
    except:
        logging.error("🌐 Сайт: НЕДОСТУПНИЙ. Реанімація...")
        os.system(f"docker start {CONTAINER_WEB}")

    # 2. Перевірка бази (через Docker inspect)
    # Ми перевіряємо, чи контейнер з базою просто "запущений"
    db_status = os.popen(f"docker inspect -f '{{{{.State.Running}}}}' {CONTAINER_DB}").read().strip()
    if db_status == "true":
        logging.info("🗄️ База: OK")
    else:
        logging.error("🗄️ База: ВПАЛА. Запускаю...")
        os.system(f"docker start {CONTAINER_DB}")

logging.info("🚀 Розширений моніторинг запущено")
while True:
    check_infrastructure()
    print("-" * 30) # Розділювач для краси в терміналі
    time.sleep(10)
