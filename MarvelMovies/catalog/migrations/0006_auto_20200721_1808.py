# Generated by Django 2.2.5 on 2020-07-21 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200721_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieinstance',
            options={'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
