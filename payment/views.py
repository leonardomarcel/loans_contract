from decimal import Decimal

from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR


# Create your views here.
from payment.forms.form_payments import PaymentForm

from core.models import Contract
from payment.models import Payment

@login_required
def list_payments(request, id_contract):

    contract = get_object_or_404(Contract, id=id_contract)
    if contract.created_user  == request.user:
        payments = Payment.objects.filter(contract=id_contract)
    else:
        return redirect ('index')
    return render(request, 'list_payments.html', locals())

@login_required
def add(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, user=request.user)
        if form.is_valid():
            form = form.save()
            contract = Contract.objects.get(pk=form.contract.id)
            actual_value = Decimal(contract.amount()) - form.payment_value
            contract.actual_value = actual_value
            contract.save()
            return redirect('list_payments', id_contract=contract.id)

    else:
       form =  PaymentForm(user=request.user)
    return render(request, 'form_payment.html', locals())

@login_required
def update(request, id_payment):
    instance = get_object_or_404(Payment, id=id_payment)
    form = PaymentForm(instance=instance, user=request.user)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=instance, user=request.user)
        if form.is_valid():
            form = form.save()
            contract = Contract.objects.get(pk=form.contract.id)
            actual_value = Decimal(contract.amount()) - form.payment_value
            contract.actual_value = actual_value
            contract.save()

            return redirect('list_payments', id_contract=contract.id)


    return render(request, 'form_payment.html', locals())




