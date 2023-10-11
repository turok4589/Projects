from django.urls import path
from . import views

urlpatterns = [
    path('diet/', views.DietPlanAPIView.as_view(),name="DietPlanAPIView"),
    path('diet/<int:pk>/', views.DietPlanAPIView.as_view(),name="DietPlanAPIView"),
    path('excerise/', views.ExceciseAPIView.as_view(),name="ExceciseAPIView"),
    path('excerise/<int:pk>/', views.ExceciseAPIView.as_view(),name="ExceciseAPIView"),

   

]