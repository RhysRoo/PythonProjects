from graphics import *
from patchestest import *
from wrapper import *

#functions
def rect(win, tl, br, colours):

    r = Rectangle(Point(tl.x, tl.y), Point(br.x, br.y))
    r.setFill(colours)
    r.draw(win)
    return r

def main():
    screenSize = 100
    win = GraphWin("", screenSize, screenSize)
    colours = ["red", "white", "blue"]

    for y in range(0, screenSize, 20):
        for x in range(0, screenSize, 25):

                tl = Point(x, y)
                br = Point(tl.x + 25, tl.y + 10)
                rectangle(win, tl, br, colours[0])

    for y in range(10, screenSize, 20):
        for x in range(20, screenSize, 40):

                tl = Point(x, y)
                br = Point(tl.x + 20, tl.y + 10)
                rectangle(win, tl, br, colours[1])

    for y in range(10, screenSize, 20):
        for x in range(0, screenSize, 40):

                tl = Point(x, y)
                br = Point(tl.x + 20, tl.y + 10)
                rectangle(win, tl, br, colours[0])


    win.getMouse()
main()