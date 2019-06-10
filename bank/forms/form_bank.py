from django import forms

from bank.models import Bank

class BanktForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BanktForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class']='form-control'


    class Meta:
        model = Bank
        fields = "__all__"