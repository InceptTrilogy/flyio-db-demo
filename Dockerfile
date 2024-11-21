FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN pip install -e .

CMD ["uvicorn", "flyio_db_demo.api:app", "--host", "0.0.0.0", "--port", "8080"]
