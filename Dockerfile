# Start with a lightweight Python image
FROM python:3.11-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Gunicorn recommended for production
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
