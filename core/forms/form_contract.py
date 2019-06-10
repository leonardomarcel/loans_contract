from django import forms
from core.models import Contract

class ContractForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.fields['initial_value'].widget.attrs['class'] = 'form-control'
        self.fields['interest_rate'].widget.attrs['class'] = 'form-control'
        self.fields['ip_address'].widget.attrs['class'] = 'form-control'
        self.fields['submission_date'].widget.attrs['class'] = 'form-control'
        self.fields['bank'].widget.attrs['class'] = 'form-control'
        self.fields['customer'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contract
        exclude = ['actual_value', 'created_user', ]