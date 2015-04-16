#!/usr/bin/env python
import Tkinter as tk

from Tkinter import Tk, Frame, Canvas, BOTH
import building

class SkylineFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Skyline")

        canvas = Canvas(self)
        self.buildcity(canvas,150)

        canvas.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)

    def buildcity(self, canvas, y0):
        width_to_go = 800
        while width_to_go >= -10:
            rect = building.makebuilding(800-width_to_go)
            canvas.create_rectangle(800-width_to_go,y0-rect[1],800-width_to_go-rect[0],y0)
            width_to_go -= (rect[0]+2)
        return

def main():

    root = Tk()
    root.geometry("800x150")
    SkylineFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()