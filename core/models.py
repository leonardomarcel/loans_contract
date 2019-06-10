from django.db import models
from django.conf import settings
from bank.models import Bank
import datetime
from customer.models import Customer


class Contract(models.Model):
    initial_value   = models.DecimalField(decimal_places=2, max_digits=10)
    actual_value    = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    interest_rate   = models.DecimalField(decimal_places=2, max_digits=10)
    ip_address      = models.CharField(max_length=40)
    submission_date = models.DateField()
    bank            = models.ForeignKey(Bank, on_delete=models.CASCADE)
    customer        = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


    # Formula Juros compostos: amaount = Value(1 +  interest_rate)ˆqtd_mes
    def amount(self):
        interest_rate = self.interest_rate / 100
        hoje = datetime.date.today()
        qtd_mes = hoje.month - self.submission_date.month
        amount = self.actual_value * (1 + interest_rate)**qtd_mes
        return("%.2f" % amount)
