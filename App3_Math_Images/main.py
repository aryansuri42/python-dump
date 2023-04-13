class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.width = width
        self.height = height

    def make(self):
        pass


class Rectangle:

    def __init__(self, x, width, y, height, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def draw(self):
        pass


class Square:

    def __init__(self, x, color, width, height):
        self.x = x
        self.color = color
        self.width = width
        self.height = height

    def draw(self):
        pass
