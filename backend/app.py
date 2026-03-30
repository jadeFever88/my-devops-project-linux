from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Ми використовуємо назву сервісу 'database' як хост
# Якщо у вашому docker-compose.yml назва інша — змініть її тут
redis = Redis(host='database', port=6379, socket_connect_timeout=2)

@app.route('/')
def hello():
    try:
        # Спроба збільшити лічильник у Redis
        count = redis.incr('hits')
        return f'<h1>Успіх!</h1><p>Цю сторінку переглянули <b>{count}</b> разів.</p>'
    except Exception as e:
        # Якщо база не доступна, ми побачимо текст помилки
        return f'<h1>Помилка підключення!</h1><p>Додаток не бачить Redis. Помилка: <code>{e}</code></p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
