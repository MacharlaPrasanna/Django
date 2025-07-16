FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        libmariadb-dev \
        libmariadb-dev-compat \
        pkg-config \
        build-essential \
        gcc \
        libssl-dev \
        libffi-dev \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*



COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
