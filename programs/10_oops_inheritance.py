from oops_class import Calculator


class ChildClass(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def get_complete_data(self):
        return self.num2 + self.num + self.add_numbers()


obj = ChildClass()
print(obj.get_complete_data())
