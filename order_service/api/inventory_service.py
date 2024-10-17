import requests

@staticmethod
def check_item_availability(id, quantity):
    """Check the availability of an item in the inventory."""
    inventory_service_url = f'http://inventory:8080/api/inventory/{id}/'
    response = requests.get(inventory_service_url)
    
    if response.status_code == 200:
        data = response.json()  
        available_quantity = data.get('quantity', 0)  # Get 'quantity', default to 0 if not found
        
        if available_quantity >= quantity:
            return True
        else:
            return False
    else:
        # Handle non-200 responses
        return False
    
@staticmethod
def reduce_item_quantity(item_id, quantity):
    """Send a request to inventory_service to reduce item quantity."""
    inventory_service_url = f'http://inventory:8080/api/inventory/reduce/'
    
    payload = {
        'item_id': item_id,
        'quantity': quantity
    }
    
    try:
        response = requests.post(inventory_service_url, json=payload)
        
        if response.status_code == 200:
            data = response.json()  
            if data.get('success'):  # Check if the reduction was successful
                return True
            else:
                return False
        else:
            # Log or handle non-200 responses here
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False