from django.shortcuts import render
from .models import DietPlan,Excecise
from .serializer import *
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.permission import IsGymMember

class DietPlanAPIView(APIView):
    permission_classes = [IsAuthenticated,IsGymMember]
    def get_object(self, pk):
        try:
            return DietPlan.objects.get(pk=pk)
        except DietPlan.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = DietPlanSerializer(data,context={'request': request})
                return Response(serializer.data)

            else:
                data = DietPlan.objects.all()
                serializer = DietPlanSerializer(data, many=True,context={'request': request})
                return Response(serializer.data)
            



class ExceciseAPIView(APIView):
    permission_classes = [IsAuthenticated,IsGymMember]
    def get_object(self, pk):
        try:
            return Excecise.objects.get(pk=pk)
        except models.Excecise.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = ExcerciseSerializer(data,context={'request': request})
                return Response(serializer.data)

            else:
                data = Excecise.objects.all()
                serializer = ExcerciseSerializer(data, many=True,context={'request': request})

                return Response(serializer.data)