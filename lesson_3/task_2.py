def get_float(num):
    pass


def get_num():
    while True:
        num = input('Введите число: ')
        try:
            if int(num):
                print(f'{num} - целое число')
                continue
        except:
            break
    return get_float(num)


# def get_num():
#     num = input('Введите число: ')
#     try:
#         if int(num):
#             return f'{num} - целое число'
#     except:
#         return get_float(num)


print(get_num())
