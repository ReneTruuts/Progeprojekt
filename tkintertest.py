from tkinter import *
from tkinter import ttk
import sys

class GameGUI(object):

    def __init__(self, root):
        self.root = root

        self.GameButton1 = Button(root, text="Arvuta aeg!", command=self.NewGame)
        self.GameLabel1 = Label(root, text="Hommik", fg="blue", font=("Helvetica",16))

        self.GameButton2 = Button(root, text="Arvuta aeg!", command=self.NewGame)
        self.GameLabel2 = Label(root, text="Lõuna", fg="blue", font=("Helvetica",16))

        self.GameButton3 = Button(root, text="Arvuta aeg!", command=self.NewGame)
        self.GameLabel3 = Label(root, text="Õhtu", fg="blue", font=("Helvetica",16))

        self.HelpButton = Button(root, text="Meie programmist", command=self.Help)
        self.HelpLabel = Label(root, text="", fg="orange", font=("Helvetica",16))

        self.ExitButton = Button(root, text="Välju",command=self.Exit)
        self.ExitLabel = Label(root, text="Vajuta, et väljuda", fg="red", font=("Helvetica",16))

        self.InstructionsLabel = Label(root, text="""
            Taken from nrich.maths.org

            This is a collection of games of skill for two players, both players have exactly the same information, chance plays no part,
            and each game must terminate. There is always a 'winning strategy' and all the moves can be analysed mathematically. The only
            advantage that either player can possibly have is to start or to play second. To work out how to win you need to start by
            analysing the 'end game', and the losing position to be avoided, and then work back to earlier moves. Can you find the winning strategies?

            The rules are simple. Start with any number of counters in any number of piles. Two players take turns to remove any number of
            counters from a single pile. The winner is the player who takes the last counter.""", fg="black", font=("Calibri", 14))

        self.ReturnMenu = Button(root, text="Return to Main Menu", command=self.MainMenu)

        self.MainMenu()

    def MainMenu(self):
        self.RemoveAll()
        self.GameButton1.grid()
        self.GameButton2.grid()
        self.GameButton3.grid()
        self.GameLabel.grid()
        self.HelpButton.grid()
        self.HelpLabel.grid()
        self.ExitButton.grid()
        self.ExitLabel.grid()

    def NewGame(self):
        self.GameButton.grid_remove()
        self.GameLabel.grid_remove()
        self.ExitButton.grid_remove()
        self.ExitLabel.grid_remove()

    def Help(self):
        self.RemoveAll()

        self.InstructionsLabel.grid()
        self.ReturnMenu.grid()

    def RemoveAll(self):
        self.GameButton.grid_remove()
        self.GameLabel.grid_remove()
        self.HelpButton.grid_remove()
        self.HelpLabel.grid_remove()
        self.ExitButton.grid_remove()
        self.ExitLabel.grid_remove()
        self.InstructionsLabel.grid_remove()
        self.ReturnMenu.grid_remove()

    def Exit(self):
        self.root.quit
        sys.exit(0)


if __name__ == '__main__':

    root = Tk()
    GameGUI = GameGUI(root)
    root.mainloop()