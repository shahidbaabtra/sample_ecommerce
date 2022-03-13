# Generated by Django 4.0.3 on 2022-03-11 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='ordered', max_length=10),
        ),
    ]
