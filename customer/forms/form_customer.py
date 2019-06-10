from django import forms
from customer.models import Customer


class CustomerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Customer
        fields = "__all__"