class shop:
    def __init__(self, sweet, price):
        self.sweet = sweet
        self.price = price

    def ship(self):
        print("shiping product")


    def add_item(self, amount):
        print("Item Added")


my_shop = shop(sweet = 5, price = 999)

my_shop.add_item(500)