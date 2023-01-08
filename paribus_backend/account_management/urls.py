from django.urls import path
from account_management import views 

urlpatterns = [

    path("accounts/", views.get_account_data, name="get_accounts_data"),
    path("transactions/", views.get_accounts_transaction_data, name="get_account_transactions")

]