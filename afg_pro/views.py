from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from .forms import *
from django.contrib import messages
from django.conf import settings
from .models import *

# --------------------------------------------------------------------------------
# Admin/ Superuser Access Area

@login_required(login_url='afg_pro:login')
@permission_required('afg_pro:', login_url='afg_pro:home')
def dashboard(request):
    customers = MyCustomer.objects.all()
    orders = Order.objects.all()
    customers_total = customers.count()
    orders_total = orders.count()
    pending_orders = orders.filter(status="pending").count()
    delivered_orders = orders.filter(status="Delivered").count()
    Out_for_delivery_orders = orders.filter(status="Out for delivery").count()
    context = {
        'orders': orders,
        'customers': customers,
        'customers_total': customers_total,
        'orders_total': orders_total, 
        'pending_orders': pending_orders,
        'Out_for_delivery_orders': Out_for_delivery_orders,
        'delivered_orders': delivered_orders,      

    }
    return render(request, 'afg_pro/dashboard.html', context)

def MyProducts(request):
    products = MyProduct.objects.all()

    context = {'products': products}
    return render(request, 'afg_pro/products.html', context)


def Add_New_Product(request):
    product = MyProduct.objects.all()
    form = addNewProduct()
    if request.method == "POST":
        form = addNewProduct(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('afg_pro:dashboard'))
    
    context = { 'form': form}
    return render(request, 'afg_pro/add_new_product.html', context)

def delete_products(request, pro_id):
    product = get_object_or_404(MyProduct, pk=pro_id) 
    product.delete()

    return redirect('/products')

def edit_products(request, pk):
    product = MyProduct.objects.get(id=pk)
    form = addNewProduct(instance= product)

    if request.method == "POST":
        form = addNewProduct(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('/products')

    context = {
        'form': form
    }
   
    return render(request, 'afg_pro/edit_product.html', context)


def EachCustOrders_View(request, cust_id):
    customer = MyCustomer.objects.get(pk=cust_id)
    orders = customer.order_set.all()
    orders_total = orders.count()
    context = {
        'customer': customer, 
        'orders': orders,
        'orders_total': orders_total
    }
    return render(request, 'afg_pro/single_user_view.html', context)


def delete_orders(request, order_id):
    # order = Order.objects.get(id=pk)
    order= get_object_or_404(Order, pk=order_id) 

    order.delete()

    return HttpResponseRedirect(reverse('afg_pro:dashboard'))


def edit_orders(request, pk):
    order = Order.objects.get(id=pk)
    form = Order_Form(instance=order)
    
    if request.method == "POST":
        form = Order_Form(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('afg_pro:dashboard'))
           
    context = {
        'form': form
    }
   
    return render(request, 'afg_pro/edit_order.html', context)

# ----------------------------------------------------------------------------#
# Customer_access Area

def home(request): 
    product = MyProduct.objects.all().order_by('id')
    print(product)
    context = {'product': product}
    return render(request, 'afg_pro/home.html', context)


@login_required(login_url='afg_pro:login')
def profile(request, pk):
    customer = MyCustomer.objects.get(id=pk)
    print(request.user.id)
    orders = customer.order_set.all()
    context = {'orders': orders, 'customer':customer,}
    return render(request, 'afg_pro/customer_profile.html', context)
    

@login_required(login_url='afg_pro:login')
def profile_setting(request):
    context = {}
    return render(request, 'afg_pro/Customer_account_setting.html', context)


@login_required(login_url='afg_pro:login')
def Creating_order(request, pk):
    customer = MyCustomer.objects.get(id = pk)
    product = MyProduct.objects.get(id=pk)
    form = Create_Form()

    if request.method == "POST":
        form = Create_Form(request.POST)
        if form.is_valid():
            order = form.save()
            customer = get_object_or_404(MyCustomer, user = request.user)
            product = get_object_or_404(MyProduct, name = product.name)
            order.customer = customer
            order.product = product

            order.save()

            return HttpResponseRedirect(reverse('afg_pro:home'))

    context = {'form': form, 'customer': customer, 'product': product}
    return render(request, 'afg_pro/customer_order_form.html', context)





# ----------------------------------------------------------------------------------
# Signup/signin/logout
def SignupView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreatingUserForm()

        if request.method == "POST":
            form = CreatingUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user )
                return redirect('/login')


        context = {
            'form': form
        }
        return render(request, 'afg_pro/signup.html', context)

def LoginView(request):
    
    if request.user.is_authenticated:
        return redirect('/')
    else:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('afg_pro:dashboard'))
            else:
                messages.info(request, "The username or password you entered is incorrect..")

    
        return render(request, 'afg_pro/login.html')

def LogoutView(request):
    logout(request)
    return redirect('/')

