# Generated by Django 4.1.1 on 2022-10-21 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaDeSolicitacoes', '0015_rename_disciplina_mensagemcurso_solicitacao_curso_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitacaocurso',
            old_name='assessoria_comunicacao',
            new_name='acessoria_comunicacao',
        ),
    ]
