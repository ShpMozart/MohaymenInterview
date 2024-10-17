# Dockerfile

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

# Run migrations and collect static files
# RUN python3 manage.py migrate
# RUN python3 manage.py collectstatic --noinput

# Expose the port your app runs on
EXPOSE 8080

# Start the Django application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]


