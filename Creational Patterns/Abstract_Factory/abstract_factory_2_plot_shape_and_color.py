import math
import matplotlib.pyplot as plt

class Circle():
    def get_shape(self, r=1., n=100):
        return [(math.cos(2 * math.pi / n * x) * r, math.sin(2 * math.pi/ n * x) * r) for x in range(0, n+1)]

class Square():
    def get_shape(self, width=10):
        return [(0,0), (width, 0), (width, width), (0, width), (0, 0)]

class Rectangle():
    def get_shape(self, width=10, height=20):
        return [(0,0), (height, 0), (height, width), (0, width), (0, 0)]

class Red():
    def get_color(self):
        return ("r")

class Green():
    def get_color(self):
        return ("g")

class Blue():
    def get_color(self):
        return ("b")

class Shape_Factory():
    def __init__(self, shape):
        self.shape = shape

    def get_shape(self):
        if(self.shape is not "Circle" and self.shape is not "Square" and self.shape is not "Rectangle"):
            return -1

        circle = Circle()
        square = Square()
        rectangle = Rectangle()

        shapes = {
            "Circle": circle,
            "Square": square,
            "Rectangle": rectangle,
        }

        return shapes[self.shape].get_shape()

class Color_Factory():
    def __init__(self, color):
        self.color = color

    def get_color(self):
        if (self.color is not "Red" and self.color is not "Green" and self.color is not "Blue"):
            return -1

        red = Red()
        green = Green()
        blue = Blue()

        colors = {
            "Red": red,
            "Green": green,
            "Blue": blue,
        }

        return colors[self.color].get_color()

def shape_with_color_factory(shape="Circle", color="Red"):
    shape_factory = Shape_Factory(shape)
    color_factory = Color_Factory(color)

    shape_ret = shape_factory.get_shape()
    color_ret = color_factory.get_color()

    if(shape_ret == -1 or color_ret == -1):
        print("Unsupport shape or color")

    return (shape_ret, color_ret)

def plot_shape_with_color(shape, color):
    if(shape == -1 or color == -1):
        return -1

    plt.figure(figsize=(5, 5))
    plt.fill([s[0] for s in shape], [s[1] for s in shape], color=color)
    plt.show()

if __name__ == "__main__":
    shape, color = shape_with_color_factory("Circle", "Blue")
    plot_shape_with_color(shape, color)

    shape, color = shape_with_color_factory("Square", "Green")
    plot_shape_with_color(shape, color)

    shape, color = shape_with_color_factory("Rectangle", "Red")
    plot_shape_with_color(shape, color)

    shape, color = shape_with_color_factory("I want other shapes!", "I want other colors!")
    plot_shape_with_color(shape, color)
