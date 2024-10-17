# api/rabbitmq_publisher.py
import pika
import json

RABBITMQ_HOST = 'rabbitmq'  
RABBITMQ_QUEUE = 'orders'

def publish_order_event(order):
    """Publish an order event to RabbitMQ."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    # Create the message payload
    message = {
        'id': order.id
    }

    # Publish the message
    channel.basic_publish(
        exchange='',
        routing_key=RABBITMQ_QUEUE,
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make message persistent
        )
    )

    # Close the connection
    connection.close()
