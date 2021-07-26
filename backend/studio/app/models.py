from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'form/user_{0}/{1}'.format(instance.user.id, filename)


def case_directory_path(instance, filename):
    return 'case/case_{0}'.format(filename)


class Case(models.Model):
    url = models.SlugField(max_length=160, unique=True)
    img = models.ImageField("Изображение", upload_to=case_directory_path, default='default.jpg')
    name = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return self.name


class Review(models.Model):
    personName = models.CharField(max_length=50, verbose_name='Автор отзыва')
    textReview = models.CharField(max_length=1000, verbose_name='Текст отзыва')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class FormData(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя клиента')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    mail = models.CharField(max_length=50, verbose_name='Почта')
    textData = models.CharField(max_length=5000, null=True, verbose_name='Описание заявки')
    file = models.FileField(upload_to=user_directory_path, verbose_name='Прикреплленный файл')

    class Meta:
        verbose_name = 'Форма заявки'
        verbose_name_plural = 'Формы заявок'


class Ready(models.Model):
    percent = models.PositiveSmallIntegerField(verbose_name='Процент готовности')
    mark = models.BooleanField(verbose_name='Галочка', )
    report = models.FileField()

    class Meta:
        verbose_name = 'Готовность'
        verbose_name_plural = 'Готовность'


class PersReady(models.Model):
    person_id = models.OneToOneField(User, on_delete=models.PROTECT)
    ready_id = models.OneToOneField(Ready, on_delete=CASCADE)
    

class Person(User):
    phone = PhoneNumberField()
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'


