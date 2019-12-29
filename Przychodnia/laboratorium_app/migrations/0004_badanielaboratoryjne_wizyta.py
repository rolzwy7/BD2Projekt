# Generated by Django 2.1 on 2019-12-29 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('przychodnia_wizyta', '0004_auto_20191228_1420'),
        ('laboratorium_app', '0003_auto_20191228_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='badanielaboratoryjne',
            name='wizyta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='przychodnia_wizyta.Wizyta'),
            preserve_default=False,
        ),
    ]