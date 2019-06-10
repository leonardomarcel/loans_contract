from customer.models import Customer
from rest_framework.serializers import ModelSerializer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'