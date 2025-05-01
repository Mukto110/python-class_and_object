class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove_item(self, item_name):
        for product in self.cart:
            if (product['item'] == item_name):
                self.cart.remove(product)
                print(f'{item_name} removed from cart')
                return
        print(f'{item_name} not found in cart')        
        
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            print(item)
            item_total = item['price'] * item['quantity']
            total += item_total
            print(f"Item Total: {item_total}")
        print(f"Final Total: {total}")

        if amount < total:
            print(f'You do not have sufficient balance')
        else:
            remaining = amount - total
            print(f'here is your change: ', remaining)    

mukto = Shopping("Mukto")
mukto.add_to_cart("mobile", 10000, 5)
mukto.add_to_cart("computer", 50000, 4)
mukto.add_to_cart("laptop", 80000, 6)

mukto.remove_item("laptop")

print(mukto.cart)