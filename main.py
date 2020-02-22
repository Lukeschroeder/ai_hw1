from puzzle import Puzzle
from gui import Gui
import sys
import itertools
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import random

def hillclimbing(dim, iters):
    puz = Puzzle(dim)
    puz.printmovenums()
    puz.printdistances()

    initialevaluation = puz.evaluation

    evaluation = puz.evaluation

    for i in range(1, iters + 1):

        swp = puz.swaprandommovenum()

        # Evaluation dropped so revert swap
        if puz.evaluation < evaluation:
            print('\nEvaluation worsened... reverting swap')
            puz.revertswap(swp)
            continue
        else:
            evaluation = puz.evaluation
            print('\nIteration: ', i)
            puz.printswap(swp)
            print('Evaluation: ', evaluation)

            # UNCOMMENT IF YOU WANT FULL DETAILS OF SWAP           
            # puz.printmovenums()
            # puz.printdistances()
            
    print('\n----- RESULTS -----')
    print('Initial Evaluation: ', initialevaluation)
    print('Final Evaluation: ', evaluation)
    return puz



def generate(dim, n):
    print('Generating initial population... ')
    population = [Puzzle(dim) for i in range(1, n + 1)]
    print('Population generated of size: ', int(len(population)))

    return population


def select(population, d):
    print('Applying Selection...')
    population.sort(key = lambda puz: puz.evaluation, reverse = True)
    population = population[:int(len(population) * d)]
    print('Population selected of size: ', int(len(population)))
    return population


def mate(puztuple):
    puza = puztuple[0]
    puzb = puztuple[1]

    distsa = puza.distances
    distsb = puzb.distances
    movesa = puza.movenums
    movesb = puzb.movenums

    n = puza.n

    outmoves = {}

    for x in range(1, n + 1):
        for y in range(1, n + 1):

            if(distsa[(x, y)] > distsb[(x, y)]):
                outmoves[(x, y)] = movesa[(x, y)]
            else:
                outmoves[(x, y)] = movesb[(x, y)]
 
    babypuz = Puzzle(n)
    babypuz.movenums = outmoves
    babypuz.calculatemindistances()
    babypuz.evaluate()

    return babypuz


def crossover(population):
    print('Applying Crossover...')
    newpop = []
    for i in itertools.product(population, population):
        newpop.append(mate(i))
    population = newpop
    print('Population mated of size: ', int(len(population)))
    return population

def mutate(population, i):
    print('Mutating Population...')
    for puz in population:
        for j in range(1, i + 1):
            evaluation = puz.evaluation
            swp = puz.swaprandommovenum()
            if puz.evaluation < evaluation:
                puz.revertswap(swp)

    print('Population mutated of size: ', int(len(population)))
    return population

def geneticalgorithm(dim, iters):
    d = .1
    n = 100
    print('Calling Genetic Algorithm with population:', n , 'Selection rate:', d)
    population = generate(dim, n)

    population.sort(key = lambda puz: puz.evaluation, reverse = True)
    initialpopulation = population[:int(len(population) * d)]
    print()

    for i in range(1, iters + 1):
        print(i, ':')     
        population = select(population, d)
        population = mutate(population, 50)
        population = crossover(population)
        print()
        

    population = select(population, d)

    print('\n----- RESULTS -----')

    print('Initial population best: ', end='')
    initialpopulation.sort(key = lambda puz: puz.evaluation, reverse = True)
    for p in initialpopulation:
        print(p.evaluation, end=' ')
    print()

    print('Final population best: ', end='')
    for p in population:
        print(p.evaluation, end=' ')
    print()


    goldenchild = population[0]
    print('Resulting Evaluation: ', goldenchild.evaluation)
    print()
    return goldenchild


def readpositiveint(message):
        s = input(message)
        try:
            i = int(s)
        except ValueError:
            i = -1
        if i < 1:
            print('\nInvalid input...\n')
            sys.exit()
        return i




# --------------------------------------------------------------------------------------------
# Main User Input Execution Loop
def executeuserinputloop():
    i = readpositiveint('\nPuzzle Generation Tactics \n1: From File\n2: Random Puzzle\n3: Hill Climbing\n4: Genetic Algorithm\n\nEnter your choice: ')

    if i == 1:
        print('\n----- Generate from File -----\n')
        filename = input('Input filename: ')
        f = open(filename, 'r')
        puz = Puzzle(int(f.readline()) )
        puz.fromfile(f)

    elif i == 2:
        print('\n----- Random Puzzle -----\n')
        dim = readpositiveint('Puzzle dimension: ')
        puz = Puzzle(dim)

    elif i == 3:
        print('\n----- Hill Climbing -----\n')

        dim = readpositiveint('Puzzle dimension: ')
        iters = readpositiveint('Algorithm iterations: ')

        puz = hillclimbing(dim, iters)

    elif i == 4:
        print('\n----- Genetic Algorithm -----\n')

        dim = readpositiveint('Puzzle dimension: ')
        iters = readpositiveint('Algorithm iterations: ')
        
        # dim: puzzle dimension, iters: iterations of algorithm
        puz = geneticalgorithm(dim, iters)

    else:
        print('Invalid choice...')
        sys.exit()

    puz.printmovenums()
    puz.printdistances()

    i = readpositiveint('\nPuzzle generated... \n1: Display puzzle\n2: Run A*\n3: Run BFS\n4: Run SPF\nEnter your choice: ')

    if i == 1:
        gui = Gui(puz)
        gui.title('Puzzle')
        gui.mainloop()

    elif i == 2:
        puz.astar()

    elif i == 3:
        puz.bfs()

    elif i == 4:
        puz.spf()

    else: 
        print('Invalid choice...')

# Testing population generation algorithms loop
def testpopulationgenerationalgs():
    i = readpositiveint('\nTest...\n1: Genetic\n2: Hill Climbing\n\nEnter your choice: ')
    if i == 1:
        dim = 11
        times = []
        evaluations = []
        iterations = [1, 2, 3, 4, 5, 8, 10, 15]

        for it in iterations:
            vertices = []
            for i in range(1, 51):
                start = timer()
                puz = geneticalgorithm(dim, it)
                end = timer()
                vert = (end - start, puz.evaluation)
                vertices.append(vert)
            
            time = 0
            evaluation = 0
            for x in vertices:
                time += x[0]
                evaluation += x[1]
            avgtime = time / len(vertices)
            avgevaluation = evaluation / len(vertices)
            times.append(avgtime)
            evaluations.append(avgevaluation)
        plt.plot(times, evaluations)
        plt.plot(times, evaluations, 'or')
        plt.title('Genetic Algorithm Computation Time vs. Evaluation, n = 11')
        plt.xlabel('Avg time over 50 runs (s)', fontsize=12)
        plt.ylabel('Avg evaluation', fontsize=12)
        plt.show()

    elif i == 2:
        dim = 11
        times = []
        evaluations = []
        iterations = [10, 20, 50, 75, 100, 200, 500, 750, 1000, 2000, 5000, 10000]

        for it in iterations:
            vertices = []
            for i in range(1, 51):
                start = timer()
                puz = hillclimbing(dim, it)
                end = timer()
                vert = (end - start, puz.evaluation)
                vertices.append(vert)
            
            time = 0
            evaluation = 0
            for x in vertices:
                time += x[0]
                evaluation += x[1]
            avgtime = time / len(vertices)
            avgevaluation = evaluation / len(vertices)
            times.append(avgtime)
            evaluations.append(avgevaluation)
        plt.plot(times, evaluations)
        plt.plot(times, evaluations, 'or')
        plt.title('Hill Climbing Computation Time vs. Evaluation, n = 11')
        plt.xlabel('Avg time over 50 runs (s)', fontsize=12)
        plt.ylabel('Avg evaluation', fontsize=12)
        plt.show()

    else:
        print('Invalid choice...')


def testpathfindingalgs():
    populationsize = 50

    print('Generating random population...')

    population = []
    for n in range(1, populationsize + 1):
        dim = random.randint(3, 14)
        algorithmtype = random.randint(1, 2)

        # Genetic
        if algorithmtype == 1:
            alg = 'GEN'
            iters = random.randint(1, 30)
            print('Algorithm: ', alg, ' Dim: ', dim, 'Iters: ', iters, end=' ')

            puz = geneticalgorithm(dim, iters)

        # Hill Climbing
        elif algorithmtype == 2:
            alg = 'HC'
            iters = random.randint(1, 10000)
            print('Algorithm: ', alg, ' Dim: ', dim, 'Iters: ', iters, end=' ')
            puz = hillclimbing(dim, iters)

        print('Evaluation: ', puz.evaluation)
        population.append(puz)


    astartimes = []
    bstartimes = []
    sstartimes = []
    dims = []

    for p in population: 
        dim = p.n

        dims.append(dim)

        start = timer()
        for i in range(1, 100):
            puz.astar()
        end = timer()
        astartimes.append(end - start)

        start = timer()
        for i in range(1, 100):
            puz.bfs()
        end = timer()
        bstartimes.append(end - start)

        start = timer()
        for i in range(1, 100):
            puz.spf()
        end = timer()
        sstartimes.append(end - start)

    plt.plot(dims, astartimes, 'or')

    plt.plot(dims, bstartimes, 'og')

    plt.plot(dims, sstartimes, 'ob')

    
    plt.title('A*, BFS, and SPF Comparison')
    plt.xlabel('Dimension of puzzle', fontsize=12)
    plt.ylabel('Time for 100 Runs of Algorithm', fontsize=12)
    plt.show()





if __name__ == '__main__':
    executeuserinputloop()
    # testpopulationgenerationalgs()
    # testpathfindingalgs()


