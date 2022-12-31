from django.shortcuts import render, redirect
from . models import Transaction
import uuid
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm

@login_required
def index(request):
    transaction = Transaction.objects.all()
    context = {'transaction': transaction}
    return render(request, 'dashboard/index.html', context)

# def get(request):
#     transaction = Transaction.objects.all()
#     context = {'transaction':transaction}

#     return render(request,'dashboard/index.html',context )

def home(request):
   

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form':form}
            return render(request, 'customer/home.html', context )
    else:
        form = TransactionForm
        context = {'form':form}
        return render(request, 'customer/home.html', context )

    
    # def save(self, commit=True):
    #     form = super().save(commit=False)
    #     if not form.pk:
    #         # Generate a new reference code if the form is being created for the first time
    #         form.reference_code = uuid.uuid4().hex

    #     if commit:
    #         form.save()
    #     return form


# Create your views here.
