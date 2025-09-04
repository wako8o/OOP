class ImageArea:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __lt__(self, other):
        if isinstance(other, ImageArea):
            # I'm checking if it's a different class, if it is, we'll return it. NotImplemented
            return self.get_area() < other.get_area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, ImageArea):
            return self.get_area() <= other.get_area()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, ImageArea):
            return self.get_area() == other.get_area()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ImageArea):
            return self.get_area() != other.get_area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, ImageArea):
            return self.get_area() > other.get_area()
        return NotImplemented

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)
