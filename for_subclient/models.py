from django.db import models

class Ttn(models.Model):
    date = models.DateField('Дата рейса')
    order_number = models.CharField('Номер заявки клиента', max_length=1024, default="", null=True, blank=True)
    client = models.CharField('Клиент (заказчик услуги 1-а)', max_length=1024, default="", null=True, blank=True)
    client_data = models.CharField('ИНН Клиента / юр.Адрес раздел 1-а', max_length=1024, default="", null=True, blank=True)
    cargoholder = models.CharField('Грузоотправитель', max_length=1024, default="", null=True, blank=True)
    cargoholder_data = models.CharField('ИНН Грузоотправителя / юр.Адрес', max_length=1024, default="", null=True, blank=True)
    drop_on = models.CharField('Адрес погрузки', max_length=1024, default="", null=True, blank=True)
    cargorecipient = models.CharField('Грузополучатель', max_length=1024, default="", null=True, blank=True)
    cargorecipient_data = models.CharField('ИНН Грузополучателя / юр.Адрес', max_length=1024, default="", null=True, blank=True)
    drop_off = models.CharField('Адрес выгрузки', max_length=1024, default="", null=True, blank=True)
    subclient = models.CharField('Перевозчик', max_length=1024, default="", null=True, blank=True)
    subclient_data = models.CharField('ИНН Перевозчика / юр.адрес', max_length=1024, default="", null=True, blank=True)
    driver = models.CharField('ФИО Водителя', max_length=1024, default="", null=True, blank=True)
    truck = models.CharField('Номер машины', max_length=1024, default="", null=True, blank=True)
    model = models.CharField('Марка машины', max_length=1024, default="", null=True, blank=True)
    trailer = models.CharField('Номер Прицепа', max_length=1024, default="", null=True, blank=True)
    cargo = models.CharField('Груз', max_length=1024, default="", null=True, blank=True)
    pallet = models.CharField('Количетсво мест', max_length=1024, default="", null=True, blank=True)
    weight = models.CharField('Вес', max_length=1024, default="", null=True, blank=True)
    subclient_contract = models.CharField('Реквизиты договора с перевозчиком ', max_length=1024, default="", null=True, blank=True)
    client_contract = models.CharField('Реквизиты договора с клиентом ', max_length=1024, default="", null=True, blank=True)
    
    def __str__(self):
        return self.order_number
    
    def get_absolute_url(self):
        return f'/ttn/{self.id}'
    
    class Meta:
        verbose_name = 'ТН'
        verbose_name_plural = 'ТН'
