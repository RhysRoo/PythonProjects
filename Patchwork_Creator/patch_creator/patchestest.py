from graphicalObjects import *

def patch1():

    for y in range(0, 100, 20):
        for x in range(0, 100, 25):
            
            if x <= 100 and y <= 100:
                tl = Point(x, y)
                br = Point(tl.x + 25, tl.y + 10)
                rectangle(win, tl, br, colours[0])

    for y in range(10, 100, 20):
        for x in range(0, 100, 20):

            if x >= 20 and x <= 30 and y <= 100:
                tl = Point(x, y)
                br = Point(tl.x + 20, tl.y + 10)
                myRect(win, tl, br, colours[1])

            elif x >= 60 and x <= 70 and y <= 100:
                tl = Point(x, y)
                br = Point(tl.x + 20, tl.y + 10)
                myRect(win, tl, br, colours[1])

    for y in range(10, 100, 20):
        for x in range(0, 100, 40):

            if x >= 0 and x <= 100:
                tl = Point(x, y)
                br = Point(tl.x + 20, tl.y + 10)
                myRect(win, tl, br, colours[0])


# def patch2(win, colours, tlOffset):
#     screenSize = 110
#     scale = 25
#     alternateFlag = False
    
#     for y in range(0, screenSize, scale):
#         for x in range(0, screenSize, scale):
#             tl = Point(tlOffset.getX() + y, tlOffset.getY() + x)
#             br = brPoint(tl, scale, scale)
#             if alternateFlag:
#                 circlefromTL(win, tl, 12, colours[1])
#             else:
#                 circlefromTL(win, tl, 12, colours[0])
            
#             alternateFlag = not alternateFlag