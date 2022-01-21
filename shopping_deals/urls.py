"""shopping_deals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from deals.views import CreateDeal, UpdateDeal, EndDeal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_deal/', CreateDeal.as_view(), name="create deal"),
    path('update_deal/', UpdateDeal.as_view(), name="create deal"),
    path('end_deal/', EndDeal.as_view(), name="create deal"),
]
