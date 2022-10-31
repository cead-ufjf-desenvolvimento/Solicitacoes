# Generated by Django 4.1.1 on 2022-09-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaDeSolicitacoes', '0010_alter_servicoaudiovisual_breve_descricao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoAudiovisual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_responsavel', models.CharField(max_length=255, verbose_name='Professor Responsável')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(blank=True, max_length=13, null=True)),
                ('data_gravacao', models.DateField(verbose_name='Data')),
                ('hora_gravacao', models.TimeField(verbose_name='Hora')),
                ('duracao', models.DurationField(blank=True, null=True, verbose_name='Duração esperada de uso do estúdio? (campo não obrigatório)')),
                ('setor_ou_curso', models.CharField(max_length=255, verbose_name='Setor/Curso')),
                ('breve_descricao', models.TextField(verbose_name='Breve descrição (no máximo 250 caracteres)')),
                ('equipamentos', models.CharField(max_length=255, verbose_name='De quais equipamentos irá precisar?')),
                ('equipe', models.CharField(choices=[('S', 'Sim, precisaremos da equipe do CEAD'), ('N', 'Não, iremos utilizar a nossa própria equipe')], max_length=1)),
                ('pessoas', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('data_abertura', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Aberto'), ('E', 'Em Andamento'), ('P', 'Pendente'), ('F', 'Fechado')], max_length=1)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ServicoAudiovisual',
        ),
    ]
