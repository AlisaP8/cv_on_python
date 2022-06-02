start_sum = int(input("Введите начальную сумму вклада \n"))
month = int(input("На сколько месяцев? \n"))
summ = start_sum


def perc(val):
    try:
        res = summ / 100.0 * val / 12
        result = res * month + summ
        print(f'За месяц начислено процентов: {res:.2f}\n'
              f'Сумма денег через {month}', 'месяцев составит {:.2f} рублей'.format(result))
    except TypeError:
        print('Некорректные данные')


def total_sum(num, month):
    try:
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
                print('Некорректный срок вклада')
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
                print('Некорректный срок вклада')
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
                print('Некорректный срок вклада')
    except (TypeError, ValueError):
        pass


func = total_sum(start_sum, month)
percent = perc(func)
