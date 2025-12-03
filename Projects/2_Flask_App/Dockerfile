# Pull base image for Python
FROM python:3.8-slim

# Set working directory in the Image
WORKDIR /app

# Copy everything needed from the current directory 
COPY . .

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt


# Run the application
CMD ["python", "app.py"]