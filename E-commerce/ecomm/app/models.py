from django.db import models
from django.contrib.auth.models import User
CATEGORY_CHOICES =(
    ('CR','crud'),
    ('MI','Milk'),
    ('LS','lissi'),
    ('MS','Milkshake'),
    ('PN','paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Cream'))
# Create your models here.
class product(models.Model):
    title =models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self) :
        return self.title
    
STATE_CHOICE = (('MH','Maharastra'),
                ('GJ','Gujarat'),
                ('RJ','Rajastan'),
                ('DL','Delhi'),
                ('AN','Andhra Pradesh'),
                ('KA','Karnataka'),
                ('TN','Tamilnadu'),
                ('UP','Uttar Pradesh'),
                ('WB','West Bengal'),
                ('BR','Bihar'),
                ('JH','Jharkhand'),
                ('OR','Orissa'),
                ('CT','Chhattisgarh'),
                ('PB','Punjab'),
                ('HR','Haryana'),
                ('GOA','Goa'),
                ('JK','Jammu and Kashmir'),
                ('HP','Himachal Pradesh'),
                ('AS','Assam'),
                ('TR','Tripura'),
                ('AR','Arunachal Pradesh'),
                ('AP','Andaman and Nicobar Islands'),
                ('TS','Telangana'),
                ('JH','Jharkhand'),
                ('HP','Himachal Pradesh'),
                ('AS','Assam'),
                )

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city  = models.CharField(max_length=200)
    mobile = models.IntegerField()
    zipcode = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICE,max_length=100)


##############################################################################################################
#                                      Order table/class


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    quantitiy =models.PositiveIntegerField(default=1)
    
    @property
    def total_Cost(self):
        return self.quantitiy * self.product.discounted_price




STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Deliverd','Deliverd'),
    ('Cancel','Cancel'),
    ('pending','pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razor_order_id = models.CharField(max_length=100,blank=True,null=True)
    razor_payment_status =models.CharField(max_length=100,blank=True,null=True)
    razor_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

class OrderdPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    Product =models.ForeignKey(product,on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)
    orderd_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICE,default='pending')   
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    @property
    def total_cost(self):
        return self.quantity * self.Product.discounted_price
    
class WishList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(product,on_delete=models.CASCADE)
    