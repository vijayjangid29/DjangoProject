from django.contrib import admin
from .models import product,Customer,Cart,Payment,OrderdPlaced,WishList
from django.utils.html import format_html
from django.urls import reverse
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['id','title','selling_price','discounted_price','category','product_image']
admin.site.register(product,ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','mobile','zipcode','state']

admin.site.register(Customer,CustomerAdmin)

@admin.register(Cart)
class Cart_admin(admin.ModelAdmin):
    list_display = ['id','user','product','quantitiy']
   # def products(self,obj):
   #     link = reverse("admin:app_product_change",args=[object.product.pk])
    #    return format_html('<a href="{}"></a> ',link,obj.product.title)


@admin.register(Payment)

class Payment_admin(admin.ModelAdmin):
    list_display = ['id','user','amount','razor_order_id','razor_payment_status','razor_payment_id','paid']

@admin.register(OrderdPlaced)
class OrderdPlaced_admin(admin.ModelAdmin):
    list_display = ['id','user','customer','Product','quantity','orderd_date','status']

@admin.register(WishList)
class WishList_admin(admin.ModelAdmin):
    list_display = ['id','user','product']
