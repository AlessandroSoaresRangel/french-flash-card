from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def flip():
    canvas.itemconfig(image, image=card_back_image)
    canvas.itemconfig(title, text="English", fill="White")
    canvas.itemconfig(word, text=current_card["English"], fill="White")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="Black")
    canvas.itemconfig(word, text=current_card["French"], fill="Black")
    canvas.itemconfig(image, image=card_front_image)
    flip_timer = window.after_id = window.after(3000, flip)


def right_button_pressed():
    global current_card
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, flip)

canvas = Canvas(width=800, height=600)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
image = canvas.create_image(410, 300, image=card_front_image)
title = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_button_pressed)
right_button.grid(column=1, row=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=2)

next_card()


window.mainloop()

