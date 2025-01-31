# Generated by Django 3.2.16 on 2022-10-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_payments_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='request_status',
            field=models.CharField(blank=True, choices=[('I', 'Indisponível'), ('D', 'Disponível'), ('AC', 'Aguardando confirmação'), ('A', 'Antecipado'), ('N', 'Negado')], default='Disponível', max_length=30, null=True, verbose_name='Status da Solicitação'),
        ),
    ]
