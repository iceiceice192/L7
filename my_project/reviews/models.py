from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Абстрактная базовая модель (требование задания)
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True

# Таблица 1: Жанры
class Genre(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="Название жанра")

    def __str__(self):
        return self.name

# Таблица 2: Книги
class Book(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books', verbose_name="Жанр")

    def __str__(self):
        return self.title

# Таблица 3: Отзывы (Связывает Книгу и Пользователя)
class Review(TimeStampedModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name="Книга")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка (1-5)"
    )

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"