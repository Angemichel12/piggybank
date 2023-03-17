from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Currency, Category, Transaction
from .serializers import CurrencySerializer, CategorySerializer,  WriteTransactionSerializer, ReadTransactionSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

class CurrencyListAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionModelViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.select_related('currency', 'Category')
    filter_backends = (SearchFilter,OrderingFilter, DjangoFilterBackend)
    search_fields = ('description',)
    ordering_fields = ('amount', 'date')
    filterset_fields = ('currency__code',)
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
