from django.shortcuts import render, redirect, get_object_or_404
from . models import Transaction
import uuid
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from django.contrib.auth.models import User
from user.models import Profile
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from io import BytesIO

@login_required
def index(request):
    #transaction = Transaction.objects.all()
    user_object = User.objects.get(username=request.user.username)
    #user_profil = Transaction.objects.get(select=user_object)
    user_profile = Transaction.objects.filter(select=user_object)
   
    context = {'user_profile': user_profile,}
    return render(request, 'dashboard/index.html', context)

# class CustomerListView(ListView):
#     model = Transaction
#     template_name = 'customer/Receipt.html'


def generate_receipt(request,):
     #transaction = Transaction.objects.all()
    user_object_pdf = User.objects.get(username=request.user.username)
    #user_profil = Transaction.objects.get(select=user_object)
    user_profile_pdf = Transaction.objects.filter(select=user_object_pdf)
    template_path = 'dashboard/Receipt.html'
    context = {'user_profile_pdf': user_profile_pdf}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, )
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    
def get(request):
    transaction = Transaction.objects.all()
    sum = 0
    total = sum + Transaction.Amount
    context = {'transaction':transaction, 'total': total}


    return render(request,'dashboard/index.html',context )


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

def landing(request):
    return render(request, 'customer/landing-page.html')


# def render_pdf_view(request):
#     template_path = 'dashboard/Receipt.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     #if download:
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     #if display
#     response['Content-Disposition'] = ' filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response, )
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response

# Create y:our views here.
