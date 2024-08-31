from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    eventer = models.BooleanField(
        'Доступ Ивент-команды',
        default=False
    )
    assist = models.BooleanField(
        'Доступ ассистента',
        default=False
    )
