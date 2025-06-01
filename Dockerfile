FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app

# Install uv
RUN pip install uv

COPY . .

# Use uv to install dependencies
RUN uv pip install --system --no-cache-dir .

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
