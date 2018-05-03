import math
import matplotlib.pyplot as plt

class Circle(object):
    def get_shape(self, r=1., n=100):
        return 'circle shape', [(math.cos(2 * math.pi / n * x) * r, math.sin(2 * math.pi/ n * x) * r) for x in range(0, n+1)]

class Square(object):
    def get_shape(self, width=10):
        return 'square shape', [(0,0), (width, 0), (width, width), (0, width), (0, 0)]

class Rectangle(object):
    def get_shape(self, width=10, height=20):
        return 'rectangle shape', [(0,0), (height, 0), (height, width), (0, width), (0, 0)]

class Red(object):
    def get_color(self):
        return "red color", 'r'

class Green(object):
    def get_color(self):
        return "green color", 'g'

class Blue(object):
    def get_color(self):
        return "blue color", 'b'

class Shape_Factory(object):
    def __init__(self, shape_obj):
        self.shape_obj = shape_obj

    def get_shape(self):
        shape = self.shape_obj()
        return shape.get_shape()[1]

class Color_Factory(object):
    def __init__(self, color_obj):
        self.color_obj = color_obj

    def get_color(self):
        color = self.color_obj()
        return color.get_color()[1]

class Shape_With_Color_Factory(object):
    def __init__(self, shape_factory, color_factory):
        self.shape_factory = shape_factory
        self.color_factory = color_factory

    def get_shape_with_color(self):
        shape_ret = self.shape_factory.get_shape()
        color_ret = self.color_factory.get_color()

        return (shape_ret, color_ret)

    @staticmethod
    def plot_shape_with_color(shape, color):
        plt.figure(figsize=(5, 5))
        plt.fill([s[0] for s in shape], [s[1] for s in shape], color=color)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

if __name__ == "__main__":
    shape, color = Shape_With_Color_Factory(Shape_Factory(Circle), Color_Factory(Blue)).get_shape_with_color()
    Shape_With_Color_Factory.plot_shape_with_color(shape, color)

    shape, color = Shape_With_Color_Factory(Shape_Factory(Square), Color_Factory(Green)).get_shape_with_color()
    Shape_With_Color_Factory.plot_shape_with_color(shape, color)

    shape, color = Shape_With_Color_Factory(Shape_Factory(Rectangle), Color_Factory(Red)).get_shape_with_color()
    Shape_With_Color_Factory.plot_shape_with_color(shape, color)
