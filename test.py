import tkinter as tk
import random

#Square Width: 25, Square Height: 25

n = 15


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=n*25, height=n*25, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 25
        self.cellheight = 25

        self.rect = {}
        for column in range(n):
            for row in range(n):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")
                self.canvas.create_text(((x1 + x2) / 2, (y1 + y2) /2), text="a2")

if __name__ == "__main__":
    app = App()
    app.mainloop()