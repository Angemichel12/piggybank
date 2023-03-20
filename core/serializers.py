from rest_framework import serializers
from .models import Currency, Category, Transaction
from django.contrib.auth.models import User


class ReodOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name')
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'code')

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Category
        fields = ('id', 'name', 'user')

class WriteTransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    currency = serializers.SlugRelatedField(slug_field='code', queryset=Currency.objects.all())
    class Meta:
        model = Transaction
        fields = ('user','amount','currency','date','description','category')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        self.fields["category"].queryset = user.categories.all()

class ReadTransactionSerializer(serializers.ModelSerializer):
    user = ReodOnlyUserSerializer()
    currency = CurrencySerializer()
    category = CategorySerializer()
    class Meta:
        model = Transaction
        fields = "__all__"

        read_only_fields = tuple(fields)