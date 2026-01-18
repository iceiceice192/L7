from django.contrib import admin
from .models import Genre, Book, Review

# Простая регистрация моделей
admin.site.register(Genre)
admin.site.register(Book)

# Для отзывов можно сделать чуть красивее (видно кто, что и рейтинг)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')