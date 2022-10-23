from django.urls import path
from core.views import (
    payments_list_view,
    history_list_view,
    request_status_redirect_view,
    requests_list_view,
    request_approved_redirect_view,
    envia_email,
)

app_name = "core"
urlpatterns = [
    path("history/", history_list_view, name="history"),
    path("payments/", payments_list_view, name="payments"),
    path("payments/request/<int:id>/", request_status_redirect_view, name='request'),
    path("requests/", requests_list_view, name='requests'),
    path("requests/<int:id>/<str:sp>/", request_approved_redirect_view, name='requests_approved'),
    path("email/", envia_email, name='envia_email'),
]