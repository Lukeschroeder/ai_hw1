import tkinter as tk
import random

#Square Width: 25, Square Height: 25

n = 17

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=n*25, height=n*25, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cellwidth = 25
        self.cellheight = 25

        self.rect = {}
        self.label = {}

        for x in range(n):
            for y in range(n):
                x1 = x * self.cellwidth
                y1 = y * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight

                if (y + 1) * (x + 1) == n**2:
                    self.rect[y + 1, x + 1] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="green", outline="white", tags="rect")
                    break

                self.rect[y + 1, x + 1] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="dark gray", outline="white", tags="rect")

    def addlabel(self, x, y,label):
        xcoord = (x - 1) * self.cellwidth + self.cellwidth / 2
        ycoord = (y - 1) * self.cellheight + self.cellheight / 2
        self.label[x, y] = self.canvas.create_text((xcoord, ycoord), text=label, font=('fixedsys', 12), fill="black")  

    def generatepuzzle(self):
        i = 0
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if ( x * y == n**2):
                    break
                bound = max(n - x, x - 1, n - y, y - 1)
                self.addlabel(x, y, str(random.randint(1, bound)))

  
if __name__ == "__main__":
    app = App()
    app.generatepuzzle()
    #app.canvas.itemconfig(app.rect[n,n], fill='green')
    #app.canvas.itemconfig(app.label[2,7], text='234')
    app.mainloop()
    
    