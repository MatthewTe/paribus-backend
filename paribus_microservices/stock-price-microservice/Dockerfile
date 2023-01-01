FROM python:3.8-slim

# Create a directory for the app
RUN mkdir -p /app

# Set the working directory to the app directory
WORKDIR /app

# Copy the requirements file to the app directory
COPY requirements.txt /app

# Install the required libraries
RUN pip install -r requirements.txt

# Copy the app code to the app directory
COPY stock-price-microservice.py /app

# Expose the default Flask port
EXPOSE 5001