from bank.models import Bank
from rest_framework.serializers import ModelSerializer

class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'