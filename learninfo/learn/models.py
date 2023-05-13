from django.db import models

# Create your models here.

class Table(models.Model):
    name      = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emails    = models.EmailField()
    cards     = models.CharField(max_length=30) 
    
    def __str__(self):
        return self.name