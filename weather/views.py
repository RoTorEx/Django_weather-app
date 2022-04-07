from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests


def index(request):
    app_id = "acc48f91d35aafd02e3b9f305c82243f"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + app_id

    if(request.method == 'POST'):
        # Создаём объект на основе класс, который содержит форму
        form = CityForm(request.POST)  # В переменную мы сохраняем данные полученные от пользователя
        form.save()  # Сохраняет даныне в БД

    form = CityForm()  # Для очистки формы, после вписания

    cities = City.objects.all()  # Делаем выборку из таблицы City

    all_cities = []

    for city in cities:
        response = requests.get(url.format(city.name)).json()  # Получаем ответ в json формате и конвертируем его в dict

        city_info = {
            "city": city.name,
            "temp": response["main"]["temp"],
            "icon": response["weather"][0]["icon"],
        }

        all_cities.append(city_info)

    context = {"all_info": all_cities, "form": form}

    return render(request, 'weather/index.html', context)  # Функция вызова шаблона главной страницы
