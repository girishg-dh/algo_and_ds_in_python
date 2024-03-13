class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return self.x ** 2 + self.y ** 2
    def __str__(self):
        return f"Point: ({self.x}, {self.y}, Distance: {self.distance_from_origin()})"
    
    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __le__(self, other):
        return self.distance_from_origin() <= other.distance_from_origin()

    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()

    def __ne__(self, other):
        return self.distance_from_origin() != other.distance_from_origin()

    def __gt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def __ge__(self, other):
        return self.distance_from_origin() >= other.distance_from_origin()