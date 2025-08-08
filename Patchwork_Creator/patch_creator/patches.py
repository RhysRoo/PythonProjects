from wrapper import *


def patchB(win, colour, tlPoint):
    dimension = 100
    centre = centrePoint(tlPoint, 50)
    scale = 30
    r = rectangle(win,tlPoint,brPoint(tlPoint,dimension,dimension),colour)
    t = Text(centre,"")
    t.setSize(scale)
    t.setTextColor("white")
    t.draw(win)



def patchF(win, colour, tlPoint):
    dimension = 100
    centre = centrePoint(tlPoint, 50)
    scale = 30
    r = rectangle(win, tlPoint, brPoint(tlPoint, dimension, dimension), colour)
    t = Text(centre,"F")
    t.setSize(scale)
    t.setTextColor("black")
    t.draw(win)


def patchP(win, colour, tlPoint):
    dimension = 100
    centre = centrePoint(tlPoint, 50)
    scale = 30
    r = rectangle(win,tlPoint,brPoint(tlPoint,dimension,dimension),colour)
    t = Text(centre,"P")
    t.setSize(scale)
    t.setTextColor("white")
    t.draw(win)

def mypatch1(win, colour):

    screenSize = 100
    # win = GraphWin("", screenSize, screenSize)
    # colour = ["red", "white"]

    for y in range(0, screenSize, 20):
        for x in range(0, screenSize, 25):

                tl = Point(x, y)
                br = Point(tl.x + 25, tl.y + 10)
                rectangle(win, tl, br, colour[0])

    for y in range(10, screenSize, 20):
        for x in range(20, screenSize, 40):

                tl = Point(x, y)
                br = Point(tl.x + 20, tl.y + 10)
                rectangle(win, tl, br, colour[1])

    for y in range(10, screenSize, 20):
        for x in range(0, screenSize, 40):

                tl = Point(x, y)
                br = Point(tl.x + 20, tl.y + 10)
                rectangle(win, tl, br, colour[0])

    win.getMouse()
# mypatch1()