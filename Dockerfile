FROM hdgigante/python-opencv:4.11.0-ubuntu

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    cmake \
    g++ \
    python3-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libgstreamer-plugins-base1.0-dev \
    libgstreamer1.0-dev \
    libgtk2.0-dev \
    libgtk-3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements_docker.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt --break-system-packages && \
    rm -rf ./requirements.txt

COPY app/ ./app/
COPY main.py ./

ENV TZ=Europe/Moscow

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]