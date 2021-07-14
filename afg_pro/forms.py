from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreatingUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class Order_Form(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class Create_Form(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']



class addNewProduct(ModelForm):
    class Meta:
        model = MyProduct
        fields = '__all__'

class Cust_profile_form(ModelForm):
    class Meta:
        model = MyCustomer 
        fields = '__all__'
        excluds = ['user']