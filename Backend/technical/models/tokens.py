from django.db import models


class Tokens(models.Model):
    token= models.CharField(max_length=256)
    valid= 0