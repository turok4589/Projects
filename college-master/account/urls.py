from django.urls import path,include
from .views import Register,Login,userData,update_profile,PasswordResetAPIView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
     path('register/', Register.as_view(),name="register"),
     path('login/', Login.as_view(),name="login"),
     path('profile/',userData.as_view(),name="profile"),
     path('update-profile/',update_profile.as_view(),name="update_profile"),

     path('password_reset/', PasswordResetView.as_view(), name='account_password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
     path('password_reset/', PasswordResetAPIView.as_view(), name='password_reset')
]
