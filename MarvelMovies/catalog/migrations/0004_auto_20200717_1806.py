# Generated by Django 2.2.5 on 2020-07-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_movieinstance_imprint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'get_latest_by': 'date'},
        ),
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.ManyToManyField(to='catalog.Language'),
        ),
    ]
