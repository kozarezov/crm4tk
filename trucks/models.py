from django.db.models.signals import post_delete, post_save
from django.db import models
from clients.models import Client
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler

class Truck(ChangeloggableMixin, models.Model):

    TYPE = [
        ('ТЕНТ', 'ТЕНТ'),
        ('ТЕРМ', 'ТЕРМ'),
        ('РЕФ', 'РЕФ'),
        ('БОРТ', 'БОРТ'),
        ('ТРАЛ', 'ТРАЛ'),
    ]

    CAPACITY= [
        ('1,5т.', '1,5т.'),
        ('3,5т.', '3,5т.'),
        ('5т.', '5т.'),
        ('10т.', '10т.'),
        ('20т.', '20т.'),
    ]

    truck_number = models.CharField('Номер тягача', max_length=1024)
    trailer_number = models.CharField('Номер прицепа', max_length=1024)
    type = models.CharField('Тент/Терм/Реф', choices=TYPE, max_length=1024)
    capacity = models.CharField('Грузовместимость', choices=CAPACITY, max_length=1024)
    vin_number = models.CharField('VIN номер (необязательно)', blank=True, max_length=1024)
    brand = models.CharField('Марка/Модель/Цвет (необязательно)', blank=True, max_length=1024)
    owner = models.ForeignKey(Client, verbose_name="Выберите перевозчика", on_delete=models.SET_NULL, null=True, limit_choices_to={'subclient_bool': True})
    

    def __str__(self) -> str:
        return self.truck_number
        
    def get_absolute_url(self):
        return f'/trucks/{self.id}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

post_save.connect(journal_save_handler, sender=Truck)
post_delete.connect(journal_delete_handler, sender=Truck)