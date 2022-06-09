import os


def get_file():
    path_m = os.path.abspath('test.txt')
    if os.path.exists(path_m):
        print('Файл уже существует')
    else:
        with open('test.txt', 'a+', encoding='utf-8') as f:
            lines1 = ['first', 'second', 'third']
            lines2 = [1, 2, 3]
            # f.writelines("%s\n" % line for line in (lines1, lines2))
            n = zip(lines1, lines2)
            # print(n)
            for el in n:
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

