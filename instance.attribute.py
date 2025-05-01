class Shop:
    shopping_mall = "Bashundhara"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # here card is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


buyer_mukto = Shop("Mukto")
buyer_mukto.add_to_cart("Juta")
buyer_mukto.add_to_cart("ghori")
buyer_mukto.add_to_cart("bag")

print("Mukto's Product: ", buyer_mukto.cart)

buyer_puppu = Shop("Puppu")
buyer_puppu.add_to_cart("makeup")
buyer_puppu.add_to_cart("lipstick")
buyer_puppu.add_to_cart("heel")

print("Puppu's product: ", buyer_puppu.cart)
