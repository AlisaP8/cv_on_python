class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_parent_data(self):
        print(f'{self.name} {self.price}')


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        super().get_parent_data()
        print(f'{self.price}')


num1 = ItemDiscount('TV', 250)
num1.get_parent_data()
num2 = ItemDiscountReport('TV', 300)
num2.get_parent_data()

