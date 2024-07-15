import os
import random
import shutil

german_folder_path = "D:\\.Dataset05032024 - TCC\\labels\\german"
indian_folder_path = "D:\\.Dataset05032024 - TCC\\labels\\indian"
japanese_folder_path = "D:\\.Dataset05032024 - TCC\\labels\\japanese"
spanish_folder_path = "D:\\.Dataset05032024 - TCC\\labels\\spanish"

def shuffle_images(folder_path):
    if not os.path.isdir(folder_path):
        print("O caminho especificado não é um diretório válido.")
        return

    files = os.listdir(folder_path)
    random.shuffle(files)

    for index, file_name in enumerate(files, start=0):
        file_path = os.path.join(folder_path, file_name)
        new_file_name = f"image_{index + 1}.jpg"
        new_file_path = os.path.join(folder_path, new_file_name)
        shutil.move(file_path, new_file_path)
        print(f"Arquivo {file_name} movido para {new_file_name}")

# shuffle_images(german_folder_path)
# shuffle_images(indian_folder_path)
# shuffle_images(japanese_folder_path)
shuffle_images(spanish_folder_path)