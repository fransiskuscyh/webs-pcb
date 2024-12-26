from django.db import models

class Hommode(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='ImageHom/', blank=True, null=True)

    def __str__(self):
        return self.name
