# Generated by Django 2.2.3 on 2021-04-02 12:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contentManagement', '0012_auto_20210401_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 51, 12, 207928, tzinfo=utc), null=True),
        ),
    ]
