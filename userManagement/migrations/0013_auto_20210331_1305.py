# Generated by Django 2.2.3 on 2021-03-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0012_auto_20210329_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
