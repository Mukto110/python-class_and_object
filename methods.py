class Phone:
    model = "Samsung A24"
    brand = "Samsung"
    color = "White"
    features = ['Camera', 'AI Voice Control', "Speaker"]
    price = 17000

    def call(self):
        print("Calling someone")

    def send_sms(self, number, sms):
        text = f'sending sms to: {number} and message: {sms}'
        return text    


my_phone = Phone()

number = "+8801642321506"
sms = "Ei gaan ti sunte dial korun 123 and 2 taka projojjo"

print(my_phone.send_sms(number, sms))