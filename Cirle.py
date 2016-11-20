from graphics import *

def circle ():
    print ("Dai mne radius, detka!")
    field_draw=int(input())
    win = GraphWin()
    pt = Point(100, 50)
    pt.draw(win)
    cir = Circle(pt, field_draw)
    cir.draw(win)
circle()

input ("Press enter to continue")
print (" Game Over")