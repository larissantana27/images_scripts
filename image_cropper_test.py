from PIL import Image
import os

def crop_images(folder_path, output_folder_path, crop_size):
    # Verificar se o caminho especificado é um diretório válido
    if not os.path.isdir(folder_path):
        print("O caminho especificado não é um diretório válido.")
        return

    # Verificar se o caminho especificado é um diretório válido para a pasta de saída
    if not os.path.isdir(output_folder_path):
        print("O caminho especificado para a pasta de saída não é um diretório válido.")
        return

    # Listar todos os arquivos no diretório
    files = os.listdir(folder_path)

    # Loop através de cada arquivo na pasta
    for file_name in files:
        # Verificar se o arquivo é uma imagem (você pode adicionar mais extensões de arquivo, se necessário)
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            # Abrir a imagem
            image_path = os.path.join(folder_path, file_name)
            image = Image.open(image_path)

            # Obter as dimensões originais da imagem
            width, height = image.size

            # Definir as coordenadas de recorte
            left = crop_size
            right = width - crop_size
            top = 0
            bottom = height

            # Recortar a imagem
            cropped_image = image.crop((left, top, right, bottom))
            # Converter a imagem para o modo RGB antes de salvar como JPEG
            cropped_image = cropped_image.convert("RGB")

            # Salvar a imagem recortada no novo local
            output_path = os.path.join(output_folder_path, f"cropped_{file_name}")
            cropped_image.save(output_path)

            print(f"Imagem {file_name} recortada e salva em {output_path}.")
            folder_path = "C:\\Users\\Larissa Santana\\Pictures\\tcc"

def calculate_crop_size(image_path, target_horizontal_dim = 375):
    image = Image.open(image_path)
    width, height = image.size
    crop_width = target_horizontal_dim # Calculate the crop width based on the target horizontal dimension
    crop_height = int(height * (crop_width / width)) # Calculate the crop height to maintain aspect ratio
    
    return crop_width, crop_height

folder_path = "C:\\Users\\Larissa Santana\\Pictures\\tcc"
output_folder_path = "C:\\Users\\Larissa Santana\\Pictures\\tcc\\result"

for image_path in folder_path:

    crop_width, crop_height = calculate_crop_size(image_path, target_horizontal_dim=375)
    print("Crop width:", crop_width)
    print("Crop height:", crop_height)

    crop_images(folder_path, output_folder_path, crop_width)