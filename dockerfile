# Dockerfile

FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy folder to be built
COPY nutrihelp_ai/ ./nutrihelp_ai/
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose FastAPI app port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "nutrihelp_ai.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
