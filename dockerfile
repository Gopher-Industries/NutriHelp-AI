# Dockerfile

FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app code last (this is what changes most often)
COPY nutrihelp_ai/ ./nutrihelp_ai/

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "nutrihelp_ai.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
