from rest_framework import serializers
from .models import Currency, Category, Transaction


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'code')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class WriteTransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field='code', queryset=Currency.objects.all())
    class Meta:
        model = Transaction
        fields = ('amount','currency','date','description','Category')

class ReadTransactionSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    Category = CategorySerializer()
    class Meta:
        model = Transaction
        fields = "__all__"

        read_only_fields = tuple(fields)