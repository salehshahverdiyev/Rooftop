# Generated by Django 3.2.19 on 2023-08-24 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogmodel_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 16, 41, 15, 922117), verbose_name='Tarix'),
        ),
    ]
