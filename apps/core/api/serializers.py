from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import (
    Supplier,
    Payments,
    Request,
)
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            "username", "email",
        ]


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = [
            "corporate_name", "cnpj",
            "user",
        ]


class PaymentsSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(required=False)

    class Meta:
        model = Payments
        fields = [
            'user',
            "request_status", "date_of_issue",
            "expiration_date", "original_value",
            "supplier", 
        ]


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ["requests", 'payments']
