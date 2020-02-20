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
    print('Iterations: ', iters)
    print('Initial Evaluation: ', initialevaluation)
    print('Final Evaluation: ', evaluation)

    gui = Gui(puz)
    gui.title('Puzzle')
    gui.mainloop()


def crossover(puztuple):
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

    return max([puza, puzb, babypuz], key=lambda puz: puz.evaluation)


def geneticalgorithm(dim, n, d):
    print('Calling Genetic Algorithm with population:', n , 'Selection rate:', d)

    # Generation
    print('Generating initial population... ')
    population = [Puzzle(dim) for i in range(1, n + 1)]
    print('Population generated of size: ', int(len(population)))

    for p in population:
        print(p.evaluation)

    # Selection 1
    print('Applying Selection...')
    population.sort(key = lambda puz: puz.evaluation, reverse = True)
    population = population[:int(len(population) * d)]
    print('Population selected of size: ', int(len(population)))

    for p in population:
        print(p.evaluation)

    # Crossover
    newpop = []
    print('Applying Crossover...')
    for i in itertools.product(population, population):
        newpop.append(crossover(i))
    population = newpop
    print('Population mated of size: ', int(len(population)))


    for p in population:
        print(p.evaluation)

    # Selection 2
    print('Applying Selection...')
    population.sort(key = lambda puz: puz.evaluation, reverse = True)
    population = population[:int(len(population) * d)]
    print('Population selected of size: ', int(len(population)))

    for p in population:
        print(p.evaluation)






    




def readpositiveint(message):
        dimstr = input(message)
        try:
            dim = int(dimstr)
        except ValueError:
            dim = -1

        if dim < 1:
            print('\nInvalid input...\n')
            sys.exit()

        return dim



if __name__ == "__main__":
    s = input('\nPuzzle Generation Tactics \n1: Random Puzzle\n2: Hill Climbing\n3: Genetic Algorithm\n\nEnter your choice: ')
    print()

    try:
        i = int(s)
    except ValueError:
        i = -1

    if i == 1:
        dim = readpositiveint('Puzzle dimension: ')

        puz = Puzzle(dim)
        gui = Gui(puz)
        gui.title('Puzzle')
        gui.mainloop()

    elif i == 2:
        print('----- Hill Climbing -----\n')

        dim = readpositiveint('Puzzle dimension: ')
        iters = readpositiveint('Iterations: ')

        hillclimbing(dim, iters)

    elif i == 3:
        print('----- Genetic Algorithm -----\n')

        dim = readpositiveint('Puzzle dimension: ')
        n = 100 
        d = .1

        # dim: puzzle dimension, n: population size, d: rate selected
        geneticalgorithm(dim, n, d)

    else:
        print("Invalid choice...")
    