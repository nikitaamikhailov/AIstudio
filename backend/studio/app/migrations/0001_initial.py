# Generated by Django 3.2.5 on 2021-07-28 21:33

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Статус персонала')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный пользователь')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, verbose_name='Пароль')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=200, unique=True, verbose_name='Почта')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Пользователи',
            },
        ),
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
    ]
