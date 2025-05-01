class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_card(self, item):
        self.cart.append(item)


mukto = Shop("Mukto")
mukto.add_to_card("watch")
mukto.add_to_card("shoe")
mukto.add_to_card("laptop")
mukto.add_to_card("mobile")

print(mukto.cart)


sabbir = Shop("Puppu")
sabbir.add_to_card("makeup")
sabbir.add_to_card("lipstick")
sabbir.add_to_card("face wash")

print(sabbir.cart)