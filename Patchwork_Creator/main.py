from graphics import *

# Function lib

def brPoint(tlPoint, width, height):
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint


def centrePoint(tlPoint, radius):
    x = tlPoint.getX() + radius
    y = tlPoint.getY() + radius
    centre = Point(x, y)
    return centre

def patchB(win, colour, tlPoint):
    dimension = 100
    centre = centrePoint(tlPoint, 50)
    scale = 30
    r = myRectangle(win, tlPoint, brPoint(tlPoint, dimension, dimension), colour)
    t = Text(centre, "")
    t.setSize(scale)
    t.setTextColor("white")
    t.draw(win)
    return r

def myCircle(win, centre, radius, colours, strokeColour):
    c = Circle(centre, radius)
    c.setFill(colours)
    c.setOutline(strokeColour)
    c.draw(win)
    return c


def myRectangle(win, tlPoint, brPoint, colours):
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colours)
    r.draw(win)
    return r

def question():
    question = input("do you want to choose patch colours: ")

    if question == "yes":
        colours = []
        colours.append(input("Please enter your colours from list below?\nred, green, blue, purple, yellow, orange, cyan\n1st colour: ")) 
        colours.append(input("2nd colour: "))
        colours.append(input("3rd colour: "))
    else:
        colours = ["blue", "orange", "red"]
    
    return colours

def main():
    colours = question()

# Patches

def patch1(win, tlxPoint, tlyPoint, patchColour):
    patchSize = 100

    # tly is the y value from main + tlx is the x value from main

    for y in range(tlyPoint, tlyPoint + patchSize, 20):
        for x in range(tlxPoint, tlxPoint + patchSize, 25):
            tlPoint = Point(x, y)
            brPoint = Point(tlPoint.x + 25, tlPoint.y + 10)
            myRectangle(win, tlPoint, brPoint, patchColour)

    # tly + location in pattern patch

    for y in range(tlyPoint + 10, tlyPoint + patchSize, 20):
        for x in range(tlxPoint + 20, tlxPoint + patchSize, 40):
            tlPoint = Point(x, y)
            brPoint = Point(tlPoint.x + 20, tlPoint.y + 10)
            myRectangle(win, tlPoint, brPoint, "white")

    for y in range(tlyPoint + 10, tlyPoint + patchSize, 20):
        for x in range(tlxPoint, tlxPoint + patchSize, 40):
            tlPoint = Point(x, y)
            brPoint = Point(tlPoint.x + 20, tlPoint.y + 10)
            myRectangle(win, tlPoint, brPoint, patchColour)


def patch2(win, tlxPoint, tlyPoint, patchColour):
    patchSize = 100

    for y in range(tlyPoint + 10, tlyPoint + patchSize, 40):
        for x in range(tlxPoint + 10, tlxPoint + patchSize, 20):
            centre = Point(x, y)

            if x <= tlxPoint + patchSize and y <= tlyPoint + patchSize:
                myCircle(win, centre, 10, patchColour, patchColour)

    for y in range(tlyPoint + 30, tlyPoint + patchSize, 40):
        for x in range(tlxPoint + 10, tlxPoint + patchSize, 20):
            centre = Point(x, y)

            if x <= tlxPoint + 100 and y <= tlyPoint + patchSize:
                myCircle(win, centre, 10, "white", patchColour)

# Main

def main():
    screenSize = int(input("What is patchwork size? 5 or 7: ")) * 100
    colours = question()
    win = GraphWin("Patch Coursework", screenSize, screenSize)

    if screenSize == 500:

        for y in range(0, 401, 100):
            patchB(win, colours[0], Point(0, y))

        for y in range(0, 401, 100):

            if y == 0:
                patch1(win, 100, y, colours[1])

            elif 100 <= y <= 300:
                patch2(win, 100, y, colours[2])

            else:
                patchB(win, colours[2], Point(100, y))

        for y in range(0, 401, 100):

            if y == 0:
                patch1(win, 200, y, colours[1])

            elif 100 <= y <= 100:
                patchB(win, colours[1], Point(200, y))

            elif 200 <= y <= 300:
                patch2(win, 200, y, colours[0])

            else:
                patchB(win, colours[0], Point(200, y))

        for y in range(0, 401, 100):

            if y == 0:
                patch1(win, 300, y, colours[1])

            elif 100 <= y <= 200:
                patchB(win, colours[1], Point(300, y))

            elif y == 300:
                patch2(win, 300, y, colours[2])

            else:
                patchB(win, colours[2], Point(300, y))

        for y in range(0, 401, 100):

            if 0 <= y <= 300:
                patch1(win, 400, y, colours[1])

            else:
                patchB(win, colours[0], Point(400, y))

    # screenSize 700

    elif screenSize == 700:

        for y in range(0, 701, 100):
            patchB(win, colours[0], Point(0, y))

        for y in range(0, 701, 100):

            if y == 0:
                patch1(win, 100, y, colours[1])

            elif 100 <= y <= 500:
                patch2(win, 100, y, colours[2])

            else:
                patchB(win, colours[2], Point(100, y))

        for y in range(0, 701, 100):

            if y == 0:
                patch1(win, 200, y, colours[1])

            elif y == 100:
                patchB(win, colours[1], Point(200, y))

            elif 200 <= y <= 500:
                patch2(win, 200, y, colours[0])

            else:
                patchB(win, colours[0], Point(200, y))

        for y in range(0, 701, 100):

            if y == 0:
                patch1(win, 300, y, colours[1])

            elif 100 <= y <= 200:
                patchB(win, colours[1], Point(300, y))

            elif 300 <= y <= 500:
                patch2(win, 300, y, colours[2])

            else:
                patchB(win, colours[2], Point(300, y))

        for y in range(0, 701, 100):

            if y == 0:
                patch1(win, 400, y, colours[1])

            elif 100 <= y <= 300:
                patchB(win, colours[1], Point(400, y))

            elif 400 <= y <= 500:
                patch2(win, 400, y, colours[0])

            else:
                patchB(win, colours[0], Point(400, y))

        for y in range(0, 701, 100):

            if y == 0:
                patch1(win, 500, y, colours[1])

            elif 100 <= y <= 400:
                patchB(win, colours[1], Point(500, y))

            elif y == 500:
                patch2(win, 500, y, colours[2])

            else:
                patchB(win, colours[2], Point(500, y))

        for y in range(0, 701, 100):

            if 0 <= y <= 500:
                patch1(win, 600, y, colours[1])

            else:
                patchB(win, colours[0], Point(600, y))

    else:
        print("Invalid screensize")

    win.getMouse()

main()