from unittest.util import _MAX_LENGTH
from django.db import models


class City(models.Model):
    '''Класс создаёт табличку City с полем name и возращает название города'''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
