# Generated by Django 3.2.19 on 2023-08-24 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_campaignmodel_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignmodel',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 16, 41, 15, 920314), verbose_name='Start date'),
        ),
    ]
