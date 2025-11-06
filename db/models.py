import sys
from django.db import models


class Product(models.Model):
    # UPC (Universal Product Code) as a string field — unique identifier
    upc = models.CharField(max_length=12, unique=True)

    # Name of the product
    name = models.CharField(max_length=100)

    # Price of the product, with up to 6 digits total and 2 decimal places
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class User(models.Model):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name
