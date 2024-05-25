from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")

to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=current_card["French"])


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

canvas = Canvas(width=800, height=600)

card_front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(410, 300, image=card_front_image)
title = canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=2)

next_card()

window.mainloop()

