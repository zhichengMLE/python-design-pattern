# In object-oriented programming, the command pattern is a behavioral design pattern
# in which an object is used to encapsulate all information needed to perform
# an action or trigger an event at a later time. This information includes
# the method name, the object that owns the method and values for the method parameters..
# See more in wiki: https://en.wikipedia.org/wiki/Command_pattern
#
# We are going to implement command pattern which save command set
# of plotting different shape.

class Circle():
    def __init__(self, rad=1):
        self.rad = rad

    def plot_circle(self):
        print("Plot a circle with rad = %s" %(self.rad))
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
