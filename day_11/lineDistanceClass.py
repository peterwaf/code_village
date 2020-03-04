"""Fill in the Line class methods to accept coordinates as a pair of
 tuples and return the slope and distance of the line."""
 
import math
class Line:
    """class methods to accept coordinates as a pair of
    tuples and return the slope and distance of the line"""
    
    coor1 = ()
    coor2 = ()
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    
    def distance(self):
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1]
        result1 = x2 - x1
        result2 = y2 - y1
        xsquare = result1 ** 2
        ysquare = result2 ** 2
        sumsquare = xsquare + ysquare
        d = math.sqrt(sumsquare)
        print('The distance is',d)
        
    
    def slope(self):
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1]
        carrier1 = y2 - y1
        carrier2 = x2 - x1
        line = carrier1 / carrier2
        print('The slope  is ',line)

Line.coor1 = (3,2) #accessing the Line tuple for the first coordinates
Line.coor2 = (8,10) #accessing the Line tuple for the second coordinates
mycoordinates = Line(Line.coor1,Line.coor2)
mycoordinates.distance()
mycoordinates.slope()