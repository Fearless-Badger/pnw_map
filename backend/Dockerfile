FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip setuptools

WORKDIR /backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["python", "-m", "backend.main"]
