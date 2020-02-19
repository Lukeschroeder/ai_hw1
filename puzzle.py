import tkinter as tk
import random

#Square Width: 25, Square Height: 25


class Puzzle:
    def __init__(self, n):

        # Stored Data
        self.n = n
        self.movenums = {}
        self.distances = {}
        self.evaluation = 0

        # Populate Stored Data
        self.generatepuzzle()
        self.calculatemindistances()
        self.evaluate()
         
    # Initializes labels containing tkinter objects, 
    # and movenums containing integer move numbers
    def generatepuzzle(self):
        n = self.n
        i = 0
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                bound = max(y - 1, n - x, x - 1, n - y)
                value = random.randint(1, bound)

                if (x * y == n ** 2):
                    self.movenums[x, y] = 0
                    break

                self.movenums[x, y] = value

    def calculatemindistances(self):
        n = self.n

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

    def printmovenums(self):
        print("\nMove Nums: ")
        n = self.n
        for y in range(1, n + 1):
            for x in range(1, n + 1):
                print(self.movenums[(x,y)], end = ' ')
            print()

    def printdistances(self):
        print("\nShortest Distances: ")
        n = self.n
        for y in range(1, n + 1):
            for x in range(1, n + 1):
                print(self.distances[(x,y)], end = ' ')
            print()

    def evaluate(self):
        n = self.n
        if self.distances[(n,n)] < 0:
            k = 0
            for x in range(1, n+1):
                for y in range(1, n+1):
                    if(self.distances[(x,y)]) < 0:
                        k -= 1
            self.evaluation = k

        else:
            self.evaluation = self.distances[(n,n)]
            

        
                
  
if __name__ == "__main__":
    puz = Puzzle(7)
    puz.printmovenums()
    puz.printdistances()
    print('Evaluation: ', puz.evaluation)
    

    #app.printdistances()

    #app.canvas.itemconfig(app.rect[n,n], fill='green')
    #app.canvas.itemconfig(app.label[2,7], text='234')
    
    