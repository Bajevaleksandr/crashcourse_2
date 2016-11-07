from graphics import *
def rectangle ():
    win = GraphWin()
    pt = Point(100, 50)
    pt.draw(win)
    rect = Rectangle(Point(140, 40), pt)
    rect.draw(win)
rectangle()
input ("Press enter to continue")