from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fall_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            print(True)
        else:
            print(False)


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class DrawRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        turtle.done()


frrectangle = DrawRectangle(Point(randint(0, 200), randint(201, 401)), Point(randint(0, 200), randint(201, 401)))

print("Point1(", frrectangle.point1.x, ",", frrectangle.point1.y, ") and \
Point2(", frrectangle.point2.x, ",", frrectangle.point2.y, ")")

x1 = int(input("X Coordinate: "))
y1 = int(input("Y Coordinate: "))
area1 = int(input("Guess the Area: "))
pointx = GuiPoint(x1, y1)
pointx.fall_in_rectangle(frrectangle)
print("Your area was off by ", frrectangle.area() - area1)
myturtle = turtle.Turtle()
frrectangle.draw(canvas=myturtle)
pointx.draw(canvas=myturtle)
