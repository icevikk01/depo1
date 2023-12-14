import os
import random
from PIL import Image

def process_random_image(directory_path, output_directory):
    # Dizin içindeki tüm dosyaları kontrol et
    image_files = [filename for filename in os.listdir(directory_path) if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Rastgele bir görüntü seç
    if image_files:
        selected_image = random.choice(image_files)
        image_path = os.path.join(directory_path, selected_image)

        # Yeni klasörü kontrol et ve yoksa oluştur
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Yeni dosyanın yolu
        output_file = os.path.join(output_directory, f"{selected_image.split('.')[0]}_hex.txt")

        # Görüntü adını dosyaya yaz
        with open(output_file, 'w') as file:
            file.write(f"=== {selected_image} ===\n")

            # Görüntüyü aç
            image = Image.open(image_path)

            # Görüntüyü RGB moduna dönüştür
            rgb_image = image.convert('RGB')

            # Görüntü boyutlarını al
            width, height = rgb_image.size

            # Her pikselin hex değerini dosyaya yaz
            for y in range(height):
                for x in range(width):
                    r, g, b = rgb_image.getpixel((x, y))
                    hex_value = '{:02X}  {:02X}  {:02X}'.format(r, g, b)
                    file.write(hex_value + '\n')

        print(f"Seçilen rastgele görüntü: {selected_image}")
        print(f"Hexadecimal değerler {output_file} dosyasına yazıldı.")
    else:
        print("Dizin içinde uygun bir görüntü bulunamadı.")

# Örnek kullanım
input_directory = '..\pythongörüntüişleme\images'
output_directory = '..\pythongörüntüişleme\outputs'
process_random_image(input_directory, output_directory)
