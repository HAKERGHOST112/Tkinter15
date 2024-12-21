import tkinter as tk
from tkinter import PhotoImage
import random


root = tk.Tk()
root.title("Смайлик")
root.geometry("400x400")


image_path = "C:/Users/koa93/Downloads/Без-названия.pgm"
img = PhotoImage(file=image_path)

# Функция для перемещения кнопки
def move_button():
    new_x = random.randint(0, root.winfo_width() - 100)
    new_y = random.randint(0, root.winfo_height() - 100)
    button.place(x=new_x, y=new_y)

# Кнопка с изображением
button = tk.Button(root, image=img, command=move_button)
button.place(x=150, y=150)


root.mainloop()
