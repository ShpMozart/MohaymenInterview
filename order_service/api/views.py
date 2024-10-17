# api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import OrderService  # Import the service class

@csrf_exempt  # Temporarily disable CSRF for testing (not recommended for production)
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inventoryId = data.get('inventoryId')
            quantity = data.get('quantity')

            # Step 1: Check if both name and quantity are provided
            if inventoryId is None or quantity is None:
                return JsonResponse({'error': 'inventoryId and quantity are required.'}, status=400)

            # Step 2: Use the OrderService to create the order
            order = OrderService.create_order(inventoryId,quantity)

            return JsonResponse({
                'id': order.id,
                'quantity': order.quantity,
                'status': order.status,
                'created_at': order.created_at.isoformat(),
            }, status=201)  # Return the created order as JSON with status code 201

        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)  # Handle item availability errors
        except RuntimeError as e:
            return JsonResponse({'error': str(e)}, status=500)  # Handle RabbitMQ publishing errors
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)  # Handle invalid JSON

    return JsonResponse({'error': 'Invalid request method.'}, status=400)  # Handle invalid methods


@csrf_exempt  # Temporarily disable CSRF for testing (not recommended for production)
def get_order(request, order_id):
    if request.method == 'GET':
        try:
            # Retrieve the order by ID
            order = OrderService.get_order_by_id(order_id=order_id)

            # Prepare the response data
            order_data = {
                'id': order.id,
                'inventory_name': order.inventory.name,
                'inventory_id': order.inventory.id if order.inventory else None,
                'quantity': order.quantity,
                'status' : order.status,
                'created_at': order.created_at.isoformat(),
            }

            return JsonResponse(order_data, status=200)  # Return order data as JSON with status code 200

        except Exception as e:
            return JsonResponse({'error': 'Order not found.'}, status=404)  # Handle order not found

    return JsonResponse({'error': 'Invalid request method.'}, status=400)  # Handle invalid methods
