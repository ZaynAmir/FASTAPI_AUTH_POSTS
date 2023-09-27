# Use the official Python image as the base image
FROM python:alpine3.18

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Updating the os
RUN apk update

RUN apk add gcc g++ linux-headers
RUN apk add libffi-dev
# Installing python3-dev
#RUN apk add python3-dev git

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI and MySQL ports
EXPOSE 8000
EXPOSE 3307

# # Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=admin
ENV MYSQL_DATABASE=fastapi_db
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=admin

# # Install MySQL server and client
RUN apk update && apk add mysql mysql-client

# Copy the FastAPI application code into the container
COPY . /app/

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
