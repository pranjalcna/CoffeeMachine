import tkinter as tk
from tkinter import ttk


def button_latte_click_handler():
    string_selected_drink.set('Latte Selected. Please enter $2.50')


def button_espresso_click_handler():
    string_selected_drink.set('Espresso Selected. Please enter $1.50')


def button_cappuccino_click_handler():
    string_selected_drink.set('Cappuccino Selected. Please enter $3.00')


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

button_espresso = ttk.Button(frame_coffee, text='Espresso', command=button_espresso_click_handler)
button_espresso.grid(column=1, row=1)

button_cappuccino = ttk.Button(frame_coffee, text='Cappuccino', command=button_cappuccino_click_handler)
button_cappuccino.grid(column=2, row=1)

string_selected_drink = tk.StringVar()
entry_selected_drink = ttk.Entry(frame_coffee, width=40, textvariable=string_selected_drink, state='readonly')
entry_selected_drink.grid(columnspan = 3, row = 2)

root.mainloop()
