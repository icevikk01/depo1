import os
from PIL import Image

image_path = '..\pythongörüntüişleme\images\spiderMAN.png'
image_name = os.path.basename(image_path)
output_directory = '..\pythongörüntüişleme\outputs'
output_file = os.path.join(output_directory, f"{image_name.split('.')[0]}_hex.txt")

def image_to_hex(image_path, output_directory):
    # Görüntüyü aç
    image = Image.open(image_path)

    # Görüntüyü RGB moduna dönüştür
    rgb_image = image.convert('RGB')

    # Görüntü boyutlarını al
    width, height = rgb_image.size

    # Her pikselin hex değerini dosyaya yaz
    with open(output_file, 'w') as file:
        for y in range(height):
            for x in range(width):
                r, g, b = rgb_image.getpixel((x, y))
                hex_value = '{:02X}  {:02X}  {:02X}'.format(r, g, b)
                file.write(hex_value + '\n')


image_to_hex(image_path, output_file)

