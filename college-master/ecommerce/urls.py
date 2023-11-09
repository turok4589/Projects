from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductAPIView.as_view(),name="ProductAPIView"),
    path('product/<int:pk>/', views.ProductAPIView.as_view(),name="ProductAPIView"),
    path('order/', views.OrderAPIView.as_view(),name="OrderAPIView"),
    path('order/<int:pk>/', views.OrderAPIView.as_view(),name="OrderAPIView"),
    path('payment/', views.PaymentAPIView.as_view(),name="PaymentAPIView"),
    path('payment/<int:pk>/', views.PaymentAPIView.as_view(),name="PaymentAPIView"),
    path('history/', views.OrderHistoryAPIView.as_view(),name="OrderHistoryAPIView"),

    


   

]