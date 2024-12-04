___
# Отчет о выполнении практической работы по теме: "Виртуализация и контейнеризация"
___
## Подготовительный этап
С учетом выполненной практической работы по теме: [Работа с системой контроля версий Git](https://github.com/al-sapsan/skill-linux/tree/module4) и с целью дальнейшего углубления и практического усвоения полученных знаний, было принято решение, в рамках данной работы, осуществить копию (подобие) полномасштабного проекта с участием привлеченных сотрудников (Collaborators), созданием проекта в GitHub Projects, использованием различных ветвей для отдельных частей проекта, формированием и рассмотрением запросов на слияние изменений (Pull requests) и т.д.

Также, ввиду наличия в сети противоречивой информации об использовании дистрибутивов Ubuntu и Alpine linux для развертывания образов Docker, хотелось бы самому поглубже разобраться с этим вопросом. 

**Учитывая вышесказанное, на подготовительном этапе были выполнены следующие действия:**
1. Созданы и надлежащим образом оформлены аккаунты "привлеченных сотрудников", которые были поименованы как: [git-tester1](https://github.com/git-tester1) и [git-tester2](https://github.com/git-tester2).
2. Направлены приглашения на сотрудничество с помошью соответствующего интерфейса GitHub, которые были успешно приняты и подтверждены :-)
3. Создан данный репозиторий `skill-docker` для размещения проекта.
4. С помощью GitHub Projects создан [проект](https://github.com/users/al-sapsan/projects/2), в котором всем сотрудникам были даны задания.
5. В соответствии с полученными заданиями, в репозитории `skill-docker` были созданы следующие ветви:
  - `main` - ветвь репозитория для размещения окончательного варианта выполненного проекта;
  - `dev` - ветвь по умолчанию, созданная для размещения рабочих вариантов проекта;
  - `docker-container` - ветвь, созданная [git-tester1](https://github.com/git-tester1) для размещения своей части проекта;
  - `python-code` - ветвь, созданная [git-tester2](https://github.com/git-tester2) для размещения своей части проекта.
___
## Разработка программы на Python

### 1. Общее описание выполненных действий
В целях простоты и наглядности выполнения задания, был выбран и реализован код, который преобразует любое изображение в [ASCII-арт](https://ru.wikipedia.org/wiki/ASCII-графика), сохраняя его пропорции и используя символы для представления яркости каждого пикселя. По условиям проекта данный код был создан сотрудником Git-tester2 в ветви `python-code`. После создания кода и его утверждения, Git-tester2 сформировала запрос на слияние, который был одобрен, после чего произведено слияние ветви `python-code` и ветви `dev`. Ветвь `python-code` не удалялась для контроля проделанной работы.

### 2. Разработанный код

```python
from PIL import Image # import the PIL library

# Set the ASCII characters that will be used to create the art
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def modify_into_grayscale_image(image):
    return image.convert("L")

# Map each pixel to an ASCII character
def transform_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

# Main function
def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    # Resize and convert to grayscale
    image = resize_image(image, new_width)
    image = modify_into_grayscale_image(image)
    # Convert pixels to ASCII
    ascii_str = transform_pixels_to_ascii(image)
    # Format an ASCII string for proper display
    img_width = image.width
    ascii_art = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_art += ascii_str[i:i + img_width] + "\n"
    return ascii_art

# Example of use
path = "/app/drone.jpeg"
ascii_art = convert_image_to_ascii(path)
print(ascii_art)

# Saving the obtained result to a file
with open("ascii_image.txt", "w") as f:
    f.write(ascii_art)
```
**Примечание:** комментарии в коде написаны на английском языке не с целью демонстрации его знания, а так как `pylint` в VIMе постоянно ругался на отсутствие комментариев, чем изрядно раздражал создателя кода :-) 

### 3. Описание работы кода

#### 3.1. Импортирование необходимой библиотеки
```python
from PIL import Image 
```
Эта строка импортирует `Image` из модуля `PIL` (Python Imaging Library), который используется для открытия, обработки и сохранения файлов изображений.

#### 3.2. Определение ASCII-символов
```python
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
```
Этот список содержит символы, которые будут использоваться для представления различных оттенков серого в ASCII-арте. Символы расположены от самых темных (`@`) до самых светлых (`.`).

#### 3.3. Изменение размера изображения
```python
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image
```
- **Цель функции**: Эта функция изменяет размер входного изображения, сохраняя его соотношение сторон.
- **Параметры**: 
  - `image`: Входное изображение, которое нужно изменить.
  - `new_width`: Желаемая ширина измененного изображения (по умолчанию 100 пикселей).
- **Процесс**:
  - Вычисляется соотношение сторон оригинального изображения.
  - Рассчитывается новая высота на основе соотношения сторон и желаемой ширины.
  - Изображение изменяется до новых размеров и возвращается.

#### 3.4. Преобразование в градации серого
```python
def modify_into_grayscale_image(image):
    return image.convert("L")
```
- **Цель функции**: Эта функция преобразует входное изображение в градации серого.
- **Параметры**: 
  - `image`: Входное изображение для преобразования.
- **Процесс**: Используется метод `convert` с режимом `"L"` (яркость) для преобразования изображения в градации серого и возвращается.

#### 3.5. Преобразование пикселей в ASCII-символы
```python
def transform_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str
```
- **Цель функции**: Эта функция сопоставляет значение яркости каждого пикселя с ASCII-символом.
- **Параметры**: 
  - `image`: Изображение в градациях серого, из которого будут извлекаться данные пикселей.
- **Процесс**:
  - Извлекаются данные пикселей из изображения с помощью метода `getdata()`.
  - Для каждого значения пикселя (от 0 до 255) вычисляется индекс, деля на 25 (так как есть 10 ASCII-символов), и соответствующий символ из `ASCII_CHARS` добавляется к строке.

#### 3.6. Основная функция для преобразования
```python
def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    # Resize and convert to grayscale
    image = resize_image(image, new_width)
    image = modify_into_grayscale_image(image)
    # Convert pixels to ASCII
    ascii_str = transform_pixels_to_ascii(image)
    # Format an ASCII string for proper display
    img_width = image.width
    ascii_art = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_art += ascii_str[i:i + img_width] + "\n"
    return ascii_art

```
- **Цель функции**: Это основная функция, которая координирует весь процесс преобразования изображения в ASCII-арт.
- **Параметры**: 
  - `image_path`: Путь к файлу входного изображения.
  - `new_width`: Желаемая ширина для изменения размера (по умолчанию 100).
- **Процесс**:
  - Пытается открыть указанный файл изображения. Если это не удается, выводит сообщение об ошибке и завершает выполнение.
  - Изменяет размер и преобразует открытое изображение в градации серого.
  - Преобразует данные пикселей в строку ASCII.
  - Наконец, форматирует эту строку в строки, которые соответствуют ширине измененного изображения.

#### 3.7. Входные данные
```python
path = "/app/drone.jpeg"
ascii_art = convert_image_to_ascii(path)
print(ascii_art)
```
Этот раздел инициирует функцию `convert_image_to_ascii`, предоставляя путь к изображению (`drone.jpeg`). Данный путь указан в соответствии с размещением файла в образе Docker. Полученный ASCII-арт выводится на консоль.

#### 3.8. Сохранение ASCII-арта в файл
```python
with open("ascii_image.txt", "w") as f:
    f.write(ascii_art)
```
Этот блок сохраняет сгенерированный ASCII-арт в текстовый файл с именем `ascii_image.txt`. 
___
## Создание Dockerfile.

### 1. Общее описание выполненных действий
Как уже было указано выше, в начале работы по созданию образов Docker возникла дилемма: какой из дистрибутивов Linux использовать. По имеющейся информации в сети, наибольшей популярности пользуются:
  - `Debian` в виду стабильности и обширности репозитория;
  - `Ubuntu` в виду большей дружелюбности интерфейса по сравнению с `Debian`, при должной стабильности, обновляемости и обширности репозитория;
  - `Alpine linux` в виду своей минималистичности, безопасности и скорости работы.

И если с распределением сфер использования `Debian` и `Ubuntu` все понятно, то с использованием образов на `Alpine linux` для приложений на `Python` [имеются значительные разногласия](https://habr.com/ru/articles/707858/). Таким образом, в целях подробного изучения особенностей использования `Alpine linux` и `Ubuntu` для развертывания Python-приложений, были выбраны данные два дистрибутива. По условиям проекта данная часть была поручена сотруднику Git-tester1 и создавалась в ветви `docker-container`. После окончания работы и утверждения результатов, Git-tester1 сформировал запрос на слияние, который был одобрен, после чего произведено слияние ветви `docker-container` и ветви `dev`. Ветвь `docker-container` не удалялась для контроля выполненных действий.

### 2. Dockerfile для Alpine-образа
```dockerfile
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
```

#### Описание Dockerfile для Alpine-образа

- **Базовый образ**
```dockerfile
FROM python:3.12-alpine
```
Эта строка указывает базовый образ для контейнера, которым является `python:3.12-alpine`, содержащий в себе Python 3.12 и Alpine Linux.

- **Установка системных зависимостей**
```dockerfile
RUN apk add --no-cache \
    build-base \
    python3-dev \
    libjpeg-turbo-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    tiff-dev
```
Здесь команда `RUN` устанавливает несколько системных зависимостей с помощью менеджера пакетов Alpine, `apk`. Опция `--no-cache` предотвращает кэширование индекса пакетов, что помогает уменьшить размер образа. Подробнее об используемых зависимостях можно узнать [на странице Wiki данного репозитория](https://github.com/al-sapsan/skill-docker/wiki/6.-ASCII%E2%80%90art-зависимости).

- **Зависимости Python**
```dockerfile
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir pillow
```
В этом разделе обновляется `pip` до последней версии и устанавливается библиотека Pillow без кэширования файлов. Опция `--no-cache-dir` используется для уменьшения окончательного размера образа за счет того, что загруженные пакеты не сохраняются в кэше.

- **Рабочая директория**
```dockerfile
WORKDIR /app
```
Инструкция `WORKDIR` устанавливает рабочую директорию `/app` внутри контейнера. Это означает, что все последующие команды будут выполняться в этой директории.

- **Копирование файлов приложения**
```dockerfile
COPY . /app
```
Эта команда копирует все файлы из текущей директории на хост-машине в директорию `/app` в контейнере. В данном случае это - файлы `ascii-art.py` и `drone.jpeg`.

- **Команда для запуска приложения**
```dockerfile
CMD ["python", "ascii-art.py"]
```
Эта строка указывает команду, которая будет выполняться при запуске контейнера из этого образа. 

### 3. Dockerfile для Ubuntu-образа
```dockerfile
# Используем базовый образ Ubuntu 22.04
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
```

#### Описание Dockerfile для Ubuntu-образа

- **Базовый образ**
```dockerfile
FROM ubuntu:22.04
```
В данном случае используется базовый образ Ubuntu версии 22.04. 

- **Установка системных зависимостей**
```dockerfile
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
```
Здесь команда `RUN` обновляет список пакетов с помощью `apt-get update`, устанавливает необходимые пакеты для работы с `Python`, библиотекой `Pillow` и библиотеки для работы с различными форматами изображений (JPEG, PNG, TIFF и т.д.). После установки пакетов выполняется очистка кэша и удаление временных файлов для уменьшения размера образа. Подробнее об используемых зависимостях можно узнать [на странице Wiki данного репозитория](https://github.com/al-sapsan/skill-docker/wiki/6.-ASCII%E2%80%90art-зависимости).

- **Установка Python-зависимостей**
```dockerfile
RUN pip install --no-cache-dir pillow
```
Здесь непосредственно устанавливается библиотека Pillow, которая используется для обработки изображений. 

- **Создание рабочей директории**
```dockerfile
WORKDIR /app
```
Эта команда создает рабочую директорию `/app` внутри контейнера и устанавливает её как текущую директорию для последующих команд.

- **Копирование файлов программы в контейнер**
```dockerfile
COPY . /app
```
Эта команда копирует все файлы из текущей директории на хост-машине в директорию `/app` в контейнере. В данном случае это - файлы `ascii-art.py` и `drone.jpeg`.

- **Указание команды для запуска программы**
```dockerfile
CMD ["python3", "ascii-art.py"]
```
Эта команда указывает, что при запуске контейнера будет выполнен скрипт `ascii-art.py` с использованием интерпретатора Python 3.

___
## Сборка Docker-образов из созданных Dockerfile

### 1. Описание процесса сборки

### 2. Тестирование Python-приложения в Docker-контейнере

### 3. Публикация результатов проделанной работы

### 4. Анализ результатов

___
## Работа с Docker Compose.

### 1. Общее описание выполненных действий


### 2. Docker-compose.yml для Alpine-образа
```dockerfile
services:       # Определяем сервисы
  ascii-art:         # Название сервиса (можно выбрать любое)
    image: ascii-art-a  # Указываем образ, из которого будет создан контейнер
```
#### Описание Docker-compose.yml для Alpine-образа


### 3. Docker-compose.yml для Ubuntu-образа
```dockerfile
services:       # Определяем сервисы
  ascii-art:         # Название сервиса (можно выбрать любое)
    image: ascii-art-u  # Указываем образ, из которого будет создан контейнер
```

#### Описание Docker-compose.yml для Ubuntu-образа




