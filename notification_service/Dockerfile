# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the dependencies file
COPY notification_service/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY notification_service/ .

# Expose FastAPI port
EXPOSE 8001

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
