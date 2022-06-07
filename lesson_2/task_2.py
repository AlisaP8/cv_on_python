class ItemDiscount:
    def __init__(self, name, price):
        self._ItemDiscount__name = name
        self._ItemDiscount__price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'{self._ItemDiscount__name} {self._ItemDiscount__price}')


num1 = ItemDiscount('TV', 300)
num2 = ItemDiscountReport('TV', 300)
num2.get_parent_data()

