"""
Definition of models.
"""

from pyexpat import model
from django.db import models



class Item(models.Model):
    name = models.CharField(
        max_length=200
        )
    description = models.CharField(
        max_length=200
        )
    price_number = models.CharField(
        max_length=200
        )
    price_id = models.CharField(
        max_length=200
        )

