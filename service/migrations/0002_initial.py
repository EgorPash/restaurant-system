# Generated by Django 5.1 on 2024-10-30 13:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='заказчик'),
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.table', verbose_name='столик'),
        ),
        migrations.AddField(
            model_name='table',
            name='times',
            field=models.ManyToManyField(blank=True, null=True, to='service.timesection'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.ManyToManyField(to='service.timesection', verbose_name='время'),
        ),
    ]