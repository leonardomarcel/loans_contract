from django.conf.urls import url

from customer.views import list_customers, add, update

urlpatterns = [
    url(r'customers/$', list_customers, name='list_customers'),
    url(r'customer/add/$', add, name='add_customer'),
    url(r'customer/update/(?P<id_contract>\d+)/$', update, name='update_customer'),
]
