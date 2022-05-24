# Generated by Django 4.0.2 on 2022-02-08 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_ogrn'),
        ('drivers', '0002_alter_driver_birthday_alter_driver_passport_date'),
        ('trucks', '0004_auto_20211220_1754'),
        ('orders', '0009_alter_order_cargo_alter_order_driver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cargo',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True, verbose_name='Груз'),
        ),
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, default=' ', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='drivers.driver', verbose_name='Водитель'),
        ),
        migrations.AlterField(
            model_name='order',
            name='logist',
            field=models.CharField(blank=True, choices=[('Петров', 'Петров'), ('Козарезов', 'Козарезов')], default=' ', max_length=20, null=True, verbose_name='Логист'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True, verbose_name='Номер рейса'),
        ),
        migrations.AlterField(
            model_name='order',
            name='subclient',
            field=models.ForeignKey(blank=True, default=' ', limit_choices_to={'subclient_bool': True}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_subclient', to='clients.client', verbose_name='Перевозчик'),
        ),
        migrations.AlterField(
            model_name='order',
            name='truck',
            field=models.ForeignKey(blank=True, default=' ', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trucks.truck', verbose_name='Номер машины'),
        ),
    ]
