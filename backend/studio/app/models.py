from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.


class Case(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    url = models.SlugField()
    img = models.ImageField(verbose_name='Картинка')
    name = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'


class Review(models.Model):
    personName = models.CharField(max_length=50, verbose_name='Автор отзыва')
    textReview = models.CharField(max_length=1000, verbose_name='Текст отзыва')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class FormData(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя клиента')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    mail = models.CharField(max_length=50, verbose_name='Почта')
    textData = models.CharField(max_length=5000, null=True, verbose_name='Описание заявки')
    file = models.FileField(upload_to=user_directory_path, verbose_name='Прикреплленный файл')

    class Meta:
        verbose_name = 'Форма заявки'
        verbose_name_plural = 'Формы заявок'


class Report(models.Model):
    pass

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'


class Ready(models.Model):
    percent = models.PositiveSmallIntegerField(verbose_name='Процент готовности')
    mark = models.BooleanField(verbose_name='Галочка')
    report = models.OneToOneField(Report, on_delete=CASCADE, verbose_name='Отчет')

    class Meta:
        verbose_name = 'Готовность'
        verbose_name_plural = 'Готовность'


class PersReady(models.Model):
    person_id = models.ForeignKey(User, on_delete=models.PROTECT)
    ready_id = models.ForeignKey(Ready, on_delete=CASCADE)
    