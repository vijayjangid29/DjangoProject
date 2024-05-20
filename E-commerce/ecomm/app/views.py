from django.shortcuts import render,redirect
from .models import product,Customer,Cart,OrderdPlaced,Payment,WishList
from itertools import count
from django.http import JsonResponse
from django.db.models import Count
from django.views import View
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(requst):
    totalitem  = 0
    if requst.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=requst.user))
    return render(requst,'app/index.html',locals())

def about(requst):
    totalitem  = 0
    if requst.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=requst.user))
    return render(requst,'app/about.html',locals())

def contact(requst):
    totalitem  = 0
    if requst.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=requst.user))
    return render(requst,'app/contact.html',locals())

def Category(request,val):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    prod = product.objects.filter(category=val)
    title = product.objects.filter(category=val).values('title').annotate(total=Count('title'))
    return render (request,'app/category.html',locals())

def category_title(request,val):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    print(''.center(200,'*'))
    Product  = product.objects.filter(title= val)
    title    = product.objects.filter(category=Product[0].category).values('title')
    prod = product.objects.filter(title=val)
    return render(request,'app/category.html',locals())
@method_decorator(login_required,name="dispatch")
class ProductDetail(View):
    def get(self, request, pk):
        prod = product.objects.get(pk=pk)
        wishList = WishList.objects.filter(Q(user=request.user) & Q(id=prod.id))
        print(wishList)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        
        return render(request, 'app/productdetail.html', {'prod': prod, 'wishList': wishList, 'totalitem': totalitem})

class RegistrationView(View):
    def get(self,request):
        totalitem  = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerRegistrationForm()
        return render(request,'app/registration.html',locals())
    def post(self,request):
        
        form = CustomerRegistrationForm(request.POST)
#        print(form.cleaned_data['username'])
        if form.is_valid():
            print('orange')
            form.save()
            m= messages.success(request,'Congratulations ! User Register Successfully !')
            return redirect('profile')
        else:
           print('Else block')
           m= messages.error(request,'Invaild Input Data')
           print(m)
        return render(request,'app/registration.html',locals())
@method_decorator(login_required,name="dispatch")
class profileview(View):
    def get(self,request):
        totalitem  = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))

        form = CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode,state=state)
            reg.save()
            messages.success(request,'Congratulations ! Profile Updated Successfully !')
        else:
            messages.warning(request,'Invalid Input Data ')
        return render(request,'app/profile.html',locals())
@login_required
def address(request):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    add = Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())
@method_decorator(login_required,name="dispatch")
class update_Address(View):
    def get(self,request,pk):
        totalitem  = 0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))

        qs = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=qs)
        return render(request,'app/update.html',locals())
    def post(self,request,pk):
        totalitem  = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))

        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            qs = Customer.objects.get(pk=pk)
            qs.name =     form.cleaned_data['name']
            qs.locality = form.cleaned_data['locality']
            qs.city    =  form.cleaned_data['city']
            qs.mobile  =  form.cleaned_data['mobile']
            print(qs.mobile)
            qs.state   =  form.cleaned_data['state']
            qs.zipcode =  form.cleaned_data['zipcode']
            qs.save()
            messages.success(request,'Congratulations ! Profile Updated Successfully !')
        else:
            messages.warning(request,'Invalid Input Data ')
        return redirect('address')
    
##############################################################################################################################



@login_required
def add_to_cart(request):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    user = request.user
    # print(user)
    product_id = request.GET.get('prod_id')
    # print(product_id)
    Product = product.objects.get(id=product_id)
    Cart(user=user,product=Product).save()
    redirect('/cart')
@login_required
def show_cart(request):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for val in cart:
        value = val.quantitiy * val.product.discounted_price
        amount+=value
    totalamount = amount+40
    return render(request,'app/addtocart.html',locals())
@login_required
def pluscart(request):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    if request.method == "GET":
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id ) & Q(user=request.user) )
        c.quantitiy+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for val in cart:
            value = val.quantitiy * val.product.discounted_price
            amount+=value
        totalamount = amount+40
        data = {
            'quantity':c.quantitiy,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
@login_required
def minus_cart(request):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    if request.method == "GET":
        prod_id  = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantitiy-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for val in cart:
            value = val.quantitiy * val.product.discounted_price
            amount+=value
        totalamount = amount+40
        data = {
            'quantity':c.quantitiy,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
@login_required
def remove_cart(request):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    if request.method == "GET":
        prod_id  = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        c.save(commit=True)
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for val in cart:
            value = val.quantitiy * val.product.discounted_price
            amount+=value
        totalamount = amount+40
        data = {
            # 'quantity':c.quantitiy,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

import razorpay
@method_decorator(login_required,name="dispatch")
class checkout(View):
    
    def get(self,request):
        totalitem  = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
   
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0

        for p in cart_items:
            value = p.quantitiy + p.product.discounted_price
            famount+=value
        totalamount = famount + 40
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data = {'amount':razoramount,"currency":'INR',"receipt":'order_rcptid_12'}
        payment_response = client.order.create(data=data)
        # print(payment_response)
        #{'id': 'order_OCJKpgDLqSsgh2', 'entity': 'order', 'amount': 18100, 'amount_paid': 0, 'amount_due': 18100, 'currency': 'INR', 'receipt': 'order_rcptid_12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1716112652}
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == "created":
            payment = Payment(
                user = user,
                amount = totalamount,
                razor_order_id=order_id,
                razor_payment_status = order_status
            )
            payment.save()
        return render(request,'app/checkout.html',locals())
@login_required
def payment_done(request):
    print('aaya')
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    user = request.user
    customer = Customer.objects.get(id = cust_id)
    payment = Payment.objects.get(razor_order_id=order_id)
    
    payment.paid =True
    print(payment.paid)
    payment.razor_payment_id = payment_id
    payment.save()
    cart = Cart.objects.filter(user = user)
    for c in cart:
        OrderdPlaced(user=user,customer=customer,product=c.product,quantity=c.quantitiy).save()
        c.delete()
    return redirect("orders")
@login_required
def order(request):
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    order_placed = OrderdPlaced.objects.filter(user = request.user)
    return render(request,'app/order.html',locals())
from django.http import JsonResponse, HttpResponseBadRequest
@login_required
def plus_wishList_view(request):
    if request.method == "GET":
        try:
            print('here all good')
            prod_id = 1
            if not prod_id:
                return HttpResponseBadRequest("Product ID is required.")
            
            print(prod_id, 'this is prod id')
            prod_id = int(prod_id)
            
            # Ensure product is correctly defined with a capital P
            Product = product.objects.get(id=prod_id)
            WishList(user=request.user, product=Product).save()
            
            data = {
                'message': 'Wishlist Added Successfully'
            }
            return JsonResponse(data)
        
        except product.DoesNotExist:
            return HttpResponseBadRequest("Product not found.")
        
        except ValueError:
            return HttpResponseBadRequest("Invalid Product ID.")
        
        except Exception as e:
            print(e)
            return HttpResponseBadRequest(f"An error occurred: {str(e)}")

@login_required
def minus_wishList_view(request):
    if request.method == "GET":
        try:
            print('here all good')
            prod_id = request.GET.get('prod_id')
            print(prod_id)
            prod_id = int(prod_id)
            Product  = product.objects.get(id=prod_id)
            WishList(user = request.user,product = Product).delete()
            data = {
            'message':'Wishlist Added Successfully'
            }
            return JsonResponse(data)
        except Exception as e:
            print(e)
from django.core.serializers import serialize

def search(request):
    query = request.GET.get('search')
    totalitem  = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user= request.user))
    Product  = product.objects.filter(Q(title__icontains = query))
    #seria = serialize('json',[Product])
    print(Product)

    return render(request,'app/search.html',locals())