# Generated by Django 3.2.19 on 2023-08-24 22:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_alter_productmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 25, 2, 16, 10, 843613), verbose_name='Date'),
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2023, 8, 25, 2, 16, 10, 844460), verbose_name='Date')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
