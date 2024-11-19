from PIL import Image

# Задаем символы ASCII, которые будут использоваться для создания арта
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Функция для изменения размера изображения
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Преобразуем изображение в оттенки серого
def edit_grayscale_image(image):
    return image.convert("L")

# Сопоставляем каждый пиксель с символом ASCII
def edit_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

# Основная функция
def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    # Изменение размера и преобразование в оттенки серого
    image = resize_image(image, new_width)
    image = edit_grayscale_image(image)
    
    # Преобразуем пиксели в ASCII
    ascii_str = edit_pixels_to_ascii(image)
    
    # Форматируем строку ASCII для правильного отображения
    img_width = image.width
    ascii_art = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_art += ascii_str[i:i + img_width] + "\n"
    
    return ascii_art

# Пример использования
path = "/Users/a2141/al-sapsan-git/skill-docker/drone.jpeg"
ascii_art = convert_image_to_ascii(path)
print(ascii_art)

# Если вы хотите сохранить ASCII-арт в файл:
with open("ascii_image.txt", "w") as f:
    f.write(ascii_art)
