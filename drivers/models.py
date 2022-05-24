from django.db.models.signals import post_delete, post_save
from cProfile import label
from django.db import models
from datetime import date
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class Driver(ChangeloggableMixin, models.Model):
    name = models.CharField('ФИО Водителя', max_length=1024)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    passport_numbers = models.CharField('Серия/номер паспорта', max_length=1024)
    passport = models.CharField('Паспортные данные', max_length=1024)
    passport_date = models.DateField('Дата выдачи паспорта', blank=True, null=True)
    registration = models.CharField('Прописка', max_length=1024)
    phone = models.CharField('Телефон', max_length=1024)
    driver_license = models.CharField('Номер водительского удостоверения', max_length=1024)
    inn = models.CharField('Номер ИНН', max_length=1024)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/drivers/{self.id}'

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

post_save.connect(journal_save_handler, sender=Driver)
post_delete.connect(journal_delete_handler, sender=Driver)
