# Generated by Django 3.2.7 on 2021-12-20 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование точки погрузки')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=15, verbose_name='Контактный телефон')),
                ('contact_person', models.CharField(max_length=50, verbose_name='Контактное лицо')),
                ('drop_on', models.BooleanField(default=False, verbose_name='Является грузоотправителем')),
                ('drop_off', models.BooleanField(default=False, verbose_name='Является грузополучателем')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]
