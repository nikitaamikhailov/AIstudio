from django.contrib import admin

from . import models

admin.site.register(models.Case)
admin.site.register(models.Review)
admin.site.register(models.FormData)
admin.site.register(models.PersReady)
admin.site.register(models.Ready)
admin.site.register(models.Person)