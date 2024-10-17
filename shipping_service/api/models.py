# api/models.py
from django.db import models

class Order(models.Model):
    inventory_id = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order {self.id}: {self.status}"
