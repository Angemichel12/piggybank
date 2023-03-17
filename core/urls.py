from django.urls import path

from .views import(CurrencyListAPIView, 
                   CategoryModelViewSet,
                   TransactionModelViewSet) 
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'categories', CategoryModelViewSet, basename='category')
router.register(r'transactions', TransactionModelViewSet, basename='transaction')

urlpatterns = [
    path('currencies/', CurrencyListAPIView.as_view())
]+router.urls
