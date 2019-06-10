"""loans_contracts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls import url
from rest_framework.authtoken import views
from auth_local.views import index, login, logout
from core import urls


from rest_framework import  routers


from bank.api.viewsets import BankViewSet
from core.api.viewsets import ContractViewSet
from customer.api.viewsets import CustomerViewSet
from payment.api.viewsets import PaymentViewSet


router = routers.DefaultRouter()
router.register(r'contracts', ContractViewSet, base_name='Contract')
router.register(r'banks', BankViewSet)
router.register(r'customers', CustomerViewSet)
#router.register(r'payments', PaymentViewSet)






urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),

    url('^payments/(?P<id_contract>.+)/$', PaymentViewSet.as_view()),

    url(r'^$', index, name='index'),

    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),

    url(r'core/', include('core.urls')),
    url(r'bank/', include('bank.urls')),
    url(r'payment/', include('payment.urls')),
    url(r'customer/', include('customer.urls')),

]
