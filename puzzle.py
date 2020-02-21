import tkinter as tk
import random

#Square Width: 25, Square Height: 25


class Puzzle:
    def __init__(self, n):

        # Initial data
        self.n = n
        self.movenums = {}
        self.distances = {}
        self.evaluation = 0

        # Generate puzzle and populate stored data
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

    # Returns the coordinates of swap and old/new values
    def swaprandommovenum(self):
        n = self.n

        x = n
        y = n

        while x == n and y == n:
            x = random.randint(1, n)
            y = random.randint(1, n)

        bound = max(y - 1, n - x, x - 1, n - y)
        new = random.randint(1, bound)
        old = self.movenums[x, y]

        self.movenums[x, y] = new

        self.calculatemindistances()
        self.evaluate()

        return (x, y, old, new)

    
    def revertswap(self, swp):
        self.movenums[swp[0], swp[1]] = swp[2]
        self.calculatemindistances()
        self.evaluate()

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
        print("\nPuzzle: ")
        n = self.n
        for y in range(1, n + 1):
            for x in range(1, n + 1):
                print(self.movenums[(x,y)], end = ' ')
            print()

    def printdistances(self):
        print("\nSolution: ")
        n = self.n
        for y in range(1, n + 1):
            for x in range(1, n + 1):
                print(self.distances[(x,y)], end = ' ')
            print()

    def printswap(self, swp):
        print('Swap: (',swp[0],',',swp[1],'): ', swp[2], '->', swp[3])

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


    def astar(self):
        print('Calling A Star with evaluation: ', self.evaluation)

    def bfs(self):
        print('Calling bfs with evaluation: ', self.evaluation)

    def spf(self):
        print('Calling spf with evaluation: ', self.evaluation)

        

