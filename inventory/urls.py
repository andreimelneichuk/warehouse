from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import StockViewSet, CategoryViewSet, EquipmentViewSet

router = DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'equipment', EquipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]