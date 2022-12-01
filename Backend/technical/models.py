from django.db import models


class Car(models.Model):
    """Car model."""
    model= models.CharField(max_length=30)
    color= models.CharField(max_length=15)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model
