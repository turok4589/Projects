from django.db import models

# Create your models here.

class DietPlan(models.Model):
    BODY_CHOICES = [
        ('lean', 'Lean'),
        ('muscle', 'Muscle Building'),
        ('weight_loss', 'Weight Loss'),
        ('balanced', 'Balanced'),
    ]
    body = models.CharField(max_length=100, choices=BODY_CHOICES)
    morningPlan = models.TextField()
    morningPlanImage = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    afternoonPlan = models.TextField()
    afternoonPlanImage = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    nightPlan = models.TextField()
    nightPlanImage = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    

class Excecise(models.Model):
    videos = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)
    images = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    images1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    images2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    images3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    images4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    