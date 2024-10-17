import os
import pika
import json

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shipping_service.settings')

import django
django.setup()  # Initialize Django

from .models import Order

def update_order_status(order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.status = 'Shipped'
        order.save()
        print(f"Order {order_id} status updated to 'Shipped'.")
    except Order.DoesNotExist:
        print(f"Order {order_id} not found.")

def callback(ch, method, properties, body):
    """Callback function to handle incoming messages."""
    message = json.loads(body)
    order_id = message.get('id')
    if order_id:
        update_order_status(order_id)
    else:
        print("No order ID found in the message.")

def start_consumer():
    """Start the RabbitMQ consumer."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Declare the queue (replace 'your_queue_name' with the actual name)
    channel.queue_declare(queue='orders',durable=True)

    # Set up the consumer
    channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
