# Используем базовый образ Alpine Linux с Python 3.12
FROM ubuntu:22.04

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libtiff-dev \
    libwebp-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir pillow

# Создаем рабочую директорию в контейнере
WORKDIR /app

# Копируем ваш файл программы в контейнер
COPY . /app

# Указываем команду для запуска программы
CMD ["python3", "ascii-art.py"]
