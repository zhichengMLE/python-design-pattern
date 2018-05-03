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


class Command():
    def __init__(self):
        self.command_stack = []

    def add_command(self, command):
        self.command_stack.append(command)

    def execute_command(self):
        for command in self.command_stack:
            command()

if __name__ == "__main__":
    command = Command()
    command.add_command(Circle(rad=1).plot_circle)
    command.add_command(Circle(rad=2).plot_circle)
    command.add_command(Circle(rad=3).plot_circle)
    command.add_command(Circle(rad=4).plot_circle)
    command.add_command(Circle(rad=5).plot_circle)
    command.execute_command()
