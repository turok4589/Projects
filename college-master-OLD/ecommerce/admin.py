from django.contrib import admin
from .models import Product,Order,Payment,OrderHistory
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','headline','price','details','id')

class OrderAmdin(admin.ModelAdmin):
    list_display = ('user','product','id')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('price','status','id')


admin.site.register(OrderHistory)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Order,OrderAmdin)
admin.site.register(Product,ProductAdmin)
