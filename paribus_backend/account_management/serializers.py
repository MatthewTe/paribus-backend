from rest_framework import serializers
from .models import Account, AccountTransactions

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'account_name', 'account_value')

class AccountTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTransactions
        fields = ('transaction_id', 'account', 'date', 'transaction_value', 'transaction_description', 'current_account_value')