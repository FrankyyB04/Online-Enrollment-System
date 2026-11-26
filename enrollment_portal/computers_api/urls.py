from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ComputerProductViewSet

router = DefaultRouter()
router.register(r"products", ComputerProductViewSet, basename="computer-product")

urlpatterns = [
    path("", include(router.urls)),
]
