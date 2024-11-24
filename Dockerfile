FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libc6-dev \
    libffi-dev \
    libpq-dev \
    postgresql-client \
    libssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/oktta

COPY req.txt /app/req.txt

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r ../req.txt

COPY . .

ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
