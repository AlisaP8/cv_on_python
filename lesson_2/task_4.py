class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, disc):
        super().__init__(name, price)
        self.disc = disc

    def __str__(self):
        return f'Сумма без скидки: ${self.price}, сумма со скидкой в {self.disc}%: ${self.get_total()}'

    def get_total(self):
        res = self.price - self.price * self.disc / 100
        return res


num1 = ItemDiscount('TV', 250)
# print(num1)
num2 = ItemDiscountReport('TV', 250, 10)
print(num2)
num2.__str__()
