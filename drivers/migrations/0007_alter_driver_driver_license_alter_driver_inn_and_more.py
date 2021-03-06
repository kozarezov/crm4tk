# Generated by Django 4.0.2 on 2022-03-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0006_alter_driver_passport_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_license',
            field=models.CharField(max_length=1024, verbose_name='Номер водительского удостоверения'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='inn',
            field=models.CharField(max_length=1024, verbose_name='Номер ИНН'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='ФИО Водителя'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='passport',
            field=models.CharField(max_length=1024, verbose_name='Паспортные данные'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='passport_numbers',
            field=models.CharField(max_length=1024, verbose_name='Серия/номер паспорта'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.CharField(max_length=1024, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='registration',
            field=models.CharField(max_length=1024, verbose_name='Прописка'),
        ),
    ]
