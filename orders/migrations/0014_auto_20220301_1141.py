# Generated by Django 3.2.5 on 2022-03-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_order_cargo_alter_order_driver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_off_fact',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выгрузки фактическая'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_on_fact',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата погрузки фактическая'),
        ),
        migrations.AddField(
            model_name='order',
            name='problem_bool',
            field=models.BooleanField(default=False, verbose_name='Проблема в рейсе'),
        ),
        migrations.AddField(
            model_name='order',
            name='status_dispatcher',
            field=models.CharField(blank=True, choices=[('В пути на погрузку', 'В пути на погрузку'), ('На погрузке', 'На погрузке'), ('В пути на выгрузку', 'В пути на выгрузку'), ('На выгрузке', 'На выгрузке'), ('Нет связи', 'Нет связи'), ('Рейс окончен, документы получены', 'Рейс окончен, документы получены'), ('В работе ДО', 'В работе ДО'), ('Опаздывает', 'Опаздывает'), ('Поломка', 'Поломка')], max_length=50, null=True, verbose_name='Статус диспетчера'),
        ),
        migrations.AddField(
            model_name='order',
            name='status_do',
            field=models.CharField(blank=True, choices=[('Ожидаем документы', 'Ожидаем документы'), ('В работе ДО', 'В работе ДО'), ('На согласовании ФК', 'На согласовании ФК'), ('Согласован', 'Согласован'), ('Отклонен', 'Отклонен'), ('Оплачен', 'Оплачен')], max_length=50, null=True, verbose_name='Статус документооборота'),
        ),
        migrations.AlterField(
            model_name='order',
            name='logist',
            field=models.CharField(blank=True, choices=[('Домашенко А.А.', 'Домашенко А.А.'), ('Дымшиц Е.М.', 'Дымшиц Е.М.'), ('Саморай А.П.', 'Саморай А.П.'), ('Вотрин Р.В.', 'Вотрин Р.В.'), ('Ширяева Д.В.', 'Ширяева Д.В.'), ('Панасенко А.И.', 'Панасенко А.И.'), ('Максимович О.В.', 'Максимович О.В.')], default='', max_length=50, null=True, verbose_name='Логист'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Актуальная', 'Актуальная'), ('Бронь', 'Бронь'), ('Срыв', 'Срыв'), ('Обнулена', 'Обнулена'), ('ТС назначен', 'ТС назначен'), ('Выполнена', 'Выполнена')], default='Актуальная', max_length=50, verbose_name='Статус заявки'),
        ),
    ]
