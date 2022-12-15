from django.db import models

# Create your models here.
class Hello(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True, default='username')
    
    def __str__(self):
        return self.name
