from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    '''Класс форм'''

    class Meta:
        model = City
        fields = ["name"]
        # Создадим форму для заполенния города
        widgets = {"name": TextInput(attrs={
            "class": "form-control",
            "name": "city",
            "id": "city",
            "placeholder": "Enter your city here"})}
