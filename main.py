from puzzle import Puzzle
from gui import Gui

if __name__ == "__main__":
    puz = Puzzle(23)
    gui = Gui(puz)
    gui.title('Puzzle 1')
    gui.showmovenums()
    
    gui.mainloop()
    

    #app.canvas.itemconfig(app.rect[n,n], fill='green')
    #app.canvas.itemconfig(app.label[2,7], text='234')