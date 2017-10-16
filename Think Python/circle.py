import math
import copy

class Point:
    """Represents a point in 2D space

    Attributes: x, y"""

class Circle:
    """Represents a circle in 2D space

    Attributes: centre, radius

    centre is a point"""

class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def print_circle(c):
    print_point(c.centre)
    print('%g' % c.radius)

c = Circle()
c.radius = 1
c.centre = Point()
c.centre.x = 0
c.centre.y = 0

origin = Point()
origin.x = 0
origin.y = 0

p = c.centre

box = Rectangle()
box.width =  1.8
box.height = 1.8
box.corner = Point()
box.corner.x = -0.9
box.corner.y = -0.9

    
print_circle(c)

def distance(p,q):
    """returns the distances between two points in 2D space"""
    dx = p.x - q.x
    dy = p.y - q.y
    return math.sqrt(dx**2 + dy**2)

def point_in_circle(circle,point):
    if distance(circle.centre,point) <= circle.radius:
        return True
    else:
        return False

def rect_in_circle(circle,rect):
    corners = []
    for i in range(2):
        for j in range(2):
            point = Point()
            point.x = rect.corner.x + rect.width*i
            point.y = rect.corner.y + rect.height*j
            corners.append(copy.deepcopy(point))
    return all(point_in_circle(circle,corner) for corner in corners)

def circle_in_rect(circle,rect):
    return (circle.centre.x - circle.radius >= rect.corner.x
            and circle.centre.x + circle.radius <= rect.corner.x + rect.width
            and circle.centre.y - circle.radius >= rect.corner.y
            and circle.centre.y - circle.radius <= rect.corner.y + rect.height)
    

print(point_in_circle(c,p))

print(rect_in_circle(c,box))

def rect_circle_overlap(circle,rect):
    if rect_in_circle(circle,rect) or circle_in_rect(circle,rect):
        return True
    else:
        for i in range(2):
            point = Point()
            point.x = rect.corner.x + rect.width*i
            for j in range(1001):
                point.y = rect.corner.y + rect.height*(j/1000)
                if point_in_circle(circle,point):
                    return True
        for i in range(2):
            point = Point()
            point.y = rect.corner.y + rect.height*i
            for j in range(1001):
                point.x = rect.corner.y + rect.width*(j/1000)
                if point_in_circle(circle,point):
                    return True
        return False

print(rect_circle_overlap(c,box))
        
    
