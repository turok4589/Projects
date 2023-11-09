from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.permission import IsGymMember
from rest_framework import status

# Create your views here.

class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = ProductSerializer(data,context={'request': request})
                return Response(serializer.data)

            else:
                data = Product.objects.all()
                serializer = ProductSerializer(data, many=True,context={'request': request})
                return Response(serializer.data)
            


class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = OrderSerializer(data,context={'request': request})
                return Response(serializer.data)

            else:
                current_user = request.user
                data = Order.objects.filter(user=current_user)
                serializer = OrderSerializer(data, many=True,context={'request': request})
                return Response(serializer.data)
            
    def post(self, request, format=None):
       
        current_user = request.user

        # Create a mutable copy of the request data
        mutable_data = request.data.copy()

       
        mutable_data['user'] = current_user.id  

        serializer = OrderSerializerPost(data=mutable_data)
        # seri = OrderHistorySerializerPost(data=mutable_data)
        
        serializer.is_valid(raise_exception=True)
        # seri.is_valid(raise_exception=True)

        # Create the order in the DB
        serializer.save()
        # seri.save()

        # Return Response to User
        response = Response()
        response.data = {
            'message': 'Order Created Successfully',
            'data': serializer.data,
            # 'current_user': current_user.id 
        }

        return response
        # delete the employee
    def delete(self, request, pk=None, format=None):
        user = request.user  # Get the current user

        if pk:
            # Delete the order with the specified ID (pk) for the current user
            try:
                order_to_delete = Order.objects.get(pk=pk, user=user)
                order_to_delete.delete()
                return Response({
                    'message': f'Order with ID {pk} Deleted Successfully'
                })
            except Order.DoesNotExist:
                return Response({
                    'message': f'Order with ID {pk} not found'
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            deleted_orders = Order.objects.filter(user=user)
            for order in deleted_orders:
                order_history = OrderHistory(
                    user=order.user,
                    product=order.product,
                    # delivery_address=order.delivery_address,
                    # delivery_address_pincode=order.delivery_address_pincode,
                    # country = order.country,
                    # state = order.state,
                    # city=order.city,
                    quantity=order.quantity,
                )
                order_history.save()
            deleted_orders.delete()

            return Response({
                'message': 'All Orders for the Current User Deleted and Saved in OrderHistory Successfully'
            })

class OrderHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return OrderHistory.objects.get(pk=pk)
        except OrderHistory.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = OrderHistorySerializerPost(data,context={'request': request})
                return Response(serializer.data)

            else:
                current_user = request.user
                data = OrderHistory.objects.filter(user=current_user)
                serializer = OrderHistorySerializerPost(data, many=True,context={'request': request})
                return Response(serializer.data)

            



class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
        # Get the current user
        current_user = request.user
        if pk:
            payment = self.get_object(pk)
            if payment.order.user == current_user:
                serializer = PaymentSerializer(payment)
                return Response(serializer.data)
            else:
                raise Http404

        else:
            # Get all payments for the current user
            payments = Payment.objects.filter(user=current_user)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
            
    
    def post(self, request, format=None):
           
        current_user = request.user
        mutable_data = request.data.copy()
        mutable_data['user'] = current_user.id  
        serializer = PaymentSerializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)

        # Create the order in the DB
        serializer.save()

        response = Response()
        response.data = {
            'message': 'pyment is done',
            'data': serializer.data,
        }

        return response