# Generated by Django 3.2 on 2021-04-07 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentManagement', '0018_auto_20210403_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
    ]
