from .models import  *
from rest_framework.serializers import ModelSerializer
from django.contrib.sites.shortcuts import get_current_site

class DietPlanSerializer(ModelSerializer):
    class Meta:
        model = DietPlan
        fields = '__all__'
    def get_morningPlanImage(self, obj):
        return self.build_absolute_image_url(obj.morningPlanImage)

    def get_afternoonPlanImage(self, obj):
        return self.build_absolute_image_url(obj.afternoonPlanImage)

    def get_nightPlanImage(self, obj):
        return self.build_absolute_image_url(obj.nightPlanImage)

    def build_absolute_image_url(self, image_path):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(image_path)
        else:
            # If request is not available (for example, in shell), use the default site
            site = get_current_site(None)
            return f"{site.scheme}://{site.domain}{image_path}"

class ExcerciseSerializer(ModelSerializer):
    class Meta:
        model = Excecise
        fields = '__all__'
    def get_videos(self, obj):
            return self.build_absolute_image_url(obj.videos)

    def get_images(self, obj):
        return self.build_absolute_image_url(obj.images)

    def get_images2(self, obj):
        return self.build_absolute_image_url(obj.images2)
    
    def get_images3(self, obj):
        return self.build_absolute_image_url(obj.images3)
    
    def get_images4(self, obj):
        return self.build_absolute_image_url(obj.images4)
    
    def get_images1(self, obj):
        return self.build_absolute_image_url(obj.images1)

    def build_absolute_image_url(self, image_path):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(image_path)
        else:
            # If request is not available (for example, in shell), use the default site
            site = get_current_site(None)
            return f"{site.scheme}://{site.domain}{image_path}"