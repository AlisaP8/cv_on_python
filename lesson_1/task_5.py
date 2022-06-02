from lesson_1.task_4 import total_sum, start_sum, perc, func, summ, month

quantity = int(input('Введите сумму пополнения \n'))


def get_summ(start_sum, month, quan):
    i = 0
    if quan == 0:
        res = perc(func)
        return res

    while True:
        for i in range(month - 1):
            i *= quan
        break
    return i


summ_quan = get_summ(start_sum, month, quantity)
res = total_sum(start_sum, month)


def quantity(val, percent):
    try:
        res = start_sum / 100.0 * percent / 12
        item = val / (month - 2) / 100.0 * res / 12
        result = res * month + item + start_sum + val
        print(f'Итоговая сумма через {month}', 'месяцев составит {:.2f} рублей'.format(result))
    except TypeError:
        print('Некорректные данные')


quantity(summ_quan, res)
