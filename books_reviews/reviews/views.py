from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import Book, Review, Genre
import openpyxl # Для экспорта
from django.apps import apps # Для получения списка моделей

# Главная страница + Поиск (Доп. функционал)
def index(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

# Детальная страница книги + Добавление отзыва (Основная услуга)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST" and request.user.is_authenticated:
        Review.objects.create(
            book=book,
            user=request.user,
            text=request.POST.get('text'),
            rating=request.POST.get('rating')
        )
        return redirect('book_detail', pk=pk)
    return render(request, 'book_detail.html', {'book': book})

# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# --- Логика для Админа (Экспорт) ---
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_export_view(request):
    # Получаем список наших моделей
    models_list = ['Genre', 'Book', 'Review', 'User']
    
    if request.method == 'POST':
        selected_model_name = request.POST.get('model')
        selected_fields = request.POST.getlist('fields')
        
        # Генерация XLSX
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={selected_model_name}.xlsx'
        
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = selected_model_name
        
        # Заголовки
        ws.append(selected_fields)
        
        # Данные
        Model = apps.get_model('reviews', selected_model_name) if selected_model_name != 'User' else apps.get_model('auth', 'User')
        
        # Динамическое получение данных по выбранным полям
        for obj in Model.objects.all():
            row = [str(getattr(obj, field)) for field in selected_fields]
            ws.append(row)
            
        wb.save(response)
        return response

    return render(request, 'export.html', {'models': models_list})