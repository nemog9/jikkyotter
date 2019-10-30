# Generated by Django 2.2.6 on 2019-10-30 05:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jikkyotter', '0009_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 30, 5, 9, 11, 336386, tzinfo=utc), verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 30, 5, 9, 11, 336325, tzinfo=utc), verbose_name='開始日時'),
        ),
    ]
