class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'{self.name} {self.price}')


num1 = ItemDiscount('TV', 300)
num2 = ItemDiscountReport('TV', 300)
num2.get_parent_data()

