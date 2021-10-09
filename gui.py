from geometry import grind_polygon, area
from tkinter import Tk, Label, Button, Canvas
from estimate import estimate_expectation

import random

class GUI:
    #TODO: fix convex_poly arg to common convex_poly_x, convex_poly_y 
    def __init__(self, master, convex_poly):
        self.master = master
        self.convex_poly_x, self.convex_poly_y = grind_polygon(convex_poly[0], convex_poly[1]) 
        self.sides = len(self.convex_poly_x)
        
        self.triangle = None
        
        master.title("Triangle In Cnvx")
        
        self.label = Label(master, text="auth @polka125")
        self.label.pack()

        self.greet_button = Button(master, text="Sample", command=self.resample)
        self.greet_button.pack()

        self.canv = Canvas(master, bg="white", height=300, width=400)
        self.draw_main()
        self.canv.pack()
        
        
        self.poly_area = area(convex_poly[0], convex_poly[1])
        self.avg_area = estimate_expectation(convex_poly[0], convex_poly[1])
        
        self.estimated = \
            Label(master, text=f"Estimated expectation = {self.avg_area}")
        self.estimated.pack()
        
        self.current_ratio = Label(master, text="Current ratio = ?")
        self.current_ratio.pack()


    
    def draw_main(self):
        to_draw = list(map(self.transform_to_canvas, zip(self.convex_poly_x, self.convex_poly_y)))
        self.canv.create_polygon(*to_draw,
        outline="green", fill=self._from_rgb((153, 204, 255)))


    def resample(self):
        if not (self.triangle is None):
            self.remove()
        self.sample()
        
        print("Curr triangle:")
        print(self.triangle_x, self.triangle_y)
        print(f"area =  {area(self.triangle_x, self.triangle_y)}")
        print(f"Polygon area: {self.poly_area}")
        ratio = area(self.triangle_x, self.triangle_y) / self.poly_area
        
        print(f"Ratio = {ratio}")
        
        if ratio > 1:
            raise Exception("ration grater then one!")
        
        self.current_ratio['text'] = f"Current ratio = {ratio}"
    
    #TODO: extract sampler
    def sample(self):
        all_ind = [i for i in range(self.sides)]
        choosed_ind = sorted(random.sample(all_ind, 3))
        triangle_x = [self.convex_poly_x[i] for i in choosed_ind]
        triangle_y = [self.convex_poly_y[i] for i in choosed_ind]
        self.triangle_x = triangle_x.copy()
        self.triangle_y = triangle_y.copy()
        self.draw_triangle(triangle_x, triangle_y)

    def draw_triangle(self, xs, ys):
        to_draw = list(map(self.transform_to_canvas, zip(xs, ys)))
        print(to_draw)
        self.triangle = self.canv.create_polygon(*to_draw,
        outline="black", fill=self._from_rgb((255, 0, 0)))
        
    def remove(self):
        self.canv.delete(self.triangle)
    
    def transform_to_canvas(self, xy):
        x, y = xy
        x *= 100
        y *= 100
        x += 200
        y += 150

        return (x, y)
        
    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb  