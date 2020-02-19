import tkinter as tk
import random
from puzzle import Puzzle
import time

#Square Width: 25, Square Height: 25

class Gui(tk.Tk):
    def __init__(self, puz):
        tk.Tk.__init__(self)
        self.puz = puz
        self.movenums = puz.movenums
        self.distances = puz.distances
        self.n = puz.n
        self.canvas = tk.Canvas(self, width=self.n*25, height=self.n*25, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cellwidth = 25
        self.cellheight = 25

        self.rectobj = {}
        self.labels = {}

        n = self.n
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                x1 = (x - 1) * self.cellwidth
                y1 = (y - 1) * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight

                xcoord = (x - 1) * self.cellwidth + self.cellwidth / 2
                ycoord = (y - 1) * self.cellheight + self.cellheight / 2
                if x * y == n**2:
                    self.rectobj[(x, y)] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="green", outline="white", tags="rect")
                    self.labels[(x, y)] = self.canvas.create_text((xcoord, ycoord), text=' ', font=('fixedsys', 12), fill="black")
                    break

                self.rectobj[(x, y)] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="dark gray", outline="white", tags="rect")
                self.labels[(x, y)] = self.canvas.create_text((xcoord, ycoord), text='a', font=('fixedsys', 12), fill="black")

    def showmovenums(self):
        n = self.n
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if (x * y == n ** 2):
                    break
                label = str(self.movenums[(x, y)])
                self.canvas.itemconfig(self.labels[(x,y)], text=label)

    def showdistances(self):
        n = self.n
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                label = str(self.distances[(x, y)])
                self.canvas.itemconfig(self.labels[(x,y)], text=label)
         

                
  
if __name__ == "__main__":
    puz = Puzzle(7)
    gui = Gui(puz)
    gui.showmovenums()
    gui.mainloop()


    #app.canvas.itemconfig(app.rect[n,n], fill='green')
    #app.canvas.itemconfig(app.label[2,7], text='234')
    