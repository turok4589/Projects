from django.db import models

# Create your models here.

class DietPlan(models.Model):
    BODY_CHOICES = [
        ('lean', 'Lean'),
        ('muscle', 'Muscle Building'),
        ('weight_loss', 'Weight Loss'),
        ('balanced', 'Balanced'),
    ]
    body_mass_index = models.IntegerField(null=True)
    body = models.CharField(max_length=100, choices=BODY_CHOICES)
    calories = models.IntegerField(null=True,blank=True)
    morningPlan = models.TextField()
    morningPlanImage = models.URLField(blank=True)
    afternoonPlan = models.TextField()
    afternoonPlanImage = models.URLField(blank=True)
    nightPlan = models.TextField()
    nightPlanImage = models.URLField(blank=True)
    

class Excecise(models.Model):
    videos = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)
    images = models.URLField(blank=True)
    images1 = models.URLField(blank=True)
    images2 = models.URLField(blank=True)
    images3 = models.URLField(blank=True)
    images4 = models.URLField(blank=True)
    