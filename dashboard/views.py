from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SelectCustomerForm

@login_required
def index(request):
    return render(request, 'dashboard/index.html')


def customer_form(request):
    form = SelectCustomerForm
    context = {'form':form}
    return render(request, 'customer/home.html', context)


# Create your views here.
