from django.shortcuts import render
from .models import DietPlan,Excecise
from .serializer import *
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.permission import IsGymMember
from rest_framework import generics
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import DietPlanFilter
class DietPlanAPIView(APIView):
    permission_classes = [IsAuthenticated,IsGymMember]
    def get_object(self, pk):
        try:
            return DietPlan.objects.get(pk=pk)
        except DietPlan.DoesNotExist:
            raise Http404
        
    # def get(self, request, pk=None, format=None):
    #         if pk:
    #             data = self.get_object(pk)
    #             serializer = DietPlanSerializer(data,context={'request': request})
    #             return Response(serializer.data)

    #         else:
    #             queryset = DietPlan.objects.all()
    #             lt_18 = request.query_params.get('body_mass_index__lt_18')
    #             gt_18 = request.query_params.get('body_mass_index__gt_18')
    #             gt_30 = request.query_params.get('body_mass_index__gt_30')

    #             if lt_18:
    #             # Filter for body_mass_index < 18
    #                 queryset = queryset.filter(body_mass_index__lt=lt_18)
    #             elif gt_18:
    #                     # Filter for body_mass_index > 18
    #                 queryset = queryset.filter(body_mass_index__gt=gt_18)
    #             elif gt_30:
    #                     # Filter for body_mass_index > 30
    #                 queryset = queryset.filter(body_mass_index__gt=gt_30)
    #             if pk:
    #                 data = self.get_object(pk)
    #                 serializer = DietPlanSerializer(data, context={'request': request})
    #                 return Response(serializer.data)

    #             serializer = DietPlanSerializer(queryset, many=True, context={'request': request})
    #             return Response(serializer.data)

    def get(self, request, format=None):
        queryset = DietPlan.objects.all()
        body_mass_index = request.query_params.get('body_mass_index')

        if body_mass_index:
            body_mass_index = int(body_mass_index)
            if body_mass_index < 18:
                # Filter for body_mass_index < 18
                queryset = queryset.filter(body_mass_index__lt=18)
            elif 18 <= body_mass_index < 30:
                # Filter for body_mass_index >= 18 and < 30
                queryset = queryset.filter(body_mass_index__gte=18, body_mass_index__lt=30)

            else:
                queryset = queryset.filter(body_mass_index__gte=30)

        serializer = DietPlanSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)




            



class DietPlanListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DietPlanFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        # Debugging: Print the request.GET and the generated queryset
        print("Request GET parameters:", request.GET)
        print("Generated queryset:", queryset.query)
        
        if not queryset.exists():
            return Response({'detail': 'No data found'}, status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(queryset, many=True)
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