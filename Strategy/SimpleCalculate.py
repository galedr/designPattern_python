class ISimple():
    def calculate(self):
        pass


class AddMethod(ISimple):
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def calculate(self):
        return self._num1 + self._num2


class MinusMethod(ISimple):
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def calculate(self):
        return self._num1 - self._num2
