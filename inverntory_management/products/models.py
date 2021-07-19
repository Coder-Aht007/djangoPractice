from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    company_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_by = models.ForeignKey(
        User, related_name='products', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name