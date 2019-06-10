
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from core.views import list_contracts, add, update

urlpatterns = [
    url(r'contracts/$', list_contracts, name='list_contracts'),
    url(r'contract/add/$', add, name='add_contract'),
    url(r'contract/update/(?P<id_contract>\d+)/$', update, name='update_contract'),


]


