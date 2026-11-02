# Stage 1: Build dependencies and train the model
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements-serving.txt .

RUN pip install --user --no-cache-dir -r requirements-serving.txt

COPY data/processed/iris_features.csv data/processed/iris_features.csv
COPY src/train_final_model.py src/train_final_model.py

ENV PATH=/root/.local/bin:$PATH

RUN python src/train_final_model.py


# Stage 2: Minimal runtime image
FROM python:3.11-slim AS runtime

WORKDIR /app

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/models /app/models
COPY src/serve.py src/serve.py

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)"

CMD ["python", "src/serve.py"]
