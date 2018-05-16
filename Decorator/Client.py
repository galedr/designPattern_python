from SimpleCalculate import *
from ComplexCalculate import *
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
method1 = AddMethod(num1, num2)
method2 = SquareMethod()
print(method2.calculate(method1))