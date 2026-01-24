# Pull base image
FROM python:3.11-slim-bullseye
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code

# Install system dependencies   
# Install system dependencies for Django + Pillow + Postgres
RUN apt update && apt install -y \
    gettext \
    libpq-dev \
    gcc \
    zlib1g-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    libtiff5-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt


# Copy project
COPY . /code/