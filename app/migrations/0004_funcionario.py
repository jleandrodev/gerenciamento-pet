# Generated by Django 5.0 on 2023-12-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_consultapet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nascimento', models.DateField()),
                ('cargo', models.CharField(choices=[(1, 'Atendente'), (2, 'Gerente')], max_length=1)),
            ],
        ),
    ]