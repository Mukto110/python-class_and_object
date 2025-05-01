class Shop:
    cart = [] # Here cart is a class attribute 

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


puppu = Shop("Puppu")
puppu.add_to_card("makeup")
puppu.add_to_card("lipstick")
puppu.add_to_card("face wash")

print(puppu.cart)