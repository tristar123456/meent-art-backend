# Generated by Django 2.2.3 on 2021-04-01 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0017_auto_20210401_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 2, 15, 5, 23, 428305), null=True),
        ),
    ]
