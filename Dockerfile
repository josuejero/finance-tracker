# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip and install the wheel package
RUN pip3 install --upgrade pip wheel

# Set the PYTHONPATH environment variable to include the src directory
ENV PYTHONPATH=/app/src

# Install any dependencies specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make sure the SQLite database is copied if needed
COPY ./database/finance_tracker.db /app/database/

# Expose port (if your app requires it)
EXPOSE 5000

# Command to run your application
CMD ["python", "src/main.py"]
