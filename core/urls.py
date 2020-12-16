
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from core.views import list_contracts, add, update
from core.api.viewsets import ContractViewSet

urlpatterns = [
    #url(r'contracts/$', ContractViewSet, name='list_contracts'),
    #url(r'contract/(?P<id_contract>\d+)/$', ContractViewSet, name='list_contracts'),
    #url(r'contract/add/$', add, name='add_contract'),
    #url(r'contract/update/(?P<id_contract>\d+)/$', update, name='update_contract'),


]


