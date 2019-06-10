
from django.conf.urls import url

from bank.views import list_banks, add, update

urlpatterns = [
    url(r'banks/$', list_banks, name='list_banks'),
    url(r'bank/add/$', add, name='add_bank'),
    url(r'bank/update/(?P<id_bank>\d+)/$', update, name='update_bank'),
]


