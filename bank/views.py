from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from django.contrib.auth.decorators import login_required


# Create your views here.
from bank.forms.form_bank import BanktForm
from bank.models import Bank

@login_required
def list_banks(request):
    banks = Bank.objects.all()
    return render(request, 'list_banks.html', locals())

@login_required
def add(request):
    if request.method == 'POST':
        form = BanktForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.add_message(
                request, SUCCESS,
                'Bank Saved!',
                extra_tags='alert alert-success'
            )
            return redirect('list_banks')
        else:
            messages.add_message(
                request, ERROR,
                'The bank can`t saved!',
                extra_tags='alert alert-danger'
            )
    else:
       form =  BanktForm()
    return render(request, 'form_bank.html', locals())

@login_required
def update(request, id_bank):
    instance = get_object_or_404(Bank, id=id_bank)
    form = BanktForm(instance=instance)
    if request.method == 'POST':
        form = BanktForm(request.POST, instance=instance)
        if form.is_valid():
            form = form.save()
            messages.add_message(
                request, SUCCESS,
                'Bank Saved!',
                extra_tags='alert alert-success'
            )
            return redirect('list_banks')
        else:
            messages.add_message(
                request, ERROR,
                'The bank can`t be saved!',
                extra_tags='alert alert-danger'
            )

    return render(request, 'form_bank.html', locals())
