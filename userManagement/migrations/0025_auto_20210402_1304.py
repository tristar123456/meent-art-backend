# Generated by Django 2.2.3 on 2021-04-02 13:04

from django.db import migrations, models
import userManagement.models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0024_auto_20210402_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='date',
            field=models.DateTimeField(default=userManagement.models.return_date_time, null=True),
        ),
    ]
