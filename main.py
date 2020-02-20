from puzzle import Puzzle
from gui import Gui




def hillclimbing(iters):
    print('Calling hill climbing on: ', iters)




if __name__ == "__main__":
    s = input('\nPuzzle Generation Tactics \n1: Random Puzzle\n2: Hill Climbing\n3: Genetic Algorithm\n\nEnter your choice: ')
    print()

    try:
        i = int(s)
    except ValueError:
        i = -1

    if i == 1:
        ns = input('Puzzle dimension: ')
        try:
            ni = int(ns)
        except ValueError:
            ni = -1

        if ni < 1:
            print('Invalid puzzle dimension...')
        else:
            puz = Puzzle(ni)
            gui = Gui(puz)
            gui.title('Puzzle')
            gui.mainloop()

    elif i == 2:
        ns = input('Iterations: ')
        try:
            ni = int(ns)
        except ValueError:
            ni = -1

        if ni < 1:
            print('Invalid iteration number...')
        else:
            hillclimbing(ni)

    elif i == 3:
        print(3)

    else:
        print("Invalid choice...")
    