from django.contrib import admin
from django.urls import path, include
from .view import ping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # Status/Uptime ping view:
    path("status_code/ping", ping, name="get_status"),

    path("company/", include("core_company_data.urls"))

]
