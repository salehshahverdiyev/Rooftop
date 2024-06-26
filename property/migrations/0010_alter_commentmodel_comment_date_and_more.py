# Generated by Django 4.2.4 on 2023-08-25 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_commentreplymodel_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 3, 55, 45, 635767), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='commentreplymodel',
            name='reply_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 3, 55, 45, 636247), verbose_name='Reply date'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 3, 55, 45, 634943), verbose_name='Date'),
        ),
    ]
