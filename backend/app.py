from flask import Response, Flask
from redis import Redis
import os

app = Flask(__name__)

# Ми використовуємо назву сервісу 'database' як хост
# Якщо у вашому docker-compose.yml назва інша — змініть її тут
redis = Redis(host='database', port=6379, socket_connect_timeout=2)

@app.route('/')
def hello():
    try:
        count = redis.incr('hits')
        # Формуємо рядок так, щоб він виглядав як метрика для Prometheus
        # Формат: назва_метрики значення
        output = f"hits_total {count}\napp_up 1"
        return Response(output, mimetype='text/plain')
    except Exception as e:
        # Якщо Redis впав, ми повертаємо статус 0
        output = f"hits_total 0\napp_up 0\nerror_info {e}"
        return Response(output, mimetype='text/plain', status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
