# api/models.py

from django.db import models

class Inventory(models.Model):
    # Define your Inventory fields here
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    # Foreign key to Inventory model
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')  # Include status field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.inventory.name}"
