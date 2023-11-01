from django.db import models

# Create your models here.
class chatbot(models.Model):
    ques = models.CharField(max_length=300)
    ans = models.CharField(max_length=500)
    