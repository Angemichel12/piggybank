from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Currency, Category, Transaction
from .serializers import (CurrencySerializer, 
                          CategorySerializer,  
                          WriteTransactionSerializer, 
                          ReadTransactionSerializer,
                          ReportEntrySerializer)
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from rest_framework.views import APIView
from .reports import transactions_reports
from rest_framework.response import Response



class CurrencyListAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pegination_class = None


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class TransactionModelViewSet(viewsets.ModelViewSet):
    filter_backends = (SearchFilter,OrderingFilter, DjangoFilterBackend)
    search_fields = ('description',)
    ordering_fields = ('amount', 'date')
    filterset_fields = ('currency__code',)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Transaction.objects.select_related('currency', 'Category', 'user').filter(user=self.request.user)
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
class TransactionReportAPIView(APIView):
    def get(self, request):
        data = transactions_reports()
        serializer = ReportEntrySerializer(instance=data, many=True).data
        return Response(data=serializer)

