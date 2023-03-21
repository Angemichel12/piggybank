from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import(CurrencyListAPIView, 
                   CategoryModelViewSet,
                   TransactionModelViewSet,
                   TransactionReportAPIView) 
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'categories', CategoryModelViewSet, basename='category')
router.register(r'transactions', TransactionModelViewSet, basename='transaction')

urlpatterns = [
    path('login/', obtain_auth_token, name='obtain-auth-token'),
    path('currencies/', CurrencyListAPIView.as_view()),
    path('report/', TransactionReportAPIView.as_view())
]+router.urls
