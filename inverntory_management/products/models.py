from accounts.models import my_user
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    company_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
         my_user, related_name='products', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
