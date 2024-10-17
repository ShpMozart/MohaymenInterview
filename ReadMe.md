# Order Management System

## Overview

This project is an Order Management System built using Django, MySQL, and RabbitMQ. It consists of three main components:

1. **Inventory Service**: A REST API to check availability and reduce the quantity of items.
2. **Order Service**: A REST API to create orders and retrieve order details.
3. **Shipping Service**: A consumer service that changes the status of orders based on events.

## Technologies Used

- **Django**: Web framework for building the REST APIs.
- **MySQL**: Database for storing inventory and order data.
- **RabbitMQ**: Message broker for handling asynchronous messaging between services.
- **Libraries**:
  - `requests`: For making HTTP requests.
  - `cryptography`: For secure data handling.
  - `PyMySQL`: MySQL database adapter for Python.
  - `Pika`: RabbitMQ client library for Python.
  - `Django REST Framework`: Toolkit for building Web APIs.

## Features

- **Inventory Management**: Check item availability and adjust stock levels.
- **Order Creation**: Create new orders and retrieve details about existing orders.
- **Order Status Updates**: Automatically change order statuses using RabbitMQ.

## Getting Started

### Prerequisites

- Python 3.x
- Docker and Docker Compose
- MySQL

To start the project, follow these steps:

password in project is qazplmtygv so your MySql password of root user have to be qazplmtygv

1. **Build and Start the Services**:
   ```bash
   docker-compose up --build
   docker-compose exec db mysql -u root -p
   USE mohaymen;
   INSERT INTO api_inventory (name, quantity) VALUES ('IPhoneX', 20);
   INSERT INTO api_inventory (name, quantity) VALUES ('MacBook M1 Pro', 10);
   COMMIT;
   ```
2. **Use the services**:
   - Install thunder client extension on your vs code
   - use services

