# Self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required while creating object

class Calculator:
    num = 100

    # to declare construct use __init__
    def __init__(self, a, b):
        print("I'm in constructor")
        self.a = a
        self.b = b

    def get_data(self):
        print("calling method \n")

    def add_numbers(self):
        return self.a + self.b + self.num


# Calculator().get_data()
# obj = Calculator()
# obj.get_data()
# print(obj.num)

obj1 = Calculator(2, 3)
print(obj1.add_numbers())
print(obj1.num)
