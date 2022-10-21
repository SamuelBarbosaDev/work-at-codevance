from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.users.api.views import UserViewSet
from core.api.views import PaymentsViewSet, RequestViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("payments", PaymentsViewSet)
router.register("requests", RequestViewSet)




app_name = "api"
urlpatterns = router.urls
