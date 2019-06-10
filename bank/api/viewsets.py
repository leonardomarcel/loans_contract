from .serializers import BankSerializer
from bank.models import Bank
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated

class BankViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Bank.objects.all()
    serializer_class = BankSerializer