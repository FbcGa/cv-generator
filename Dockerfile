FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
WORKDIR /app
RUN pip install --no-cache-dir uv

RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    libharfbuzz0b \
    libjpeg62-turbo \
    libopenjp2-7 \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*
    
COPY ./pyproject.toml /app/pyproject.toml
COPY ./uv.lock* /app/uv.lock

RUN uv sync

COPY ./src /app/src
COPY ./gunicorn.dev.conf.py /app/gunicorn.dev.conf.py

EXPOSE 5000

CMD ["uv", "run", "gunicorn", "-c", "gunicorn.dev.conf.py", "src.main:app"]