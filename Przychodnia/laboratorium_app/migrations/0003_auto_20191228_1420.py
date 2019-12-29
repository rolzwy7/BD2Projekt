# Generated by Django 2.1 on 2019-12-28 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_slownikbadan'),
        ('laboratorium_app', '0002_auto_20191217_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadanieLaboratoryjne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ZLE', 'Zlecone'), ('WYK', 'Wykonane'), ('ANUL_LAB', 'Anulowane przez Laboranta'), ('ZATW', 'Zatwierdzone'), ('ANUL_KLAB', 'Anulowane przez Kier. Laboratorium')], default='ZLE', max_length=9)),
                ('uwagi_lekarza', models.TextField(blank=True, null=True)),
                ('dt_zlecenia', models.DateTimeField(auto_now_add=True)),
                ('wynik', models.BooleanField(default=False)),
                ('dt_wyk_anul_lab', models.DateTimeField(null=True)),
                ('dt_zatw_anul_klab', models.DateTimeField(null=True)),
                ('uwagi_kierownika', models.TextField(blank=True, null=True)),
                ('slownik', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.SlownikBadan')),
            ],
            options={
                'verbose_name_plural': 'Badania Laboratoryjne',
            },
        ),
        migrations.AlterModelOptions(
            name='kierowniklabarotorium',
            options={'verbose_name_plural': 'Kierownicy Laboratorium'},
        ),
    ]