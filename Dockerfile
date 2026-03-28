# 1. Беремо готовий образ з веб-сервером Nginx
FROM nginx:alpine

# 2. Копіюємо наш файл index.html всередину контейнера
COPY index.html /usr/share/nginx/html/index.html

# 3. Кажемо, що контейнер буде слухати 80-й порт
EXPOSE 80
