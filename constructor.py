class Phone:
    manufactured = "China"

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, number, sms):
        text = f'{sms} from {number} this number'
        print(text)


my_phone = Phone("Mukto", "Xaomi", 200000)

# print(my_phone.price)

another_phone = Phone("Puppu", "Redmi", 27000)

print(another_phone.owner)
print(another_phone.brand)