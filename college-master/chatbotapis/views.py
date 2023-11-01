from .models import *
from .searializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from rest_framework import generics

class ChatBotApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    search_fields = ['ques']
    filter_backends = (filters.SearchFilter,)
    queryset = chatbot.objects.all()
    serializer_class = ChatbotSerializer
