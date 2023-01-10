from .word import anagram
from .player import Player
from .timer import Timer
import tkinter as tk


def main():
    # window = tk.Tk()
    # greet = tk.Label(text="Hello World")
    # greet.pack()
    a = anagram(9)
    print(a)

    # window.mainloop()
