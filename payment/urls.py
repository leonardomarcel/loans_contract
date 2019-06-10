
from django.conf.urls import url

from payment.views import list_payments, add, update

urlpatterns = [
    url(r'payments/(?P<id_contract>\d+)/$', list_payments, name='list_payments'),
    url(r'payment/add/$', add, name='add_payment'),
    url(r'payment/update/(?P<id_payment>\d+)/$', update, name='update_payment'),
]


