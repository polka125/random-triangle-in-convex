from geometry import grind_polygon, area
import random


def estimate_expectation(xs, ys, iters=10000):
    polygon_area = area(xs, ys)
    triangle_avg_area = 0.0
    
    
    xs, ys = grind_polygon(xs, ys)
    all_ind = [i for i in range(len(xs))]
    for trial in range(iters):
        choosed_ind = sorted(random.sample(all_ind, 3))
        triangle_x = [xs[i] for i in choosed_ind]
        triangle_y = [ys[i] for i in choosed_ind]
        triangle_avg_area += area(triangle_x, triangle_y)
    
    return (triangle_avg_area / iters) / polygon_area