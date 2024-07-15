import os

def count_images(folder_path):
    if not os.path.isdir(folder_path):
        print("O caminho especificado não é um diretório válido.")
        return

    image_count = 0
    files = os.listdir(folder_path)

    for file_name in files:
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            image_count += 1

    return image_count

german_folder_path = "D:\\.Dataset28022024 - TCC\\labels\\german"
indian_folder_path = "D:\\.Dataset28022024 - TCC\\labels\\indian"
japanese_folder_path = "D:\\.Dataset28022024 - TCC\\labels\\japanese"
spanish_folder_path = "D:\\.Dataset28022024 - TCC\\labels\\spanish"

# german_folder_path = "D:\\.Dataset28022024 - TCC - Copia Pequena\\german"
# indian_folder_path = "D:\\.Dataset28022024 - TCC - Copia Pequena\\indian"
# japanese_folder_path = "D:\\.Dataset28022024 - TCC - Copia Pequena\\japanese"
# spanish_folder_path = "D:\\.Dataset28022024 - TCC - Copia Pequena\\spanish"

num_images_german = count_images(german_folder_path)
num_images_indian = count_images(indian_folder_path)
num_images_japanese = count_images(japanese_folder_path)
num_images_spanish = count_images(spanish_folder_path)

print(f"O número de imagens german são: {num_images_german}")
print(f"O número de imagens indian são: {num_images_indian}")
print(f"O número de imagens japanese são: {num_images_japanese}")
print(f"O número de imagens spanish são: {num_images_spanish}")