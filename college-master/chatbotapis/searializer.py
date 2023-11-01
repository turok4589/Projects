from rest_framework.serializers import  ModelSerializer
from .models import *



class ChatbotSerializer(ModelSerializer):
    class Meta:
        model = chatbot
        fields = ['ques','ans']