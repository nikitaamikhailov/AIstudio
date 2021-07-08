from django.db import models
from django.db.models.fields.files import ImageField


class Case(models.Model):
    url = models.SlugField('Ссылка', max_length=150, unique=True)
    name = models.CharField('Имя', max_length=50)
    image = ImageField('Изображение', upload_to = 'CaseImage/')
    
    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = 'Кейсы'
    




# class User(models.Model):
#     mail = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)