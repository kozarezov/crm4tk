# Generated by Django 4.0.2 on 2022-03-25 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_alter_order_sale_manager'),
        ('docflow', '0005_alter_docflow_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docflow',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docflow', to='orders.order'),
        ),
    ]