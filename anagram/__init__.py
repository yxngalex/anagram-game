from .word import anagram
from .player import Player
from .timer import Timer
from tkinter import *

window = Tk()
window.title("CS324-PZ: Anagram Solver by Aleksa Cekic")
window.geometry("600x400")
window.resizable(True, True)

header = Label(text="Anagram Solver", font=("Helvetica", 24))
header.pack(pady=20)

startFrame = Frame(window)
playerFrame = Frame(window)
mainGameFrame = Frame(window)

playerList = list()


def go_to_player_frame():
    playerFrame.pack(fill='both', expand=1)
    startFrame.pack_forget()


def go_to_game_frame():
    mainGameFrame.pack(fill='both', expand=1)
    playerFrame.pack_forget()


def player_input(num_players_entry):
    a = int(num_players_entry.get())

    if a > 0:
        go_to_player_frame()
        label2 = Label(playerFrame, font=("Helvetica", 12), text="Set name for player {}".format(a))
        label2.pack(pady=20)

        input_field = Entry(playerFrame, width=25)
        input_field.pack(pady=20)

        btn = Button(playerFrame, text="Done", command=lambda: create_players(input_field, playerFrame, a))
        btn.pack(pady=20)
    else:
        go_to_game_frame()
        print(playerList)


# print(type(num_players_entry))
# num = int(num_players_entry.get())
# labelText = StringVar()
# label2.pack(pady=20)
#
#
# for i in range(num):
#     labelText.set("Set name for player {}".format(i + 1))
#


def create_players(name, frame, num):
    p = Player(name.get())
    playerList.append(p)
    clear_frame(frame)
    t = IntVar(None, num - 1)
    player_input(t)


def player_selection():
    startFrame.pack()
    label1 = Label(startFrame, text="Enter players (1 - 4): ", font=("Helvetica", 14))
    label1.pack(pady=20)
    options = [1, 2, 3, 4]
    clicked = IntVar(startFrame)
    clicked.set(options[0])

    drop = OptionMenu(startFrame, clicked, *options)
    drop.pack(pady=20)

    btn = Button(startFrame, text="Okay", command=lambda: player_input(clicked))
    btn.pack(pady=20)


def game_frame():
    print("game frame")
    print(playerList)


def main():
    player_selection()
    # a = anagram(9)
    # print(a)

    window.mainloop()


def clear_frame(frame):
    for w in frame.winfo_children():
        w.destroy()
