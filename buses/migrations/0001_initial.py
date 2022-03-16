# Generated by Django 3.2.3 on 2021-11-04 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aparcaderos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=150)),
                ('hora_salida', models.DateTimeField()),
                ('hora_llegada', models.DateTimeField()),
                ('llegada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buses_llegada', to='aparcaderos.aparcaderos')),
                ('origen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buses_origen', to='aparcaderos.aparcaderos')),
            ],
        ),
    ]