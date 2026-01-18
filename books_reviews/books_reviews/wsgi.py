import os
from django.core.wsgi import get_wsgi_application

# Указываем настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

# Создаем WSGI-приложение
application = get_wsgi_application()