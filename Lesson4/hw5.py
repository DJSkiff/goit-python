import os
import sys

# Filters for known files

imagesFilters = ['jpg', 'png', 'jpeg']

videoFilters = ['avi', 'mp4', 'mov']

docFilters = ['pdf', 'docx', 'txt']

musicFilters = ['mp3', 'ogg', 'wav', 'amr']

arhiveFilters = ['zip', '7zip', 'gz', 'tar']


def printFile(filesDict):

    for key, value in filesDict.items():

        if type(value) is str:

            print(f'{key} :')

            print(f'    {value}')

        else:

            if not value:

                continue  # if not value in collections skip it

            print(f'    {key}:')

            for v in value:

                print(f'        {v}')


def fileDistribute(fileCollections, path, nestingDeep):

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

    if nestingDeep > 0:

        allFiles['Вложенная папка'] = path

    else:

        allFiles[f'Стартовый путь'] = path

    allFiles['Изображения'] = images

    allFiles['Видео'] = videos

    allFiles['Документы'] = docs

    allFiles['Музыка'] = musics

    allFiles['Архивы'] = archivs

    allFiles['Другие файлы'] = others

    allFiles['Все расширения'] = set(fileExtensions)

    printFile(allFiles)

# initialise structures for find files


def grabPath(path, nestingDeep=0):

    fileCollections = []

    for file in os.listdir(path):

        if os.path.isdir(os.path.join(path, file)):

            grabPath(os.path.join(path, file), nestingDeep + 1)

        else:

            fileCollections.append(file)

    fileDistribute(fileCollections, path, nestingDeep)


def main():

    # 'C:\Users\vdunk\Desktop\Trash' sys.argv[1]
    grabPath(sys.argv[1])


if __name__ == '__main__':
    main()
