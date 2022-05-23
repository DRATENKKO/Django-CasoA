# Generated by Django 4.0.1 on 2022-05-23 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(blank=True, max_length=20, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
