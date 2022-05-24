from django.db.models.signals import post_delete, post_save
from django.db import models
from clients.models import Client
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class Address(ChangeloggableMixin, models.Model):
    all_client = Client.objects.order_by('-id')
    name = models.CharField('Наименование точки погрузки', max_length=1024)
    city = models.CharField('Город', max_length=1024)
    address = models.CharField('Адрес', max_length=1024)
    client = models.ForeignKey(Client, verbose_name="Клиент" ,on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'client_bool': True})
    phone = models.CharField('Контактный телефон', max_length=1024, blank=True, default='')
    contact_person = models.CharField('Контактное лицо', max_length=1024, blank=True, default='')
    drop_on = models.BooleanField('Является грузоотправителем', default=False)
    drop_off = models.BooleanField('Является грузополучателем', default=False)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/addresses/{self.id}'
    
    def get_verbose_name(object): 
        return object._meta.verbose_name

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

post_save.connect(journal_save_handler, sender=Address)
post_delete.connect(journal_delete_handler, sender=Address)