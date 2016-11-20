from graphics import *

def circle ():
    print ("Dai mne radius, detka!")
    field_draw=int(input())
    win = GraphWin()
    pt = Point(100, 50)
    pt.draw(win)
    cir = Circle(pt, field_draw)

    print ("Nazovi chislo, suchechka!")
    number26=int(input())
    print("xAxA")
    print("Nazovi esche odno chislo, suchechka!")
    number27 = int(input())
    cir.setOutline('black')
    color=color_rgb(number26, 0, number27)
    cir.setFill(color)
    cir.draw(win)
    # for i in range(46):
    #     circle().move(5, 0)
    #     time.sleep(.05)
circle()

input ("Press enter to continue")
print (" Game Over")