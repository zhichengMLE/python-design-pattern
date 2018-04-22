class Circle(object):
    def get_shape(self):
        return ("circle shape")

class Square(object):
    def get_shape(self):
        return ("square shape")

class Rectangle(object):
    def get_shape(self):
        return ("rectangle shape")

class Red(object):
    def get_color(self):
        return ("red color")

class Green(object):
    def get_color(self):
        return ("green color")

class Blue(object):
    def get_color(self):
        return ("blue color")

class Shape_Factory(object):
    def __init__(self, shape_obj):
        self.shape_obj = shape_obj

    def get_shape(self):
        shape = self.shape_obj()
        return shape.get_shape()

class Color_Factory(object):
    def __init__(self, color_obj):
        self.color_obj = color_obj

    def get_color(self):
        color = self.color_obj()
        return color.get_color()

class Shape_With_Color_Factory(object):
    def __init__(self, shape_factory, color_factory):
        self.shape_factory = shape_factory
        self.color_factory = color_factory

    def get_shape_with_color(self):
        shape_ret = self.shape_factory.get_shape()
        color_ret = self.color_factory.get_color()

        return ("Here is %s in %s \n" %(shape_ret, color_ret))

if __name__ == "__main__":
    print(Shape_With_Color_Factory(Shape_Factory(Circle), Color_Factory(Blue)).get_shape_with_color())
    print(Shape_With_Color_Factory(Shape_Factory(Square), Color_Factory(Green)).get_shape_with_color())
    print(Shape_With_Color_Factory(Shape_Factory(Rectangle), Color_Factory(Red)).get_shape_with_color())
