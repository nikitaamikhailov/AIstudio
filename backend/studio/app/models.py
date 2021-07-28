from django.db import models
from django.contrib.auth.models import UserManager
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from .manager import CustomUserManager
import uuid

def generateUUID():
    return str(uuid4())


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'form/user_{0}/{1}'.format(instance.user.id, filename)


def case_directory_path(instance, filename):
    return 'case/case_{0}'.format(filename)


class Case(models.Model):
    url  = models.SlugField(max_length=160, unique=True)
    img  = models.ImageField("Изображение", upload_to=case_directory_path, default='default.jpg')
    name = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return self.name


class Review(models.Model):
    personName = models.CharField(max_length=50, verbose_name='Автор отзыва')
    textReview = models.CharField(max_length=1000, verbose_name='Текст отзыва')
    date       = models.DateTimeField(auto_now=True, verbose_name='Дата отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class FormData(models.Model):
    name     = models.CharField(max_length=30, verbose_name='Имя клиента')
    phone    = models.CharField(max_length=12, verbose_name='Номер телефона')
    mail     = models.CharField(max_length=50, verbose_name='Почта')
    textData = models.CharField(max_length=5000, null=True, verbose_name='Описание заявки')
    file     = models.FileField(upload_to=user_directory_path, verbose_name='Прикреплленный файл')

    class Meta:
        verbose_name = 'Форма заявки'
        verbose_name_plural = 'Формы заявок'


class Ready(models.Model):
    percent = models.PositiveSmallIntegerField(verbose_name='Процент готовности')
    mark    = models.BooleanField(verbose_name='Галочка', )
    report  = models.FileField()

    class Meta:
        verbose_name = 'Готовность'
        verbose_name_plural = 'Готовность'
    

class Person(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS  = ("phone", "password")
    is_anonymous     = False
    is_authenticated = True
    is_active        = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_staff    = models.BooleanField(default=False, verbose_name='Статус персонала')
    is_active   = models.BooleanField(default=True, verbose_name='Активный пользователь')
    date_joined = models.DateTimeField(default=timezone.now)
    # login       = models.CharField(max_length=40, blank=True, unique=True, verbose_name="Логин")
    phone       = PhoneNumberField(unique=True)
    password    = models.CharField(max_length=100, blank=True, verbose_name="Пароль")
    first_name  = models.CharField(max_length=100, blank=True, verbose_name="Имя")
    second_name = models.CharField(max_length=100, blank=True, verbose_name="Фамилия")
    email       = models.EmailField(max_length=200, blank=True, unique=True, verbose_name="Почта")

    # EMAIL_FIELD    = "email"
    USERNAME_FIELD = "email"
    objects        = CustomUserManager()

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"

    def str(self):
        return self.email


class PersReady(models.Model):
    person_id = models.OneToOneField(Person, on_delete=models.PROTECT)
    ready_id  = models.OneToOneField(Ready, on_delete=CASCADE)