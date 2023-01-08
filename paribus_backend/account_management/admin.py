from django.contrib import admin
from account_management.models import Account, AccountTransactions

admin.site.register(Account)
admin.site.register(AccountTransactions)