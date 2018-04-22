class Circle():
    def get_shape(self):
        return ("Here is the circle")

class Square():
    def get_shape(self):
        return ("Here is the square")

class Rectangle():
    def get_shape(self):
        return ("Here is the rectangle")

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

if __name__ == "__main__":
    print(shape_factory("Circle"))
    print(shape_factory("Square"))
    print(shape_factory("Rectangle"))

    print(shape_factory("I want other shapes!"))
