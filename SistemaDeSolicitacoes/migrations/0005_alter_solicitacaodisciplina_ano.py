# Generated by Django 4.1.1 on 2022-09-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaDeSolicitacoes', '0004_alter_solicitacaodisciplina_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacaodisciplina',
            name='ano',
            field=models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=4),
        ),
    ]