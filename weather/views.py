from django.shortcuts import render


def index(request):
    return render(request, 'weather/index.html')  # Функция вызова шаблона главной страницы
