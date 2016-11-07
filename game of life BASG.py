from graphics import *
print ("Hi, i`m Game of Life")

def get_field_sizes():
    print("What is the length?")
    field_length = input()
    return field_length
    print("What is the width?")
    field_width = input()
    return field_width
    print("Okay, I got you, your field should be " + field_length + "x" + field_width)

def rectangle ():
    get_field_sizes()
    win = GraphWin()
    pt = Point(100, 50)
    pt.draw(win)
    rect = Rectangle(Point(, field_width), pt)
    rect.draw(win)

rectangle()

print (" Game Over")