from puzzle import Puzzle
from gui import Gui
import sys


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
        print(3)

    else:
        print("Invalid choice...")
    