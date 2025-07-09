# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of your app code
COPY . .

# Expose port 5000 for Flask app
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]