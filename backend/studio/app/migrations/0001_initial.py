# Generated by Django 3.2.5 on 2021-07-20 13:45

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('img', models.ImageField(default='default.jpg', upload_to=app.models.case_directory_path, verbose_name='Изображение')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя клиента')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('mail', models.CharField(max_length=50, verbose_name='Почта')),
                ('textData', models.CharField(max_length=5000, null=True, verbose_name='Описание заявки')),
                ('file', models.FileField(upload_to=app.models.user_directory_path, verbose_name='Прикреплленный файл')),
            ],
            options={
                'verbose_name': 'Форма заявки',
                'verbose_name_plural': 'Формы заявок',
            },
        ),
        migrations.CreateModel(
            name='Ready',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.PositiveSmallIntegerField(verbose_name='Процент готовности')),
                ('mark', models.BooleanField(verbose_name='Галочка')),
                ('report', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Готовность',
                'verbose_name_plural': 'Готовность',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personName', models.CharField(max_length=50, verbose_name='Автор отзыва')),
                ('textReview', models.CharField(max_length=1000, verbose_name='Текст отзыва')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='PersReady',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('ready_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.ready')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='persone', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователь',
            },
        ),
    ]
