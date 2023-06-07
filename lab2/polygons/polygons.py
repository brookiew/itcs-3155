import math


class Polygons:

    def __init__(self, num_sides, side_length):
        """
        A class that represents a regular polygon.

        attributes:
            - num_sides: the number of sides of the polygon
            - side_length: the length of each side of the polygon
            - radius: the radius of the circumscribed circle of the polygon
            - area: the area of the polygon
        """

        self.num_sides = num_sides

        self.side_length = side_length
        
        self.radius = side_length / (2 * math.sin(math.pi / num_sides))
       
        self.area = self.polygon_area()
        

    def polygon_area(self):
        """
        Method that calculates the area of the polygon from the number of sides and side length.
        returns:
            - the area of the polygon
        """
        return self.num_sides * self.side_length ** 2 / (4 * math.tan(math.pi / self.num_sides))
