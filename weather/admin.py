from django.contrib import admin
from .models import City


admin.site.register(City)  # Регистрируем табличку в админ панели
