# Generated by Django 3.2.7 on 2021-12-20 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.ForeignKey(limit_choices_to={'client_bool': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Выберите клиента'),
        ),
    ]
