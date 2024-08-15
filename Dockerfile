# Используем образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копируем все файлы проекта
COPY . .



# Выполняем миграции и запускаем Gunicorn


CMD ["sh", "wait_for_db.sh", "python manage.py migrate && gunicorn warehouse.wsgi:application --bind 0.0.0.0:8000"]