import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = 'C:/Users/vdunk/Desktop/Trash'  # sys.argv[1]

# Filters for known files

imagesFilters = ['jpg', 'png', 'jpeg']

videoFilters = ['avi', 'mp4', 'mov']

docFilters = ['pdf', 'docx', 'txt']

musicFilters = ['mp3', 'ogg', 'wav', 'amr']

arhiveFilters = ['zip', '7zip', 'gz', 'tar']

# print all collections in terminal


def printFile(filesDict):

    for key, value in filesDict.items():
        if type(value) is str:
            print(f'{key} :')
            print(f'    {value}')
        else:
            print(f'    {key}:')
            for v in value:
                print(f'        {v}')


def fileDistribute(fileCollections, path):

    fileExtensions = []

    images = []

    videos = []

    docs = []

    musics = []

    archivs = []

    others = []

    allFiles = {}

    for file in fileCollections:

        fileExtension = file.rsplit('.')[1]

        fileExtensions.append(fileExtension)

        if fileExtension in imagesFilters:
            images.append(file)
        elif fileExtension in videoFilters:
            videos.append(file)
        elif fileExtension in docFilters:
            docs.append(file)
        elif fileExtension in musicFilters:
            musics.append(file)
        elif fileExtension in arhiveFilters:
            archivs.append(file)
        else:
            others.append(file)

    allFiles['Текущая папка'] = path
    allFiles['Изображения'] = images
    allFiles['Видео'] = videos
    allFiles['Документы'] = docs
    allFiles['Музыка'] = musics
    allFiles['Архивы'] = archivs
    allFiles['Другие файлы'] = others
    allFiles['Все расширения'] = fileExtensions

    printFile(allFiles)

# initialise structures for find files


def grabPath(path):
    fileCollections = []
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            grabPath(os.path.join(path, file))
        else:

            fileCollections.append(file)

    fileDistribute(fileCollections, path)


def main():

    grabPath(path)


if __name__ == '__main__':
    main()
