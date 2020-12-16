

from .serializers import ContractSerializer
from core.models import Contract
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

#from rest_framework.authentication import TokenAuthentication




class ContractViewSet(viewsets.ModelViewSet):

    #authentication_classes = (TokenAuthentication, )
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    queryset = Contract.objects.filter()
    serializer_class = ContractSerializer

    


