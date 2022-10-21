from django.urls import path
from django.views.generic import TemplateView
# from core.api.views import (
#     payments_view_set,
#     request_view_Set,
# )

app_name = "core"
urlpatterns = [
    path("history/", TemplateView.as_view(template_name="core/pages/history.html"), name="history"),
    path("payments/", TemplateView.as_view(template_name="core/pages/payments.html"), name="payments"),

]