# Stage 1: Build environment
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .

# Install build tools & dependencies to build wheels
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ffmpeg \
        libsm6 \
        libxext6 \
        unzip \
        curl \
        && pip install --upgrade pip \
        && pip wheel --no-cache-dir -r requirements.txt -w /wheels \
        && apt-get purge -y --auto-remove build-essential \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# Stage 2: Minimal runtime image
FROM python:3.12-slim AS runtime

WORKDIR /app

# System dependencies for runtime
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        libsm6 \
        libxext6 \
        unzip \
        curl \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

COPY . .

CMD ["python3", "app.py"]
