# Generated by Django 2.2.8 on 2019-12-30 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('przychodnia_wizyta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laborant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32, verbose_name='Imię')),
                ('nazwisko', models.CharField(max_length=32, verbose_name='Nazwisko')),
                ('role', models.CharField(default='LABORANT', editable=False, max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Laboranci',
            },
        ),
        migrations.CreateModel(
            name='KierownikLabarotorium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32, verbose_name='Imię')),
                ('nazwisko', models.CharField(max_length=32, verbose_name='Nazwisko')),
                ('role', models.CharField(default='KIERLAB', editable=False, max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Kierownicy Laboratorium',
            },
        ),
        migrations.CreateModel(
            name='BadanieLaboratoryjne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ZLE', 'Zlecone'), ('WYK', 'Wykonane'), ('ANUL_LAB', 'Anulowane przez Laboranta'), ('ZATW', 'Zatwierdzone'), ('ANUL_KLAB', 'Anulowane przez Kier. Laboratorium')], default='ZLE', max_length=9)),
                ('uwagi_lekarza', models.TextField(blank=True, null=True)),
                ('dt_zlecenia', models.DateTimeField(auto_now_add=True)),
                ('wynik', models.TextField()),
                ('dt_wyk_anul_lab', models.DateTimeField(null=True)),
                ('dt_zatw_anul_klab', models.DateTimeField(null=True)),
                ('uwagi_kierownika', models.TextField(blank=True, null=True)),
                ('kier_lab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laboratorium_app.KierownikLabarotorium')),
                ('laborant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laboratorium_app.Laborant')),
                ('slownik', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.SlownikBadan')),
                ('wizyta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='przychodnia_wizyta.Wizyta')),
            ],
            options={
                'verbose_name_plural': 'Badania Laboratoryjne',
            },
            managers=[
                ('badania', django.db.models.manager.Manager()),
            ],
        ),
    ]
