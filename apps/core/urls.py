from django.urls import path
from django.views.generic import TemplateView
from core.views import (
    payments_list_view,
    history_list_view,
    request_status_redirect_view,
)

app_name = "core"
urlpatterns = [
    path("history/", history_list_view, name="history"),
    path("payments/", payments_list_view, name="payments"),
    path("payments/request/<int:id>", request_status_redirect_view, name='request')
]