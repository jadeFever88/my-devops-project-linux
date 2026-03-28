#!/bin/bash

echo "🚀 Починаємо деплой нашого сайту..."

# Зупиняємо старий контейнер, якщо він є
docker rm -f my-web-app 2>/dev/null

# Запускаємо новий з нашою папкою
docker run -d \
  --name my-web-app \
  -p 8081:80 \
  -v $(pwd):/usr/share/nginx/html \
  nginx

echo "✅ Готово! Сайт доступний на порту 8081"
docker ps | grep my-web-app
