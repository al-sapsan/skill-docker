# Используем базовый образ Alpine Linux с Python 3.12
FROM python:3.12-alpine

# Устанавливаем зависимости системы
RUN apk add --no-cache \
    build-base \
    python3-dev \
    libjpeg-turbo-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    tiff-dev

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir pillow

# Создаем рабочую директорию в контейнере
WORKDIR /app

# Копируем ваш файл программы в контейнер
COPY . /app

# Указываем команду для запуска программы
CMD ["python", "ascii-art.py"]
