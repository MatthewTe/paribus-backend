from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Account, AccountTransactions
from .serializers import AccountSerializer, AccountTransactionsSerializer

# Processing GET request endpoint for accounts:
@api_view(["GET"])
def get_account_data(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

# Processing GET request endpoint for account transactions:
@api_view(["GET"])
def get_accounts_transaction_data(request):
    if request.method == "GET":
        transactions = AccountTransactions.objects.all()
        serializer = AccountTransactionsSerializer(transactions, many=True)
        return Response(serializer.data)