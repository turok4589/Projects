from django.db import models
from account.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    price = models.IntegerField()
    headline = models.CharField(max_length=100,blank=True)
    details = models.CharField(blank=True,help_text="product small details")
    description = models.TextField()


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=100,blank=True)
    delivery_address_pincode = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField(null=True)
    created = models.DateField(auto_now=True)


class Payment(models.Model):
    SUBSCRIPTION_CHOICES = [
        ('monthly', 'Monthly Subscription'),
        ('yearly', 'Yearly Subscription'),
    ]
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    subscription = models.CharField(max_length=100,choices=SUBSCRIPTION_CHOICES,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    card_no = models.BigIntegerField(null=True,blank=True)
    expiry_date = models.CharField(max_length=100, blank=True,null=True)
    cvv = models.IntegerField(null=True,max_length=18)
    price = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.order} - {self.get_subscription_display()}"



class OrderHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=100,blank=True)
    delivery_address_pincode = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField(null=True)
    created = models.DateField(auto_now=True)





