# Базовый образ
FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt && \
    rm -rf ./requirements.txt

COPY app/ ./app/
COPY main.py ./

ENV TZ=Europe/Moscow

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]