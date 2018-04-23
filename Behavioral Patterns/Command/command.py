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


