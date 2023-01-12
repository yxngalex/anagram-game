from .word import anagram
from .player import Player
from tkinter import *

window = Tk()
window.title("CS324-PZ: Anagram Solver by Aleksa Cekic")
window.geometry("1280x720")
window.resizable(True, True)

header = Label(text="Anagram Solver", font=("Helvetica", 20))
header.pack(pady=20)

startFrame = Frame(window)
mainGameFrame = Frame(window)

t = StringVar()
t.set("30")

p = Player()


def go_to_game_frame():
    mainGameFrame.pack(fill='both', expand=1)
    startFrame.pack_forget()


def player_input(text, frame):
    if text.get() != "":
        p.set_name(text.get())
    clear_frame(frame)
    game_frame()


def start():
    startFrame.pack()
    label1 = Label(startFrame, text="Enter players name: ", font=("Helvetica", 14))
    label1.pack(pady=20)

    input_field = Entry(startFrame, width=25)
    input_field.pack(pady=20)

    btn = Button(startFrame, text="Okay", command=lambda: player_input(input_field, startFrame))
    btn.pack(pady=20)


def solve(answer, inpt, frame):
    if answer == inpt:
        count = p.get_score() + 1
        p.set_score(count)
        clear_frame(frame)
        game_frame()
    else:
        if p.get_score() > 0:
            count = p.get_score() - 1
            p.set_score(count)
        clear_frame(frame)
        game_frame()


def show(lbl, t):
    lbl.config(text=t)


def game_frame():
    go_to_game_frame()

    player_name = Label(mainGameFrame, text="Name: {}, Score: {}".format(p.get_name(), p.get_score()),
                        font=("Helvetica", 15))
    player_name.pack(pady=20)

    a = anagram(5)

    question_label = Label(mainGameFrame, text="".join(a.get_question()), font=("Helvetica", 12), fg="Red")
    question_label.pack()

    hint = Label(mainGameFrame, text="", font=("Helvetica", 12), fg="Blue")
    hint.pack(pady=20)

    inpt = Entry(mainGameFrame, width=25)
    inpt.pack(pady=20)

    btn_solve = Button(mainGameFrame, text="Solve", command=lambda: solve(a.get_answer(), inpt.get(), mainGameFrame))
    btn_solve.pack(pady=20)

    btn_show = Button(mainGameFrame, text="Show Hint", command=lambda: show(hint, a.get_hint()))
    btn_show.pack(pady=20)

    btn_show = Button(mainGameFrame, text="End Game", command=lambda: save_stats(p, window))
    btn_show.pack(pady=20)


def main():
    start()

    window.mainloop()


def clear_frame(frame):
    for w in frame.winfo_children():
        w.destroy()


def save_stats(plyr, win):
    # saves to file
    file = open("docs/player_score.txt", "a")
    file.write("\n" + plyr.__repr__())
    file.close()
    win.destroy()
