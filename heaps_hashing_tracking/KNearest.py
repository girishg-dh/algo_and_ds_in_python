'''
Given a list of points on a plane, where the plane is a 2-D array with (x, y) coordinates, find the k
 closest points to the origin (0,0)
'''
import heapq
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

def k_closest(points, k):
    top_k = []
    result = []
    for p in points:
        heapq.heappush(top_k, (p.distance_from_origin(), p))
    for i in range(k):
        _, p = heapq.heappop(top_k)
        result.append(p)
    return result

point_list = [[2,2],[2,2],[2,2]]
point_list = [Point(i[0], i[1]) for i in point_list]
for i in k_closest(point_list, 3):
    print(i)