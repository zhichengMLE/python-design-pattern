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
        return True

'''
    Exercise to the student
    - Implement the Command design pattern in following classes(i.e., Command()).
    1. add_command(self, command)
        1) You need to append the command into command_stack

    2. execute_command(self)
        1) Execute the command iteratively.
        2) Return the execute status.

    Note: remember to remove pass statement in the function after implement the code.
'''
class Command():
    def __init__(self):
        self.command_stack = []
        self.command_execute_status = False

    def add_command(self, command):
        pass
        # self.command_stack.append(command)

    def execute_command(self):
        pass
        # self.command_execute_status = True
        # for command in self.command_stack:
        #     execute_status = command()
        #     if(execute_status == False):
        #         self.command_execute_status = False
        # return self.command_execute_status
