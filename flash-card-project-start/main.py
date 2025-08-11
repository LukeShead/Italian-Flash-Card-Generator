from tkinter import *
import pandas as pand
import random as rand


BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
MAIN_FONT = ("Ariel", 60, "bold")


# create the interface
'''
Get the main window
put the mainloop at the bottom

Set out a canvas for the images

place the main image of white square to start

place the title and flash card word to be used

place the two images of WRONG or RIGHT in the their place.

USE GRID TO DO THIS.

read the csv with the data.
create dictionary out of it
use the french definition of it

'''

def generate_new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rand.choice(to_learn)
    main_canvas.itemconfig(background_image, image= card_front)
    main_canvas.itemconfig(language, text="Italian", fill="black")
    main_canvas.itemconfig(lang_word, text=f"{current_card["Italian"]}", fill="black")

    flip_timer = window.after(3000, func=display_english)


def display_english():
    main_canvas.itemconfig(background_image, image=card_back)
    main_canvas.itemconfig(language, text="English", fill="white")
    main_canvas.itemconfig(lang_word, text=f"{current_card["English"]}", fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pand.DataFrame(to_learn)
    data.to_csv("data\words_to_learn.csv", index=False)


    generate_new_card()

window = Tk()
window.title("Flash Card Machine")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=display_english)

main_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
correct_image = PhotoImage(file="./images/right.png")
incorrect_image = PhotoImage(file="./images/wrong.png")

background_image = main_canvas.create_image(400, 260, image=card_front)
main_canvas.grid(row=0, column=0,columnspan=2)

to_learn = {}
current_card = {}

try:
    data = pand.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pand.read_csv("data/italian.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




language = main_canvas.create_text(400, 150, font=LANG_FONT, text="")
lang_word = main_canvas.create_text(400, 263, font=MAIN_FONT, text="")

right_butt = Button(image=correct_image, command=is_known)
right_butt.grid(column=1, row=1)

wrong_butt = Button(image=incorrect_image, command=generate_new_card)
wrong_butt.grid(column=0, row=1)


generate_new_card()



# window.after(3000, main_canvas.itemconfig(background_image, image=card_back))


# with open("./data/french_words.csv", "r") as data:
#     words = data.readlines()
#     words[0].split(",")
#     print(words)
#     print(words[1])




window.mainloop()