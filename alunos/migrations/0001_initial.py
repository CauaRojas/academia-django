# Generated by Django 4.1 on 2022-11-08 00:04

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_nascimento', models.DateTimeField()),
                ('data_vencimento_matricula', models.DateTimeField(default=datetime.datetime(2022, 12, 8, 0, 4, 13, 530972, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
