# inventory_services/services.py
from .models import Inventory  
from django.core.exceptions import ObjectDoesNotExist

class InventoryService:
    @staticmethod
    def get_item_quantity(item_id):
        try:
            item = Inventory.objects.get(id=item_id)
            return item.quantity
        except ObjectDoesNotExist:
            return 0

    @staticmethod
    def reduce_item_quantity(item_id, quantity):
        try:
            item = Inventory.objects.get(id=item_id)
            if item.quantity >= quantity:
                item.quantity -= quantity
                item.save() 
                return True
            else:
                return False  
        except ObjectDoesNotExist:
            return False  
