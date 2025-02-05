# Generated by Django 5.0.6 on 2024-05-24 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('capacity_unit', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': '"sample_schema"."car"',
            },
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('cars', models.ManyToManyField(related_name='garages', to='api.car')),
            ],
            options={
                'db_table': '"sample_schema"."garage"',
            },
        ),
        migrations.CreateModel(
            name='CarGarage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parked_at', models.DateTimeField(auto_now_add=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.car')),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.garage')),
            ],
            options={
                'db_table': '"sample_schema"."car_garage"',
                'unique_together': {('car', 'garage')},
            },
        ),
    ]
