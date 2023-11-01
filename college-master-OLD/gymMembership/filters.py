import django_filters
from .models import DietPlan

class DietPlanFilter(django_filters.FilterSet):
    body_mass_index__lt_18 = django_filters.NumberFilter(field_name='body_mass_index', lookup_expr='lt', label='BMI < 18')
    body_mass_index__gt_18 = django_filters.NumberFilter(field_name='body_mass_index', lookup_expr='gt', label='BMI > 18')
    body_mass_index__gt_30 = django_filters.NumberFilter(field_name='body_mass_index', lookup_expr='gt', label='BMI > 30')

    class Meta:
        model = DietPlan
        fields = "__all__"
