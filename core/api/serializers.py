from core.models import Contract
from rest_framework.serializers import ModelSerializer

class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ('pk', 'customer', 'initial_value', 'actual_value', 'amount', 'bank', 'interest_rate', 'submission_date', 'ip_address')


