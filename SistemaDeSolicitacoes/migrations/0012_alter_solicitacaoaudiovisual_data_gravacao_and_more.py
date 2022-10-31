# Generated by Django 4.1.1 on 2022-09-27 17:06

import SistemaDeSolicitacoes.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SistemaDeSolicitacoes', '0011_solicitacaoaudiovisual_delete_servicoaudiovisual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacaoaudiovisual',
            name='data_gravacao',
            field=models.DateField(validators=[SistemaDeSolicitacoes.validators.validate_is_future], verbose_name='Data da gravação'),
        ),
        migrations.AlterField(
            model_name='solicitacaoaudiovisual',
            name='hora_gravacao',
            field=models.TimeField(validators=[SistemaDeSolicitacoes.validators.validate_is_business_time], verbose_name='Horário da gravação'),
        ),
        migrations.AlterField(
            model_name='solicitacaoaudiovisual',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]