# In object-oriented programming, the command pattern is a behavioral design pattern
# in which an object is used to encapsulate all information needed to perform
# an action or trigger an event at a later time. This information includes
# the method name, the object that owns the method and values for the method parameters..
# See more in wiki: https://en.wikipedia.org/wiki/Command_pattern
#
# We are going to implement command pattern which save command set
# of plotting different shape.

import math
import matplotlib.pyplot as plt

class Circle():
    def __init__(self, rad):
        self.rad = rad

    def plot_circle(self):
        plt.fill([math.cos(2 * math.pi / 100 * x) * self.rad for x in range(0, 101)],
                 [math.sin(2 * math.pi / 100 * x) * self.rad for x in range(0, 101)],
                 'r')
        plt.xlim([-5, 5])
        plt.ylim([-5, 5])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

if __name__ == "__main__":
    command_stack = []

    # commands are just pushed into the command stack
    command_stack.append(Circle(rad=1))
    command_stack.append(Circle(rad=2))
    command_stack.append(Circle(rad=3))
    command_stack.append(Circle(rad=4))
    command_stack.append(Circle(rad=5))

    for command in command_stack:
        command.plot_circle()
