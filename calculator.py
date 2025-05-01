class Calculator: 
    brand = "Casio MS990"

    def add(self, num1, num2):
        result = num1 + num2
        return result
    
    def sub(self, num1, num2):
        result = num1 - num2
        return result
    
    def multi(self, num1, num2):
        result = num1 * num2
        return result
    
    def div(self, num1, num2):
        result = num1 / num2
        return result
    

my_calc = Calculator()

print(my_calc.add(4,5))
print(my_calc.sub(5,4))
print(my_calc.multi(2,2))
print(my_calc.div(9,3))