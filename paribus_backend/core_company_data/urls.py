from django.urls import path
from core_company_data import views 

urlpatterns = [
    path('price-data/', views.get_price_data, name='get_price_data'),
    path('price-data/create/', views.create_price_data, name='create_price_data'),

    path('ping-microservice', views.ping_microservice, name='ping_microservice'),
    path('make-stock-price-request-microservice', views.write_stock_price_data, name="make_stock_price_microservice_request")
    
]