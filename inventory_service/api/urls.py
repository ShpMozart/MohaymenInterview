# inventory_services/urls.py

from django.urls import path
from .views import get_item_quantity, reduce_item_quantity

urlpatterns = [
    path('inventory/<int:item_id>/', get_item_quantity, name='get_item_quantity'),
    path('inventory/reduce/', reduce_item_quantity, name='reduce_item_quantity'),
]
