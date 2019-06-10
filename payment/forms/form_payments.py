from django import forms
from core.models import Contract
from payment.models import Payment
from core.models import Contract

class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['contract'].widget.attrs['class']='form-control'
        self.fields['contract'].queryset=Contract.objects.filter(created_user=user)
        self.fields['payment_date'].widget.attrs['class'] = 'form-control'
        self.fields['payment_value'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Payment
        fields = "__all__"