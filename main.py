from puzzle import Puzzle
from gui import Gui
import sys
import itertools


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



def bfs(puz):
    evaluation = puz.evaluation
    print(evaluation)

def spf(puz):
    evaluation = puz.evaluation
    print(evaluation)


def astar(puz):
    evaluation = puz.evaluation
    print(evaluation)



if __name__ == "__main__":

    i = readpositiveint('\nPuzzle Generation Tactics \n1: Random Puzzle\n2: Hill Climbing\n3: Genetic Algorithm\n\nEnter your choice: ')

    if i == 1:
        dim = readpositiveint('Puzzle dimension: ')
        puz = Puzzle(dim)

    elif i == 2:
        print('\n----- Hill Climbing -----\n')

        dim = readpositiveint('Puzzle dimension: ')
        iters = readpositiveint('Algorithm iterations: ')

        puz = hillclimbing(dim, iters)

    elif i == 3:
        print('\n----- Genetic Algorithm -----\n')

        dim = readpositiveint('Puzzle dimension: ')
        iters = readpositiveint('Algorithm iterations: ')
        
        # dim: puzzle dimension, iters: iterations of algorithm
        puz = geneticalgorithm(dim, iters)

    else:
        print('Invalid choice...')
        sys.exit()
    

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
    