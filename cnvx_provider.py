import math

def polygon(n):
    xs = []
    ys = []
    for i in range(n):
        xs.append(math.cos(i * 2 * math.pi / n))
        ys.append(math.sin(i * 2 * math.pi / n))
    return xs, ys  
    


def get_convex():
    """возвращает два массива xs, ys, в которых лежат координаты выпуклого множества"""
    return polygon(14)
    