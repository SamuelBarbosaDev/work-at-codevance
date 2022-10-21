from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import (
    Supplier,
    Payments,
    Request,
)
User = get_user_model()


class PaymentsSerializer(serializers.ModelSerializer):
    # supplier = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Payments
        fields = [
            "request_status", "date_of_issue",
            "expiration_date", "original_value",
            "supplier",
        ]
        depth = 1


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ["requests", ]
