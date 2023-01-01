from django.urls import path
from core_company_data import views 

urlpatterns = [
    path('price-data/', views.get_price_data, name='get_price_data'),
    path('price-data/create/', views.create_price_data, name='create_price_data')
]