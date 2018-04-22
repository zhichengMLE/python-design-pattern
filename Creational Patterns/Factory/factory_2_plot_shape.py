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

def shape_factory(shape="Circle"):
    if(shape is not "Circle" and shape is not "Square" and shape is not "Rectangle"):
        return ('The ShapeFactory only support "Circle", "Square" and "Rectangle"')

    # Since factory will initialize all the classes that belong to it,
    # its space complexity is large is there are more classes.
    circle = Circle()
    square = Square()
    rectangle = Rectangle()

    shapes = {
        "Circle": circle,
        "Square": square,
        "Rectangle": rectangle,
    }

    return shapes[shape].get_shape()

def plot_shape(shape):
    plt.figure(figsize=(5, 5))
    plt.plot([s[0] for s in shape], [s[1] for s in shape])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    shape = shape_factory("Circle")
    plot_shape(shape)

    shape = shape_factory("Square")
    plot_shape(shape)

    shape = shape_factory("Rectangle")
    plot_shape(shape)

    shape_factory("I want other shapes!")
