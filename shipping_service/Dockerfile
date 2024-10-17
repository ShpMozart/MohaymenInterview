# Dockerfile for shipping_service

# Use the official Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port your app runs on (optional, as this service is a consumer)
# EXPOSE 8080 

# Start the RabbitMQ consumer
CMD ["python3", "-c", "from api.rabbitmq_consumer import start_consumer; start_consumer()"]
