import tkinter as tk
import random

#Square Width: 25, Square Height: 25

n = 5
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=n*25, height=n*25, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cellwidth = 25
        self.cellheight = 25

        self.rect = {}
        self.labels = {}
        self.movenums = {}
        self.distances = {}

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
        
        self.labels[x, y] = self.canvas.create_text((xcoord, ycoord), text=label, font=('fixedsys', 12), fill="black") 
         


    # Initializes labels containing tkinter objects, 
    # and movenums containing integer move numbers
    def generatepuzzle(self):
        i = 0
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                bound = max(y - 1, n - x, x - 1, n - y)
                value = random.randint(1, bound)

                if (x * y == n ** 2):
                    self.movenums[x, y] = 0
                    break

                self.addlabel(x, y, value)
                self.movenums[x, y] = value

                


    def calculatemindistances(self):
        # Initializes shortest path distances: 0 for [1][1] and -1 otherwise
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if ( x * y == 1):
                    self.distances[(x, y)] = 0 
                else:
                    self.distances[(x, y)] = -1
        # Add first vertex to queue
        queue = []
        queue.append((1,1))
        # While queue non-empty
        while queue:
            # Pop head of queue as parent
            current = queue.pop(0)
            px = current[0]
            py = current[1]
            # Get move num of parent
            movenum = self.movenums[(px, py)]
            # If movenum = 0: found goal node, no neighbors to access
            if movenum == 0: continue

            # Get neighbors
            ns = [(px, py - movenum), (px, py + movenum), (px + movenum, py), (px - movenum, py)]

            # For each neighbor
            for (x,y) in ns:
                # If neighbor unvisited and in range, update distance add it to queue
                if (x >= 1 and x <= n and  y >= 1 and y <= n and self.distances[(x, y)] < 0):
                    self.distances[(x, y)] = self.distances[(px,py)] + 1
                    queue.append((x, y))


    def printdistances(self):
        for y in range(1, n + 1):
            print('\n')
            for x in range(1, n + 1):
                print(self.distances[(x,y)], end = ' ')

                
  
if __name__ == "__main__":
    app = App()
    app.generatepuzzle()
    app.calculatemindistances()
    #app.printdistances()

    #app.canvas.itemconfig(app.rect[n,n], fill='green')
    #app.canvas.itemconfig(app.label[2,7], text='234')
    app.mainloop()
    
    