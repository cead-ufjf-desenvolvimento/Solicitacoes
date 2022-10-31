# Generated by Django 4.1.1 on 2022-09-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaDeSolicitacoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('autor', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='solicitacaocurso',
            name='mensagens',
            field=models.ManyToManyField(to='SistemaDeSolicitacoes.mensagem'),
        ),
        migrations.AddField(
            model_name='solicitacaodisciplina',
            name='mensagens',
            field=models.ManyToManyField(to='SistemaDeSolicitacoes.mensagem'),
        ),
    ]