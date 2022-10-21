from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from core.api.serializers import PaymentsSerializer, RequestSerializer
from core.models import (
    Payments,
    Supplier,
    Request,
)

User = get_user_model()


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
