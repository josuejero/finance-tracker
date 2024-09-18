FROM python:3.9.16-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip wheel \
    && pip install --no-cache-dir -r requirements.txt

FROM python:3.9.16-slim

WORKDIR /app

COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

COPY . /app

ENV PYTHONPATH=/app/src

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

COPY --chown=appuser:appgroup ./database/finance_tracker.db /app/database/

ARG PORT=5000
ENV PORT=${PORT}
EXPOSE ${PORT}

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:${PORT}/health || exit 1

CMD ["python", "src/main.py"]
