FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Add health check (e.g., hitting the root URL of the Flask app)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
 CMD curl --fail http://localhost:8080/ || exit 1

CMD ["python", "app.py"]
