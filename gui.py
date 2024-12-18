import tkinter
from random import choice
from tkinter import *
from main import *

root = Tk()
root.resizable(False, False)

root.title('Estimation Calculator')

def get_input(event) -> None:
    selected: str = entry_line.get().lower().strip()
    entry_line.delete(0, tkinter.END)
    return menu(selected)

def sequence(selected) -> None:
    menu(selected)

def update_bottom(bottom) -> None:
    text_bot.config(text=f'{bottom}')

main_canvas = tkinter.Canvas(master=root, background="snow3", width=400, height=300)
main_canvas.pack()

logo_image = tkinter.PhotoImage(master=main_canvas, file="Logo EZ Impress.png")
title_label = tkinter.Label(master=main_canvas, image=logo_image, height=200, width= 450, background="snow3")
title_label.pack()

text_top = tkinter.Label(master=main_canvas, background="snow3", text="Select your quick estimation type: ",
                           font=('Consolas', 15), width=50, height=10, wraplength=400)
text_top.pack(pady=5)

text_bot = tkinter.Label(master=main_canvas, background="snow3", text="I shou",
                           font=('Consolas', 15), width=50, height=10, wraplength=400)
text_bot.pack(pady=5)

entry_line = tkinter.Entry(master=main_canvas, background="snow3", width=50)
entry_line.bind("<Return>", get_input)

entry_line.pack(pady=2)

button_1 = tkinter.Button(master=main_canvas, text=" Restart ", font=('Consolas', 15), bg="white", anchor="w", command=root.destroy)
button_1.pack(padx = 20 ,pady=3)


def main() -> None:
    root.mainloop()

if __name__ == '__main__':
    main()