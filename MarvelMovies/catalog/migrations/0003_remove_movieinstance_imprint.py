# Generated by Django 2.2.5 on 2020-07-15 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200713_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieinstance',
            name='imprint',
        ),
    ]
