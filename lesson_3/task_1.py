import os
from os import path
from pathlib import Path

# file = open('test.txt', 'w+', encoding='utf-8')
# file2 = open('test.tar.gz', 'w+', encoding='utf-8')
# my_path = os.path.abspath('text.txt')
# my_path2 = os.path.abspath('test.tar.gz')


# print(my_path)
# file = os.path.basename(my_path).split('.')[0]
# print(file)


# def get_file(file, my_path):
#     if file in range(my_path):
#         my_file = os.path.splitext(file)


class GetFile:

    @staticmethod
    def get_file_ext(file):
        if file is None or file == '':
            return f'Данный файл не имеет расширения'
        else:
            paths = os.path.splitext(file)
            ext = paths[1]
            my_file = paths[0]
            if ext != '':
                return GetFile.get_file_ext(my_file)
            else:
                return my_file


a = GetFile.get_file_ext(file='test.tar.gz')
b = GetFile.get_file_ext(file='test.txt')
c = GetFile.get_file_ext(file='')
print(a)
print(b)
print(c)
