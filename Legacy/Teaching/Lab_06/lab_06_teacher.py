from abc import ABC, abstractmethod
import time

# Írjunk egy logoló wrappert, amely kiírja a függvény nevét, a bemeneti paramétereket és a visszatérési értéket és kiszámolja
# a függvény futásának idejét.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print(f"Function {func.__name__} called with arguments {args} {kwargs} returned {result}")
        print(f"Execution time: {time_end - time_start:.4f} seconds")
        return result
    return wrapper

# Hozzunk létre egy MathTask absztrakt osztályt, amelynek van egy solve metódusa, amelyet a leszármazottak implementálnak.
# @abstractmethod

class MathTask(ABC):
    @abstractmethod
    def solve(self):
        pass

# Hozzunk létre egy AdditionTask osztályt, amely a MathTask osztályból származik és implementálja a solve metódust.
# Az osztályon belül alkalmazzuk a log_decorator dekorátort.
class AdditionTask(MathTask):
    @log_decorator
    def solve(self, a, b):
        return a + b

# Hozzunk létre egy MultiplicationTask osztályt, amely a MathTask osztályból származik és implementálja a solve metódust.
# Az osztályon belül alkalmazzuk a log_decorator dekorátort.
class MultiplicationTask(MathTask):
    @log_decorator
    def solve(self, a, b):
        return a * b

from sympy import *
class DerivationTask(MathTask):
    @log_decorator
    def solve(self, f, x):
        expr_diff = Derivative(f, x)
        return expr_diff.doit()

# Example usage

add_task = AdditionTask()
print(add_task.solve(3, 4))
multiply_task = MultiplicationTask()
print(multiply_task.solve(3, 4))
derivation_task = DerivationTask()
x,y = symbols('x y')
print(derivation_task.solve(x**4 + 3*y**3, x))