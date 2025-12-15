# Pull base image
FROM python:3.11-slim-bullseye
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code

# Install system dependencies   
RUN apt update && apt install -y \  
    gettext \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt


# Copy project
COPY . /code/