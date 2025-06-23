from django.db import models
from django.utils import timezone
from my_project.settings import NULLABLE
from users.models import User


class TimeSection(models.Model):
    time_section = models.CharField(verbose_name='час')

    def __str__(self):
        return self.time_section

    class Meta:
        verbose_name = 'Часовая секция'
        verbose_name_plural = 'Часовые секции'
        ordering = ['time_section']


# Create your models here.
class Table(models.Model):
    number = models.IntegerField(verbose_name='Номер столика')
    seats = models.IntegerField(verbose_name='Количество мест')
    times = models.ManyToManyField(TimeSection, **NULLABLE)
    image = models.ImageField(upload_to='tables/', **NULLABLE)

    def __str__(self):
        return f'Столик номер: {self.number}'

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'
        ordering = ['number']


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='заказчик', **NULLABLE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, verbose_name='столик', **NULLABLE)
    order_time = models.ManyToManyField(TimeSection, verbose_name='время')
    order_date = models.DateField(default=timezone.now, verbose_name='Дата бронирования')
    order_confirm = models.BooleanField(default=False, verbose_name='Поле подтверждения бронирования')
    reservation_date = models.DateField(verbose_name='Дата бронирования', **NULLABLE)

    def __str__(self):
        return f'Заказ {self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['pk']
