"""Functions for classifying triangles."""
def is_valid(sides):
    if all(side>0 for side in sides) and all(sum(sides[j] for j in range(3) if j!=i)>sides[i]
        for i in range(3)):
        return True
    return False

def equilateral(sides):
    if not is_valid(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_valid(sides):
        return False
    return sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]


def scalene(sides):
    if not is_valid(sides):
        return False
    return not sides[0]==sides[1] and not sides[1]==sides[2] and not sides[0]==sides[2]
