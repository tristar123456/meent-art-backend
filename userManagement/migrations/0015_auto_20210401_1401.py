# Generated by Django 2.2.3 on 2021-04-01 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0014_auto_20210331_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 2, 14, 1, 4, 576979), null=True),
        ),
    ]
