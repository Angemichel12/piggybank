from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import(CurrencyModelViewSet, 
                   CategoryModelViewSet,
                   TransactionModelViewSet,
                   TransactionReportAPIView) 
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'categories', CategoryModelViewSet, basename='category')
router.register(r'transactions', TransactionModelViewSet, basename='transaction')
router.register(r'currencies', CurrencyModelViewSet, basename='currency')

urlpatterns = [
    path('login/', obtain_auth_token, name='obtain-auth-token'),
    path('report/', TransactionReportAPIView.as_view())
]+router.urls
