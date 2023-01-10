from django.db import models

class Order (models.Model):
    numbre_order = models.IntegerField
    products = models.__dict__
    time = models.DateTimeField(auto_now_add=True)

