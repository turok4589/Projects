from django.contrib import admin
from .models import DietPlan, Excecise

# Register your models here.

class customDietPlan(admin.ModelAdmin):
    list_display = ('body','morningPlan','afternoonPlan','nightPlan',)


admin.site.register(DietPlan,customDietPlan)
admin.site.register(Excecise)