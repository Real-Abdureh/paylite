from django.shortcuts import render, redirect
from . models import Transaction
import uuid
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from django.contrib.auth.models import User
from user.models import Profile

@login_required
def index(request):
    #transaction = Transaction.objects.all()
    user_object = User.objects.get(username=request.user.username)
    #user_profil = Transaction.objects.get(select=user_object)
    user_profile = Transaction.objects.filter(select=user_object)
   
    context = {'user_profile': user_profile,}
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

            return render(request, 'customer/pay.html', context, )
            
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
def pay(request):
    return render(request, 'customer/pay.html')

# Create y:our views here.
