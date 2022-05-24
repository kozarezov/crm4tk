from datetime import datetime
from django.db.models.signals import post_delete, post_save
from django.db import models
from clients.models import Client
from trucks.models import Truck
from addresses.models import Address
from drivers.models import Driver
import os
from docflow.storages import setMediaStorage
from django.db import connection
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler

class Order(ChangeloggableMixin, models.Model):
    def get_upload_to(instance, filename):
        return os.path.join(str(instance.pk), filename)

    STATUS = [
        ('Актуальная', 'Актуальная'),
        ('Бронь', 'Бронь'),
        ('Срыв', 'Срыв'),
        ('Закрыта КА', 'Закрыта КА'),
        ('Обнулена', 'Обнулена'),
        ('ТС назначен', 'ТС назначен'),
        ('Выполнена', 'Выполнена'),
    ]
    
    STATUS_DISPATCHER = [
        ('В пути на погрузку', 'В пути на погрузку'),
        ('На погрузке', 'На погрузке'),
        ('В пути на выгрузку', 'В пути на выгрузку'),
        ('На выгрузке', 'На выгрузке'),
        ('Нет связи', 'Нет связи'),
        ('Рейс окончен, документы получены', 'Рейс окончен, документы получены'),
        ('Опаздывает', 'Опаздывает'),
        ('Поломка', 'Поломка'),
    ]
    
    TYPE = [
        ('ТЕНТ', 'ТЕНТ'),
        ('ТЕРМ', 'ТЕРМ'),
        ('РЕФ', 'РЕФ'),
        ('БОРТ', 'БОРТ'),
        ('ТРАЛ', 'ТРАЛ'),
    ]

    LOGISTS = [
        ('Домашенко А.А.', 'Домашенко А.А.'),
        ('Дымшиц Е.М.', 'Дымшиц Е.М.'),
        ('Саморай А.П.', 'Саморай А.П.'),
        ('Вотрин Р.В.', 'Вотрин Р.В.'),
        ('Ширяева Д.В.', 'Ширяева Д.В.'),
        ('Панасенко А.И.', 'Панасенко А.И.'),
        ('Максимович О.В.', 'Максимович О.В.'),
    ]
    
    SALE_MANAGER = [
        ('Крушельницкая Р.А.', 'Крушельницкая Р.А.'),
        ('Новосельцева Г.А.', 'Новосельцева Г.А.'),
        ('Иовлева С.В.', 'Иовлева С.В.'),
        ('Марушко А.О', 'Марушко А.О'),
        ('Коновалов Н.А', 'Коновалов Н.А'),
        ('Сафонова А. В.', 'Сафонова А. В.'),
        ('Соловьева Н.А.', 'Соловьева Н.А.'),
        ('Карнаухова Т.В.', 'Карнаухова Т.В.'),
        ('Лещенко Е.В', 'Лещенко Е.В'),
        ('Павлов Г.Н', 'Павлов Г.Н'),
        ('Колесник Д.В.', 'Колесник Д.В.'),
        ('Кругликов С.И.', 'Кругликов С.И.'),
        ('Кремнев А.А.', 'Кремнев А.А.'),
        ('Потапенко М.С.', 'Потапенко М.С.'),
        ('Мешкова А.М.', 'Мешкова А.М.'),
    ]

    date = models.DateField('Дата рейса')
    client = models.ForeignKey(Client, verbose_name="Клиент", on_delete=models.SET_NULL, null=True, limit_choices_to={'client_bool': True}, related_name='order_client')
    order_number = models.CharField('Номер рейса', max_length=1024, default="", null=True, blank=True)
    drop_on = models.ForeignKey(Address, verbose_name="Точка погрузки", on_delete=models.SET_NULL, null=True, limit_choices_to={'drop_on': True}, related_name='order_drop_on')
    drop_off = models.ForeignKey(Address, verbose_name="Точка выгрузки", on_delete=models.SET_NULL, null=True, limit_choices_to={'drop_off': True}, related_name='order_drop_off')
    date_on = models.DateTimeField('Дата погрузки')
    date_off = models.DateTimeField('Дата выгрузки')
    cargo = models.CharField('Груз', max_length=1024, null=True, default="", blank=True)
    pallet = models.IntegerField('Количество паллет', default=0, blank=True)
    required_type = models.CharField('Тент/Терм/Реф', choices=TYPE, max_length=5)
    required_info = models.CharField('Доп.требования к ТС', max_length=1024, null=True, default="", blank=True)
    client_cost = models.FloatField('Ставка клиента', default=0)
    subclient = models.ForeignKey(Client, verbose_name="Перевозчик", on_delete=models.SET_NULL, null=True, limit_choices_to={'subclient_bool': True}, related_name='order_subclient', blank=True)
    truck = models.ForeignKey(Truck, verbose_name="Номер машины", on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(Driver, verbose_name="Водитель", on_delete=models.SET_NULL, null=True, blank=True)
    subclient_cost = models.FloatField('Ставка перевозчика', default=0, null=True, blank=True)
    logist = models.CharField('Логист', choices=LOGISTS, max_length=1024, default="", null=True, blank=True)
    status = models.CharField('Статус заявки', choices=STATUS, max_length=1024, default='Актуальная')
    date_on_fact = models.DateTimeField('Дата погрузки фактическая', blank=True, null=True)
    date_off_fact = models.DateTimeField('Дата выгрузки фактическая', blank=True, null=True)
    comment = models.CharField('Комментарий', max_length=1024, default="", null=True, blank=True)
    status_dispatcher = models.CharField('Статус диспетчера', choices=STATUS_DISPATCHER, max_length=1024, null=True, blank=True)
    problem_bool = models.BooleanField('Проблема в рейсе', default=False)
    sale_manager = models.CharField('Клиентский менеджер', choices=SALE_MANAGER, max_length=1024, default="", null=True, blank=True)
    subclient_document = models.FileField('Заявка с перевозчиком', storage=setMediaStorage(), upload_to=get_upload_to, null=True, blank=True)
    ttn_document = models.FileField('ТТН', storage=setMediaStorage(), upload_to=get_upload_to, null=True, blank=True)
    drop_on_plus = models.ForeignKey(Address, verbose_name="Доп.Точка погрузки", on_delete=models.SET_NULL, blank=True, null=True, limit_choices_to={'drop_on': True}, related_name='order_drop_on_plus')
    drop_off_plus = models.ForeignKey(Address, verbose_name="Доп.Точка выгрузки", on_delete=models.SET_NULL, blank=True, null=True, limit_choices_to={'drop_off': True}, related_name='order_drop_off_plus')
    date_on_plus = models.DateTimeField('Доп.Дата погрузки', blank=True, null=True)
    date_off_plus = models.DateTimeField('Доп.Дата выгрузки', blank=True, null=True)
    date_status_dispatcher = models.DateField('Дата обновления статуса диспетчера', blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return f'/orders/{self.id}'
    
    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
        
    @classmethod
    def total(cls):
        return cls.objects.filter(status='Актуальная').count()
    
    @classmethod
    def total_in_way(cls):
        return cls.objects.filter(status='ТС назначен').filter(problem_bool=True).count()
        
    def get_subclient_cost(self):
        if self.client_cost > 0:
            return int(self.client_cost * 0.97)
        return 0
    
    def margin(self):
        return int(self.client_cost - self.subclient_cost)

    def gross(self):
        return int(self.client_cost)
    
    def margin_percent(self):
        margin = self.margin()
        
        if margin == 0:
            return 0
        else:
            return str(round(margin / self.client_cost * 100, 2))
        
    def delete_everything(self):
        Order.objects.all().delete()

    def drop_table(self):
        cursor = connection.cursor()
        table_name = "ORDERS"
        sql = "DROP TABLES %s;" % table_name
        cursor.execute(sql)

    def sberfraht_status(self):
        if self.status == 'Актуальная' or self.status == 'Бронь':
            return 'в работе'
        elif self.status == 'ТС назначен' or self.status == 'Выполнена':
            return 'Выполнена'
        elif self.status == 'Обнулена':
            return 'Отказ клиента'
        else:
            return 'ТС не найден'
    
    def sberfraht_status_1(self):
        if self.sberfraht_status() == 'ТС не найден':
            return 'Нет предложения от перевозчиков'
        else:
            return ''

    def sberfraht_status_2(self):
        if self.sberfraht_status() == 'ТС не найден' or self.sberfraht_status() == 'в работе':
            return ''
        else:
            return 'ТС найдена, ставка согласована'

    def get_docflow_id(self):
        return self.objects.get(pk=self.pk).DocFlow_set.id

    def get_non_nds(self):
        return round(self.subclient_cost / 1.2)
    
    def save(self, *args, **kwargs):
        if self.status_dispatcher != None:
            self.date_status_dispatcher = datetime.today()
        super(Order, self).save(*args, **kwargs)
    
    def today_bool(self):
        if self.date_status_dispatcher == datetime.today().date():
            return True
        else:
            return False

    def get_subclient_cost(self):
        return int(self.subclient_cost)
    
    def get_client_cost(self):
        return int(self.client_cost)


post_save.connect(journal_save_handler, sender=Order)
post_delete.connect(journal_delete_handler, sender=Order)
