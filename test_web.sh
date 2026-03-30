#!/bin/bash
# Перевіряємо, чи повертає сервер статус 200 (ОК)
status_code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost)

if [ "$status_code" -eq 200 ]; then
  echo "Тест пройдено: Сайт доступний (Status 200)"
  exit 0
else
  echo "Тест провалено: Сервер повернув статус $status_code"
  exit 1
fi
