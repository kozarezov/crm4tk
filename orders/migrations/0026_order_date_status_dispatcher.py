# Generated by Django 4.0.2 on 2022-04-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_alter_order_sale_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_status_dispatcher',
            field=models.DateField(blank=True, null=True, verbose_name='Дата обновления статуса диспетчера'),
        ),
    ]
