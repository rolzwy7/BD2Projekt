# Generated by Django 2.2.6 on 2020-01-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('przychodnia_wizyta', '0002_wizyta_dt_rej_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wizyta',
            name='dt_rej_2',
        ),
        migrations.AlterField(
            model_name='wizyta',
            name='dt_rej',
            field=models.DateTimeField(),
        ),
    ]
