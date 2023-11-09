from .models import  *
from rest_framework.serializers import ModelSerializer
from django.contrib.sites.shortcuts import get_current_site
from account.serializer import UserSerializers


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def imagePlanImage(self, obj):
        return self.build_absolute_image_url(obj.image)
    
    def build_absolute_image_url(self, image_path):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(image_path)
        else:
            # If request is not available (for example, in shell), use the default site
            site = get_current_site(None)
            return f"{site.scheme}://{site.domain}{image_path}"

       

class OrderSerializer(ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializers(instance.user).data
        # response['product'] = ProductSerializer(instance.product).data
        return response
    


class OrderSerializerPost(ModelSerializer):
    class Meta:
        model = Order
        fields = ["user","product","created","quantity","id"]


class OrderHistorySerializerPost(ModelSerializer):
    class Meta:
        model = OrderHistory
        #fields = '__all__'
        fields = ["user","product","created","quantity","id"]
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
       
        return response

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        # response['order'] = OrderSerializer(instance.order).data
        response['user'] = UserSerializers(instance.user).data
        return response
