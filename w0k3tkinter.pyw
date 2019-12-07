from tkinter import *
import sys
top = Tk()
mb = Menubutton(exit, Text="Sulge programm", relief = RAISED)

variandid = ["hommik", "lõuna", "õhtu"]
vajutati = ("Mis aeg päevast praegu on?")
kell = ("Sisesta kellaaeg, mil sa kuskil olema pead (formaadis tunnid:minutid): ")

if vajutati == "hommik":
    a = ("Palju aega (minutites) planeerid sa kulutada voodist püsti tõusmisele? ")
    b = ("Palju aega (minutites) planeerid sa kulutada duši all käimisele? ")
    c = ("Palju aega (minutites) planeerid sa kulutada hammaste pesemisele? ")
    d = ("Palju aega (minutites) planeerid sa kulutada muule kehahooldusele (kreemitamine jne)? ")
    e = ("Palju aega (minutites) planeerid sa kulutada hommikusöögile? ")
    f = ("Palju aega (minutites) planeerid sa kulutada nõude pesemisele/muudele koristustegevustele? ")
    h = ("Palju aega (minutites) planeerid sa kulutada riietumisele? ")
    i = ("Palju aega (minutites) planeerid sa kulutada meikimisele? ")
    j = ("Palju aega (minutites) planeerid sa kulutada koti pakkimisele? ")
    k = ("Palju aega (minutites) planeerid sa kulutada kohale jõudmisele? ")
    l = ("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ")
    summa = a + b + c + e + d + f + h + i + j + k + l
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = int(oigekell[0]) - tunnid
    valjaminutid = int(oigekell[1]) - minutid
    if valjatund < 0:
        valjatund = 24 - abs(valjatund)
    if valjaminutid < 0:
        valjatund = valjatund - 1
        valjaminutid = abs(valjaminutid)
    
        
    
    (("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
if vajutati == "lõuna":
    a = ("Palju aega (minutites) planeerid sa kulutada lõunasöögile? ")
    b = ("Palju aega (minutites) planeerid sa kulutada koristamisele? ")
    c = ("Palju aega (minutites) planeerid sa kulutada sarja vaatamisele? ")
    d = ("Palju aega (minutites) planeerid sa kulutada enda korrastamisele? ")
    e = ("Palju aega (minutites) kulutad sa koti kokku pakkimisele? ")
    f = ("Palju aega (minutites) kulutad sa kohale jõudmisele? ")
    h = ("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ")
    summa = a + b + c + d + e + f + h
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = int(oigekell[0]) - tunnid
    valjaminutid = int(oigekell[1]) - minutid
    if valjatund < 0:
        valjatund = 24 - abs(valjatund)
    if valjaminutid < 0:
        valjatund = valjatund - 1
        valjaminutid = abs(valjaminutid)
    
    (("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
if vajutati == "õhtu":
    a = ("Palju aega (minutites) planeerid sa kulutada pesemisele? ")
    b = ("Palju aega (minutites) planeerid sa kulutada õhtusöögile? ")
    c = ("Palju aega (minutites) planeerid sa kulutada meigile? ")
    d = ("Palju aega (minutites) planeerid sa kulutada riietumisele? ")
    e = ("Palju aega (minutites) planeerid sa kulutada soojendamisele? ")
    f = ("Palju aega (minutites) kulutad sa kohale jõudmisele? ")
    h = ("Kui palju aega (minutites) kulub tegevustele, mida me Sinu käest ei küsinud? ")
    summa = a + b + c + e + d + f + h
    tunnid = summa // 60
    minutid = summa - (tunnid * 60)
    oigekell = kell.split(":")
    valjatund = int(oigekell[0]) - tunnid
    valjaminutid = int(oigekell[1]) - minutid
    if valjatund < 0:
        valjatund = 24 - abs(valjatund)
    if valjaminutid < 0:
        valjatund = valjatund - 1
        valjaminutid = abs(valjaminutid)
    
    (("Sinu tegevusteks läheb kokku " + str(tunnid) + " tundi " + "ja " + str(minutid) + " minutit." + 
            "Sa peaksid tegvusi alustama kell " + str(valjatund) + ":" + str(valjaminutid) + "." ))
    
    
class GameGUI(object):

    def __init__(self, root):
        self.root = root

        self.GameButton = Button(root, text="Arvuta aeg!", command=self.NewGame)
        self.GameLabel = Label(root, text="Hommik", fg="blue", font=("Helvetica",16))

        self.GameButton = Button(root, text="Arvuta aeg!", command=self.NewGame)
        self.GameLabel = Label(root, text="Lõuna", fg="blue", font=("Helvetica",16))

        self.GameButton = Button(root, text="Arvuta aeg!", command=self.NewGame)
        self.GameLabel = Label(root, text="Õhtu", fg="blue", font=("Helvetica",16))

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
        self.GameButton.grid()
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