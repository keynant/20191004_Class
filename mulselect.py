from tkinter import *
import time

class CalculatorWindow:
    def __init__(self, root):
        self.root= root
        root.title("Calculator")

        MODES = [
            ("Monochrome", "1"),
            ("Grayscale", "L"),
            ("True color", "RGB"),
            ("Color separation", "CMYK"),
        ]

        v = StringVar()
        v.set(4)  # initialize
        for value in range(1,11):
            b = Radiobutton(root, text=str(value),
                            variable=v, value=value,
                            indicatoron=0,
                            width=30)
            b.pack()
        bn = Button(root, text="Print", command=lambda:print(v.get()))
        bn.pack()

root = Tk()
my_window = CalculatorWindow(root)

root.mainloop()  # blocking

# targil:
# create option buttons from 1-10 in loop (maybe without modes?)
# print button -> will print the current selection
