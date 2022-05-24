from ast import mod
from django.db import models
from docflow.storages import setMediaStorage
import os
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Телефон', blank=True, default='', max_length=1024, null=True)
    position = models.CharField('Должность', blank=True, default='', max_length=1024, null=True)
    theme = models.BooleanField('Тема пользователя', default=False)

    def __str__(self) -> str:
        return self.user.username
    
    def initials(self):
        return str(self.user.last_name)[0] + str(self.user.first_name)[0]
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class FileStorage(models.Model):
    
    file_name = models.CharField('Наименование файла', max_length=1024)
    document = models.FileField('Файл', storage=setMediaStorage(), null=True, blank=True)

    def __str__(self) -> str:
        return self.file_name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'