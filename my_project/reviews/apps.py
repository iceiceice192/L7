from django.apps import AppConfig

class ReviewsConfig(AppConfig):
    # Тип поля для первичных ключей (ID) по умолчанию
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews' # Имя нашего приложения
    verbose_name = 'Сервис отзывов на книги'
