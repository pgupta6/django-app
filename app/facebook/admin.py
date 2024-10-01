from django.contrib import admin
from facebook import models

#Register your models here.
admin.site.register(models.User)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.PostToComment)
admin.site.register(models.Item)

