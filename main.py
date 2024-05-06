from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Python_game.com - Tic-Tac-Toe')
root.iconbitmap('C:\Users\Admin\gui\favicon_io')
#root.geometry("1200x710")

#button clicked function
def b_click(b):
    pass
#built our buttons

b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))

root.mainloop()