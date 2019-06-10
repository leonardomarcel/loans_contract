from django.db import models

# Create your models here.
from core.models import Contract


class Payment(models.Model):
    contract        = models.ForeignKey(Contract, on_delete='cascade')
    payment_date    = models.DateTimeField()
    payment_value   = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.contract)
