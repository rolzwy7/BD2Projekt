# Generated by Django 2.2 on 2019-12-06 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Laborant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32, verbose_name='Imie')),
                ('nazwisko', models.CharField(max_length=32, verbose_name='Nazwisko')),
                ('role', models.CharField(default='LABORANT', editable=False, max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KierownikLabarotorium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32, verbose_name='Imie')),
                ('nazwisko', models.CharField(max_length=32, verbose_name='Nazwisko')),
                ('role', models.CharField(default='KIERLAB', editable=False, max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
