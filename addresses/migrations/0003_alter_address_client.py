# Generated by Django 3.2.7 on 2021-12-20 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_ogrn'),
        ('addresses', '0002_alter_address_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.ForeignKey(limit_choices_to={'client_bool': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Клиент'),
        ),
    ]
