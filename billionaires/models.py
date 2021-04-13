from django.db import models
from django.urls import reverse

# Create your models here.

class Billionaires(models.Model):
    name = models.CharField(max_length=200, blank=False)
    money = models.IntegerField(blank=False)
    source = models.CharField(max_length=150)
    description = models.TextField()
    
    class Meta:
     ordering = ('-money', )
    
    def __str__(self):
        return "{} is worth ${}billion".format(self.name, self.money)
        
    def get_absolute_url(self):
        return reverse('billionaires')