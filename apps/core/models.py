from django.db import models
from djmoney.models.fields import MoneyField
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.contrib.auth import get_user_model
# Create your models here.

REQUESTS = (
    ('S', 'Solicitado'),
    ('A', 'Aprovado'),
    ('N', 'Negado'),
)

ANTICIPATION_REQUESTS = (
    ('I', 'Indisponível'), 
    ('D', 'Disponível'), 
    ('AC', 'Aguardando confirmação'), 
    ('A', 'Antecipado'), 
    ('N', 'Negado'),
)

class Supplier(models.Model):
    corporate_name = models.CharField(
        max_length=50, 
        blank=True, 
        null=True,
        verbose_name="Razão Social",
    )

    cnpj = CNPJField(
        masked=True,
        blank=True, 
        null=True,
        verbose_name="CNPJ",
    )

    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.corporate_name


class Payments(models.Model):
    id = models.BigAutoField(
        primary_key=True
        )

    request_status = models.CharField(
        max_length=30,
        choices=ANTICIPATION_REQUESTS,
        default = 'Disponível',
        blank=True, 
        null=True,
        verbose_name="Status da Solicitação",
    )

    date_of_issue = models.DateField(
        blank=True, 
        null=True,
        verbose_name="Data de Emissão",
    )

    expiration_date = models.DateField(
        blank=True, 
        null=True,
        verbose_name="Data de Vencimento",
    )

    original_value = MoneyField(
        max_digits=14, 
        decimal_places=2, 
        default_currency='BRL',
        default=00.00,
        blank=True, 
        null=True,
        verbose_name="Valor Original",
    )

    supplier = models.ForeignKey(
        Supplier,
        default=None,
        on_delete=models.CASCADE,
        verbose_name="Fornecedor",
    )

    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        expiration_date = str(self.expiration_date)
        return expiration_date


class Request(models.Model):
    payments = models.ForeignKey(
        Payments,
        default=None,
        on_delete=models.CASCADE,
        verbose_name="Pagamento",

    )

    requests = models.CharField(
        max_length=30,
        choices=REQUESTS,
        blank=True, 
        null=True,
        verbose_name="Antecipação de Pagamento",
    )

    def __str__(self):
        return self.requests


class Company(models.Model):
    corporate_name = models.CharField(
        max_length=50, 
        blank=True, 
        null=True,
        verbose_name="Razão Social",
    )

    cnpj = CNPJField(
        masked=True,
        blank=True, 
        null=True,
        verbose_name="CNPJ",
    )

    def __str__(self):
        return self.corporate_name