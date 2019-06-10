from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from django.template  import RequestContext

# Create your views here.
from customer.forms.form_customer import CustomerForm
from customer.models import Customer


def list_customers(request):

    customers = Customer.objects.all()
    return render(request, 'list_customers.html', locals())

def add(request, id_contract=None):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.add_message(
                request, SUCCESS,
                'Customer Saved!',
                extra_tags='alert alert-success'
            )
            return redirect('list_customers')
        else:
            messages.add_message(
                request, ERROR,
                'The customer can`t saved!',
                extra_tags='alert alert-danger'
            )
    else:
       form =  CustomerForm()
    return render(request, 'form_customer.html', locals())


def update(request, id_contract):
    instance = get_object_or_404(Customer, id=id_contract)
    form = CustomerForm(instance=instance)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=instance)
        if form.is_valid():
            form = form.save()
            messages.add_message(
                request, SUCCESS,
                'Customer Saved!',
                extra_tags='alert alert-success'
            )
            return redirect('list_customers')
        else:
            messages.add_message(
                request, ERROR,
                'The customer can`t saved!',
                extra_tags='alert alert-danger'
            )

    return render(request, 'form_customer.html', locals())


