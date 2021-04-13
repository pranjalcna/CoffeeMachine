import tkinter as tk
from tkinter import ttk


def button_latte_click_handler():
    print('I want some coffee')


# Step 1: Create Root Window
root = tk.Tk()
root.title('Coffee Machine')
root.geometry('400x300')

# Step 2: Create Frame
frame_coffee = ttk.Frame(root)
frame_coffee.pack(fill=tk.BOTH, expand=True)

# Step 3: Start Adding UI Elements
label_title = ttk.Label(frame_coffee, text='Coffee Machine')
label_title.grid(columnspan=3, row=0)

button_latte = ttk.Button(frame_coffee, text='Latte', command=button_latte_click_handler)
button_latte.grid(column=0, row=1)

root.mainloop()
