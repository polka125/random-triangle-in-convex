from tkinter import Tk
from cnvx_provider import *
from gui import GUI



if __name__ == "__main__":
    root = Tk()
    my_gui = GUI(root, polygon(3))
    root.mainloop()