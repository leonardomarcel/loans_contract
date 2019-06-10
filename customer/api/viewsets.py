from .serializers import CustomerSerializer
from customer.models import Customer
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer