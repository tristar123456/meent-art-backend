# Generated by Django 2.2.3 on 2021-04-02 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0022_auto_20210401_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 12, 51, 12, 208533), null=True),
        ),
    ]