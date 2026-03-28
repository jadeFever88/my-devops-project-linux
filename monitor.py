import requests
import time
import os
import logging

# Налаштування логування: записуємо у файл uptime.log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("uptime.log"), # Запис у файл
        logging.StreamHandler()            # Дублювання в термінал
    ]
)

URL = "http://localhost:8081"
CONTAINER_NAME = "my-web-app"

def check_and_fix():
    try:
        response = requests.get(URL, timeout=3)
        if response.status_code == 200:
            logging.info("Сайт працює стабільно.")
        else:
            logging.warning(f"Код відповіді {response.status_code}. Спроба реанімації...")
            os.system(f"docker start {CONTAINER_NAME}")
    except requests.exceptions.ConnectionError:
        logging.error("Сайт НЕДОСТУПНИЙ! Запускаю контейнер...")
        os.system(f"docker start {CONTAINER_NAME}")

logging.info("Система моніторингу та логування запущена.")

while True:
    check_and_fix()
    time.sleep(10) # Перевіряємо кожні 10 секунд
