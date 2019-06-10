from .serializers import PaymentSerializer
from payment.models import Payment
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class PaymentViewSet(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):

        user = self.request.user
        contract = self.kwargs['id_contract']


        return Payment.objects.filter(contract__created_user=user, contract__pk=contract)