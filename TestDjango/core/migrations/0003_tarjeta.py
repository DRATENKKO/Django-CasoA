# Generated by Django 4.0.1 on 2022-05-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_vehiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('numeroTarjeta', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('expiracion', models.DateField()),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]
