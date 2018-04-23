# In computer programming, the strategy pattern (also known as the policy pattern) is a
# behavioral software design pattern that enables selecting an algorithm at runtime.
# Instead of implementing a single algorithm directly, code receives run-time instructions
# as to which in a family of algorithms to use.
# See more in wiki: https://en.wikipedia.org/wiki/Strategy_pattern
#
# We will use Strategy Pattern to design a calculation system which support + - * /.

class Calculation_Strategy(object):
    def apply_strategy(self, num1, num2):
        pass

class Adder(Calculation_Strategy):
    def apply_strategy(self, num1, num2):
        return (num1 + num2)

class Substract(Calculation_Strategy):
    def apply_strategy(self, num1, num2):
        return (num1 - num2)

class Multiply(Calculation_Strategy):
    def apply_strategy(self, num1, num2):
        return (num1 * num2)

class Divide(Calculation_Strategy):
    def apply_strategy(self, num1, num2):
        return (num1 / num2)

class Context():
    def __init__(self, strategy):
        self._strategy = strategy

    def apply_strategy(self, num1, num2):
        return self._strategy.apply_strategy(num1, num2)

if __name__ == '__main__':
    context1 = Context(Adder())
    print("10 + 5 = %d\n" %(context1.apply_strategy(10, 5)))

    context2 = Context(Substract())
    print("10 - 5 = %d\n" %(context2.apply_strategy(10, 5)))

    context3 = Context(Multiply())
    print("10 * 5 = %d\n" %(context3.apply_strategy(10, 5)))

    context4 = Context(Divide())
    print("10 / 5 = %d\n" %(context4.apply_strategy(10, 5)))
