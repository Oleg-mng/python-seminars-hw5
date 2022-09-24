# Задача 23
# Создайте программу для игры в ""Крестики-нолики"".
from logging import root
from tkinter import *
import random
import time


def push(b):
    global game
    global game_left
    global turn
    if b==4 and turn==0:
        t=random.choice(game_left)
    elif b!=4 and turn==0:
        t=4
    game[b]='X'
    buttons[b].config(text='X', bg="white", state ="disabled")
    game_left.remove(b)
    t=random.choice(game_left)
    game[t]='0'
    time.sleep(0.5)
    buttons[t].config(text='0', bg="white", state ="disabled")
    t+=1



game = [None]*9
game_left = list(range(9))
turn=0

root = Tk()
label = Label(width=20, text="Игра Крестики-нолики",
              font=('Arial', 20, 'bold'))
buttons = [Button(width=5, height=2, font=('Arial', 28, 'bold'),
                  bg="green", command=lambda x=i: push(x)) for i in range(9)]

# button_0 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="black")
# button_1 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="black")
# button_2 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="black")
# button_3 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="grey")
# button_4 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="grey")
# button_5 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="grey")
# button_6 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="grey")
# button_7 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="grey")
# button_8 = Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="grey")

label.grid(row=0, column=0, columnspan=3)
row = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0


# button_0.grid(row=1, column=0)
# button_1.grid(row=1, column=1)
# button_2.grid(row=1, column=2)
# button_3.grid(row=2, column=0)
# button_4.grid(row=2, column=1)
# button_5.grid(row=2, column=2)
# button_6.grid(row=3, column=0)
# button_7.grid(row=3, column=1)
# button_8.grid(row=3, column=2)

root.mainloop()
# def clicked():
#     lbl.configure(text="Х")
#     lbl.grid(column=4, row=4)

# window = Tk()
# window.geometry('400x400')
# window.title("Добро пожаловать в Крестики-нолики")
# lbl = Label(window, text="Игра с ботом" , font=("Arial Bold", 15))
# lbl.grid(column=0, row=0)
# lbl = Label(window, text="Сделай ход", font=("Arial Bold", 12))
# lbl.grid(column=0, row=1)
# btn = Button(window, text=" ", command=clicked)
# btn.grid(column=3, row=3)
# btn = Button(window, text=" ")
# btn.grid(column=3, row=4)
# btn = Button(window, text=" ")
# btn.grid(column=3, row=5)
# btn = Button(window, text=" ")
# btn.grid(column=1, row=3)
# btn = Button(window, text=" ")
# btn.grid(column=1, row=4)
# btn = Button(window, text=" ")
# btn.grid(column=1, row=5)
# btn = Button(window, text=" ")
# btn.grid(column=2, row=3)
# btn = Button(window, text=" ")
# btn.grid(column=2, row=4)
# btn = Button(window, text=" ")
# btn.grid(column=2, row=5)
# window.mainloop()
