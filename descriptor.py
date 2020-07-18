class Value:

    def __init__(self):
        pass

    def __set__(self, obj, value):
        self.value = value
        self.value = self.value - (self.value * obj.commission)

    def __get__(self, obj, obj_type):
        return int(self.value)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

new_acc = Account(0.1)
new_acc.amount = 100
print(new_acc.amount)