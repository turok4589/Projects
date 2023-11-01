from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', ChatBotApiView.as_view(), name='ChatBotApiView'),
]