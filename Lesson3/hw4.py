import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]  # 'C:/Users/vdunk/Desktop/Trash'
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

# initialise structures for find files
fileExtensions = []
images = []
videos = []
docs = []
musics = []
others = []

# main parts of the program

for file in files:
    # split file in list files into name and extension
    fileName, fileExtension = file.split(".")

    # collect all file extension in list fileExtensions

    fileExtensions.append(fileExtension.lower())

    # distribute to collections by extension

    if "jpg" in fileExtension or "png" in fileExtension or "jpeg" in fileExtension:
        images.append(file)
    elif "avi" in fileExtension or "mp4" in fileExtension or "mov" in fileExtension:
        videos.append(file)
    elif "pdf" in fileExtension or "docx" in fileExtension or "txt" in fileExtension:
        docs.append(file)
    elif "mp3" in fileExtension or "ogg" in fileExtension or "wav" in fileExtension or "amr" in fileExtension:
        musics.append(file)

# print all collections in terminal

print("Файлы в категории 'Изображения': ")

for file in images:
    print(f'    {file}')

print("Файлы в категории 'Видео': ")

for file in videos:
    print(f'    {file}')

print("Файлы в категории 'Документы': ")

for file in docs:
    print(f'    {file}')

print("Файлы в категории 'Музыка': ")

for file in musics:
    print(f'    {file}')

print("Папки и файлы вне категорий: ")

for file in list(set(files) ^ set(images + videos + docs + musics)):
    print(f'    {file}')

print("Список всех расширений: ")

for file in set(fileExtensions):
    # if file:  # discard subfolders
    print(f'    {file}')
