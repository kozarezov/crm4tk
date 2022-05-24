from django.db.models.signals import post_delete, post_save
from django.db import models
from orders.models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from docflow.storages import setMediaStorage
import os
from django.db import connection
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler

class DocFlow(ChangeloggableMixin, models.Model):
    
    STATUS_DO = [
        ('Ожидаем документы', 'Ожидаем документы'),
        ('В работе ДО', 'В работе ДО'),
        ('На согласовании ФК', 'На согласовании ФК'),
        ('Согласован', 'Согласован'),
        ('Отклонен', 'Отклонен'),
        ('Оплачен перевозчику', 'Оплачен перевозчику'),
        ('Передан клиенту', 'Передан клиенту'),
        ('Оплачен клиентом', 'Оплачен клиентом'),
    ]
    
    MANAGER = [
        ('Гринева', 'Гринева'),
        ('Спирин', 'Спирин'),
        ('Титова', 'Титова'),
        ('Прибойко', 'Прибойко'),
    ]
    
    def get_upload_to(instance, filename):
        return os.path.join(str(instance.pk), filename)
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='docflow')
    status = models.CharField('Статус документооборота', choices=STATUS_DO, max_length=1024, null=True, blank=True, default='Ожидаем документы')
    date = models.DateField('Дата получения документов', blank=True, null=True, default=None)
    date_in_work = models.DateField('Дата В работе ДО', blank=True, null=True, default=None)
    date_fk = models.DateField('Дата На согласовании ФК', blank=True, null=True, default=None)
    date_agreed = models.DateField('Дата Согласован', blank=True, null=True, default=None)
    date_rejected = models.DateField('Дата Отклонен', blank=True, null=True, default=None)
    date_paid = models.DateField('Дата Оплачен перевозчику', blank=True, null=True, default=None)
    date_send = models.DateField('Дата Передан клиенту', blank=True, null=True, default=None)
    date_paid_client = models.DateField('Дата Оплачен клиентом', blank=True, null=True, default=None)
    account_number = models.CharField('Номер счета', max_length=1024, default="", null=True, blank=True)
    manager_do = models.CharField('Ответсвенный специалист', choices=MANAGER, max_length=1024, null=True, blank=True)
    comment = models.TextField('Комментарий', default="", null=True, blank=True)
    subclient_document = models.FileField('Заявка с перевозчиком', storage=setMediaStorage(), upload_to=get_upload_to, null=True, blank=True)
    ttn_document = models.FileField('ТТН', storage=setMediaStorage(), upload_to=get_upload_to, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Документооборот'
        verbose_name_plural = 'Документооборот'
        
    def get_absolute_url(self):
        return f'/documents/{self.id}'
    
    @receiver(post_save, sender=Order)
    def create_order(sender, instance, created, **kwargs):
        if created:
            DocFlow.objects.create(order=instance)
            
    def date_logs(self):
        for i, el in enumerate(self.STATUS_DO):
            if el[0] == self.status:
                self.set_date(i)
                
    def get_date(self, id=None):
        if id:
            if id == 1:
                return self.date_in_work
            if id == 2:
                return self.date_fk
            if id == 3:
                return self.date_agreed
            if id == 4:
                return self.date_rejected
            if id == 5:
                return self.date_paid
            if id == 6:
                return self.date_send
            if id == 7:
                return self.date_paid_client
        else:
            return self.date_in_work, self.date_fk, self.date_agreed, self.date_rejected, self.date_paid, self.date_send, self.date_paid_client

    def set_date(self, id, date=datetime.date.today()):
        if id == 1:
            self.date_in_work = date
        if id == 2:
            self.date_fk = date
        if id == 3:
            self.date_agreed = date
        if id == 4:
            self.date_rejected = date
        if id == 5:
            self.date_paid = date
        if id == 6:
            self.date_send = date
        if id == 7:
            self.date_paid_client = date
    
    def save(self, *args, **kwargs):
        self.date_logs()
        super(DocFlow, self).save(*args, **kwargs)
        
    def warning(self):
        today = datetime.date.today()
        
        if self.order.date_off_fact and self.status == 'Ожидаем документы':
            done_days = today - self.order.date_off_fact.date()
            done_days = done_days.days
        else:
            done_days = 0
        
        if done_days > 10:
            return True
        else:
            return False
        
    def delete_everything(self):
        DocFlow.objects.all().delete()

    def drop_table(self):
        cursor = connection.cursor()
        table_name = "DOCFLOW"
        sql = "DROP DATABASE %s;" % table_name
        cursor.execute(sql)

post_save.connect(journal_save_handler, sender=DocFlow)
post_delete.connect(journal_delete_handler, sender=DocFlow)