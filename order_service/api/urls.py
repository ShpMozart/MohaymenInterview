# api/urls.py

from django.urls import path
from .views import create_order, get_order  # Import the new view

urlpatterns = [
    path('order/', create_order, name='create_order'),  # Existing path for creating an order
    path('order/<int:order_id>/', get_order, name='get_order'),  # New path for getting an order by ID
]
