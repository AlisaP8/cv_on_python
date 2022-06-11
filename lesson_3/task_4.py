import os
import random
import string


def get_file():
    path_m = os.path.abspath('test.txt')
    if os.path.exists(path_m):
        print('Файл уже существует')
    else:
        with open('test.txt', 'a+', encoding='utf-8') as f:
            # list1 = ['first', 'second', 'third']
            # list1 = ''.join(list(map(chr, [random.randint(65, 90) for _ in range(30)])))
            list1 = set()
            while len(list1) < 5:
                list1.add(''.join(random.choice(string.ascii_lowercase) for _ in range(3, 10)))
            # list2 = [1, 2, 3]
            list2 = [random.randint(0, 10000) for _ in range(10)]
            file = zip(list1, list2)
            for el in file:
                f.write(f'{el[0]}{el[1]}\n')
            f.close()
        return


def call_det_name():
    with open('test.txt', 'r', encoding='utf-8') as file:
        try:
            for line in file:
                print(line)
        finally:
            file.close()


get_file()
call_det_name()
