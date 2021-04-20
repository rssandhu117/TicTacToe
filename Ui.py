from Game import Game, GameError
from abc import ABC, abstractmethod
from tkinter import Button, Tk, Frame, X

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()
        
        Button(
            frame,
            text='Show Help',
            command= self._help_callback).pack(fill=X)

        Button(
            frame,
            text='Play',
            command= self._play_callback).pack(fill=X)
    
        Button(
            frame,
            text='Quit',
            command= self._quit_callback).pack(fill=X)
    
        self.__root = root
        
    def _help_callback(self):
    
    def _play_callback(self):
        pass
    
    def _quit_callback(self):
        self.__root.quit()
    
    
    def run(self):
        self.__root.mainloop()

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not self._game.winner:
            print(self._game)
            try:
                row = int(input("Which row? "))
                col = int(input("Which column? "))
            except ValueError:
                # Type check
                print("Invalid Input: Non numeric")
                continue
            # Range check
            if 1 <= row <= 3 and 1 <= col <= 3:
                try:
                    self._game.play(row,col)
                except GameError:
                    print("Invalid Input")
            else:
                print("Invalid Input: Must be between 1 and 3")
            
            
        print(self._game)
        w = self._game.winner
        if self._game.winner == Game.DRAW:
            print("The game was drawn")
        else:
            print(f"The winner was {w}")
