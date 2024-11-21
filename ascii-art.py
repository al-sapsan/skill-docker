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
path = "~/drone.jpeg"
ascii_art = convert_image_to_ascii(path)
print(ascii_art)

# Saving the obtained result to a file
with open("ascii_image.txt", "w") as f:
    f.write(ascii_art)
