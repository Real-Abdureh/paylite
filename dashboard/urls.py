from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('home/',views.home, name='customer-home'),
    path('pay/', views.pay, name= 'customer-pay'  ),
    path('landing/', views.landing, name='landing-page'),
   
]