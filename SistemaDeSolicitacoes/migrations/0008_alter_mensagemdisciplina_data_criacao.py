# Generated by Django 4.1.1 on 2022-09-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaDeSolicitacoes', '0007_mensagemdisciplina_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagemdisciplina',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
