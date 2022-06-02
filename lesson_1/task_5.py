from lesson_1.task_4 import total_sum, start_sum, perc, func, summ, month

quantity = int(input('Введите сумму пополнения \n'))


def get_summ(start_sum, month, quan):
    i = 0
    if quan == 0:
        res = perc(func)
        return res

    while True:
        for i in range(month):
            i *= quan
        break
    return i


summ_quan = get_summ(start_sum, month, quantity)
res = total_sum(start_sum, month)


def quantity(val, percent):
    try:
        res = start_sum / 100.0 * percent / 12
        item = res * val
        result = res * month + val * item + start_sum
        print(f'Итоговая сумма через {month}', 'месяцев составит {:.2f} рублей'.format(result))
        # return result
    except TypeError:
        # pass
        print('Некорректные данные')


# quantity(summ_quan, res)

print(quantity(summ_quan, res))
