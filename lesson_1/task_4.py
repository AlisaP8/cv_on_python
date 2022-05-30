def perc(val):
    S = C
    res = S / 100.0 * val / 12
    return res


def total_sum(num, month):
    if num in range(1000, 10000):
        if 6 <= month < 12:
            val = 5
            return val
        elif 12 <= month < 24:
            val = 6
            return val
        elif 24 <= month:
            val = 5.5
            return val
        else:
            print('Ошибка')
    elif num in range(10000, 100000):
        if 6 <= month < 12:
            val = 6
            return val
        elif 12 <= month < 24:
            val = 7
            return val
        elif 24 <= month:
            val = 6.5
            return val
        else:
            print('Ошибка')
    elif num in range(100000, 1000000):
        if 6 <= month < 12:
            val = 7
            return val
        elif 12 <= month < 24:
            val = 8
            return val
        elif 24 <= month:
            val = 7.5
            return val
        else:
            print('Ошибка')
    else:
        print('На данную сумму вклад открыть нельзя')


C = int(input("Введите начальную сумму вклада "))
n = int(input("На сколько месяцев? "))

func = number(C, n)
percent = perc(func)
S = C
result = percent * n + S
print(f'за месяц начислено процентов: {percent}\n'
      f'Количество денег через {n}', 'месяцев составит {:.2f} рублей'.format(result))
