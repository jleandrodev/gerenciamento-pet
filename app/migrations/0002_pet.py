# Generated by Django 5.0 on 2023-12-27 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nascimento', models.DateField()),
                ('categoria', models.CharField(choices=[('ca', 'Cachorro'), ('ga', 'Gato'), ('co', 'Coelho'), ('ta', 'Tartaruga'), ('pa', 'Pássaro')], max_length=2)),
                ('cor', models.CharField(choices=[('pr', 'Preto'), ('br', 'Branco'), ('ci', 'Cinza'), ('ma', 'Marrom')], max_length=2)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
    ]
