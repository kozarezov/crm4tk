from django.db.models.signals import post_delete, post_save
from django.db import models
from datetime import date
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class Client(ChangeloggableMixin, models.Model):
    company_name = models.CharField('Наименование фирмы', max_length=1024)
    contract_data = models.CharField('Номер и дата договора', max_length=1024, blank=True, default='')
    juridical_address = models.CharField('Юридический адрес', max_length=1024, blank=True, default='')
    post_address = models.CharField('Почтовый адрес', max_length=1024, blank=True, default='')
    inn = models.CharField('ИНН', max_length=1024, blank=True, default='')
    kpp = models.CharField('КПП', max_length=1024, blank=True, default='')
    ogrn = models.CharField('ОГРН', max_length=1024, blank=True, default='')
    bik = models.CharField('БИК', max_length=1024, blank=True, default='')
    payment_score = models.CharField('Расчетный счет', max_length=1024, blank=True, default='')
    correspondent_score = models.CharField('Корреспондентский счет', max_length=1024, blank=True, default='')
    bank_name = models.CharField('Наименование банка', max_length=1024, blank=True, default='')
    email = models.EmailField('Электронная почта', blank=True, default='')
    phone = models.CharField('Контактный телефон', max_length=1024, blank=True, default='')
    contact_person = models.CharField('Контактное лицо', max_length=1024, blank=True, default='')
    client_bool = models.BooleanField('Является клиентом', default=False)
    subclient_bool = models.BooleanField('Является перевозчиком', default=False)

    def __str__(self) -> str:
        return self.company_name

    def get_absolute_url(self):
        return f'/clients/{self.id}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

post_save.connect(journal_save_handler, sender=Client)
post_delete.connect(journal_delete_handler, sender=Client)