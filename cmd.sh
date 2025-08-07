# Start Celery worker
echo "Starting Celery..."
celery -A celery_app worker --loglevel=info &

echo "Starting FastAPI..."
uvicorn main:app --host 0.0.0.0 --port 8000 &