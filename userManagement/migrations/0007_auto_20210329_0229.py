# Generated by Django 2.2.3 on 2021-03-29 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0006_auto_20210329_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 2, 29, 47, 616066), null=True),
        ),
    ]
