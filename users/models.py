from django.contrib.auth.models import AbstractUser
from django.db import models

from my_project.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=50,
        verbose_name="Адрес электронной почты",
        unique=True,
        help_text='Введите адрес электронной почты'
    )

    avatar = models.ImageField(
        upload_to='users/',
        verbose_name='аватар',
        **NULLABLE,
        help_text='Выберите аватар'
    )

    phone = models.CharField(
        max_length=35,
        verbose_name='телефон',
        **NULLABLE,
        help_text='Укажите телефон'
    )

    country = models.CharField(
        max_length=50,
        verbose_name='страна',
        **NULLABLE,
        help_text='Укажите страну'
    )

    verification_code = models.CharField(
        max_length=50,
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Пользователь: {self.email}'
    class Meta:
        verbose_name = 'Пользователь сервиса'
        verbose_name_plural = 'Пользователи сервиса'
        ordering = ['-date_joined', '-email']
