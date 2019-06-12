from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from django.contrib.auth.decorators import login_required

from django.template  import RequestContext

# Create your views here.
from core.forms.form_contract import ContractForm
from core.models import Contract

@login_required
def list_contracts(request):
    contracts = Contract.objects.filter(created_user=request.user.id)
    return render(request, 'list_contracts.html', locals())

@login_required
def add(request, id_contract=None):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.actual_value = form.initial_value
            form.created_user = request.user
            form.save()
            messages.add_message(
                request, SUCCESS,
                'Contract Saved!',
                extra_tags='alert alert-success'
            )
            return redirect('list_contracts')
        else:
            messages.add_message(
                request, ERROR,
                'The contract can`t saved!',
                extra_tags='alert alert-danger'
            )
    else:
       form =  ContractForm()
    return render(request, 'form_contract.html', locals())

@login_required
def update(request, id_contract):
    instance = get_object_or_404(Contract, id=id_contract)
    form = ContractForm(instance=instance)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=instance)
        if form.is_valid():
            form = form.save()
            messages.add_message(
                request, SUCCESS,
                'Contract Saved!',
                extra_tags='alert alert-success'
            )
            return redirect('list_contracts')
        else:
            messages.add_message(
                request, ERROR,
                'The contract can`t saved!',
                extra_tags='alert alert-danger'
            )

    return render(request, 'form_contract.html', locals())




