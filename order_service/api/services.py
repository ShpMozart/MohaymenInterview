from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from .models import Order
from .inventory_service import check_item_availability,reduce_item_quantity
from .rabbitmq_publisher import publish_order_event

class OrderService:
    @staticmethod
    def create_order(inventory_id, quantity):
        # Check availability with Inventory Service
        # Uncomment the following line if you need to check item availability before creating an order
        if not check_item_availability(inventory_id, quantity):
            raise ValueError('Item not available in inventory.')
                            
        try:
            reduce_item_quantity(inventory_id,quantity)
        except Exception as e:
            raise RuntimeError('Failed to reduce quantity in inventory.')
        
        try:
            order = Order.objects.create(inventory_id=inventory_id, quantity=quantity)
        except Exception as e:
            raise RuntimeError('Failed to save order');
        
        try:
            publish_order_event(order)
        except Exception as e:
            # Handle exception, you can log this error if needed
            raise RuntimeError('Failed to publish order event to RabbitMQ.')
        return order

    @staticmethod
    def get_order_by_id(order_id):
        try:
            return Order.objects.get(id=order_id)
        except Exception as e:
            return None  # Return None if the order is not found
