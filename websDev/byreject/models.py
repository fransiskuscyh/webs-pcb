from django.db import models

class Byrejectmode(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.BinaryField()
    status = models.CharField(max_length=50)  
    
    def __str__(self):
        return self.name
