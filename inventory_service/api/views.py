# inventory_services/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import InventoryService

@csrf_exempt  
def get_item_quantity(request, item_id):
    if request.method == 'GET':
        quantity = InventoryService.get_item_quantity(item_id)  
        return JsonResponse({'quantity': quantity}, status=200)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt  
def reduce_item_quantity(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            quantity_to_reduce = data.get('quantity')

            if quantity_to_reduce is None:
                return JsonResponse({'error': 'Quantity is required.'}, status=400)

            success = InventoryService.reduce_item_quantity(item_id, quantity_to_reduce)
            if success:
                return JsonResponse({'message': 'Quantity reduced successfully.'}, status=200)
            else:
                return JsonResponse({'error': 'Not enough quantity or item not found.'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
