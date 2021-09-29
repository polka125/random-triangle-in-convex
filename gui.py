from tkinter import Tk, Label, Button, Canvas
import random

class GUI:
    def __init__(self, master, convex_poly):
        self.master = master
        self.convex_poly_x, self.convex_poly_y = convex_poly 
        self.sides = len(convex_poly[0])
        
        self.triangle = None
        
        master.title("Triangle In Cnvx")

        self.canv = Canvas(master, bg="white", height=300, width=400)
        self.draw_main()
        self.canv.pack()
        
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Sample", command=self.resample)
        self.greet_button.pack()


    
    def draw_main(self):
        to_draw = list(map(self.transform_to_canvas, zip(self.convex_poly_x, self.convex_poly_y)))
        self.canv.create_polygon(*to_draw,
        outline="green", fill=self._from_rgb((153, 204, 255)))


    def resample(self):
        if not (self.triangle is None):
            self.remove()
        self.sample()
    
    def sample(self):
        all_ind = [i for i in range(self.sides)]
        choosed_ind = sorted(random.sample(all_ind, 3))
        triangle_x = [self.convex_poly_x[i] for i in choosed_ind]
        triangle_y = [self.convex_poly_y[i] for i in choosed_ind]
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