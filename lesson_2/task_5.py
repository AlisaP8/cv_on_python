class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport1(ItemDiscount):
    def get_info(self):
        print(f'{self.name}')


class ItemDiscountReport2(ItemDiscount):
    def get_info(self):
        print(f'{self.price}')


num1 = ItemDiscountReport1('TV', 300)
num1.get_info()
num2 = ItemDiscountReport2('TV', 300)
num2.get_info()
