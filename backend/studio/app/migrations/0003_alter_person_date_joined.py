# Generated by Django 3.2.6 on 2021-08-11 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210812_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации'),
        ),
    ]