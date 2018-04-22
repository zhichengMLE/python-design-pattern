class Circle():
    def get_shape(self):
        return ("Here is the circle shape")

class Square():
    def get_shape(self):
        return ("Here is the square shape")

class Rectangle():
    def get_shape(self):
        return ("Here is the rectangle shape")

class Red():
    def get_red(self):
        return ("Here is the red color")

class Green():
    def get_green(self):
        return ("Here is the green color")

class Blue():
    def get_blue(self):
        return ("Here is the blue color")

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

        red = Circle()
        green = Square()
        blue = Rectangle()

        shapes = {
            "Red": red,
            "Green": green,
            "Blue": blue,
        }

        return shapes[self.color].get_shape()

def shape_with_color_factory(shape="Circle", color="Red"):
    shape_factory = Shape_Factory(shape)
    color_factory = Color_Factory(color)

    shape_ret = shape_factory.get_shape()
    color_ret = color_factory.get_color()

    if(shape_ret is -1 or color_ret is -1):
        return ("Unsupport shape or color.")
    else:
        return ("Here is %s in %s" %(shape, color))

if __name__ == "__main__":
    print(shape_with_color_factory("Circle", "Blue"))
    print(shape_with_color_factory("Square", "Green"))
    print(shape_with_color_factory("Rectangle", "Red"))

    print(shape_with_color_factory("I want other shapes!", "I want other colors!"))
