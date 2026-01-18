# Используем официальный образ Python
FROM python:3.10-slim

# Запрещаем Python писать pyc файлы и буферизовать вывод
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Команда запуска (будет переопределена в docker-compose, но полезна для доки)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]