# Generated by Django 3.1 on 2020-09-03 06:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200903_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 3, 6, 16, 20, 486484, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
