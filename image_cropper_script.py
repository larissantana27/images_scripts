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

def crop_images_left(folder_path, output_folder_path, crop_size):
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

            # Definir as coordenadas de recorte (mantendo a margem à esquerda fixa)
            left = crop_size
            right = width
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

def crop_images_right(folder_path, output_folder_path, crop_size):
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

            # Definir as coordenadas de recorte (mantendo a margem à esquerda fixa)
            left = 0
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


# folder_path = "D:\\.Dataset10022024 - TCC\spanish\\699-770. vivalaferia"
# folder_path = "D:\\.Dataset10022024 - TCC\spanish\\771-917. tamaraflamenco"
# folder_path = "D:\\.Dataset10022024 - TCC\spanish\\1016-1056. ytutanflamenca"
# folder_path = "D:\\.Dataset10022024 - TCC\\spanish\\test"
# folder_path = "D:\\.Dataset10022024 - TCC\\japanese\\test\\cut_left"
# folder_path = "D:\\.Dataset10022024 - TCC\\japanese\\test\\cut_right"
# folder_path = "D:\\.Dataset10022024 - TCC\\japanese\\test\\cut_center"
# folder_path = "D:\\.Dataset10022024 - TCC\\german\\test\\cut_center"
folder_path = "D:\\.Dataset10022024 - TCC\\spanish\\test\\cut_center"

# output_folder_path = "D:\\.Dataset28022024 - TCC\\spanish"
# output_folder_path = "D:\\.Dataset10022024 - TCC\\japanese\\test\\cut_left\\result"
# output_folder_path = "D:\\.Dataset10022024 - TCC\\japanese\\test\\cut_right\\result"
# output_folder_path = "D:\\.Dataset10022024 - TCC\\japanese\\test\\cut_center\\result"
# output_folder_path = "D:\\.Dataset10022024 - TCC\\german\\test\\cut_center\\result"
output_folder_path = "D:\\.Dataset10022024 - TCC\\spanish\\test\\cut_center\\result"


crop_size = 34
# crop_size = 50
# crop_size = 68
# crop_size = 72
# crop_size = 140
# crop_size = 90

crop_images(folder_path, output_folder_path, crop_size)
# crop_images_left(folder_path, output_folder_path, crop_size)
# crop_images_right(folder_path, output_folder_path, crop_size)
