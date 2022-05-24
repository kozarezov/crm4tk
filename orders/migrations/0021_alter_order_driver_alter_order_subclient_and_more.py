# Generated by Django 4.0.2 on 2022-03-20 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0007_alter_driver_driver_license_alter_driver_inn_and_more'),
        ('clients', '0004_alter_client_bank_name_alter_client_bik_and_more'),
        ('trucks', '0006_alter_truck_brand_alter_truck_capacity_and_more'),
        ('orders', '0020_orderadress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drivers.driver', verbose_name='Водитель'),
        ),
        migrations.AlterField(
            model_name='order',
            name='subclient',
            field=models.ForeignKey(blank=True, limit_choices_to={'subclient_bool': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_subclient', to='clients.client', verbose_name='Перевозчик'),
        ),
        migrations.AlterField(
            model_name='order',
            name='truck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trucks.truck', verbose_name='Номер машины'),
        ),
        migrations.DeleteModel(
            name='OrderAdress',
        ),
    ]
