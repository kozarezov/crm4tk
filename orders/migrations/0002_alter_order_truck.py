# Generated by Django 3.2.5 on 2022-01-13 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0004_auto_20211220_1754'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='truck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trucks.truck', verbose_name='Номер машины'),
        ),
    ]
