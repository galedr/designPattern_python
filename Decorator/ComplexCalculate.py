class IComplex():
    def calculate(self, simple):
        pass


class SquareMethod(IComplex):
    def calculate(self, simple):
        return simple.calculate() * simple.calculate()


class RootMethod(IComplex):
    def calculate(self, simple):
        return simple.calculate() ** 0.5
