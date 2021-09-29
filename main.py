from tkinter import Tk
from cnvx_provider import get_convex
from gui import GUI



if __name__ == "__main__":
    root = Tk()
    my_gui = GUI(root, get_convex())
    root.mainloop()