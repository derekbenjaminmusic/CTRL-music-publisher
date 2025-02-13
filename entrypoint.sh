#!/bin/bash
set -e  # Exit on error

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput || echo "Database migration failed, continuing..."

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput || echo "Static file collection failed, continuing..."

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:${PORT:-8080} dmp_project.wsgi:application --workers 3 --threads 2
