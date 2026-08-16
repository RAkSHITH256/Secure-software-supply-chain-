FROM python:3.13-slim

# Prevent Python from creating .pyc files
# and ensure logs are written immediately.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Create a dedicated non-root user.
RUN useradd --create-home --shell /usr/sbin/nologin appuser

# Copy dependency definition first.
COPY app/requirements.txt .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source.
COPY app/src/ .

# Give the application user ownership of the application.
RUN chown -R appuser:appuser /app

# Switch away from root.
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s \
            --timeout=5s \
            --start-period=5s \
            --retries=3 \
            CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health')"

CMD ["python", "app.py"]
