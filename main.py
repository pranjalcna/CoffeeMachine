import tkinter as tk
from tkinter import ttk


def button_latte_click_handler():
    string_selected_drink.set('Latte Selected. Please enter $2.50')


def button_espresso_click_handler():
    string_selected_drink.set('Espresso Selected. Please enter $1.50')


def button_cappuccino_click_handler():
    string_selected_drink.set('Cappuccino Selected. Please enter $3.00')


def button_toonie_click_handler():
    string_amount.set(f'Amount Entered: ${float(string_amount.get().split("$")[-1]) + 2:.2f}')


def button_loonie_click_handler():
    string_amount.set(f'Amount Entered: ${float(string_amount.get().split("$")[-1]) + 1:.2f}')


def button_quarter_click_handler():
    string_amount.set(f'Amount Entered: ${float(string_amount.get().split("$")[-1]) + 0.25:.2f}')


def button_dime_click_handler():
    string_amount.set(f'Amount Entered: ${float(string_amount.get().split("$")[-1]) + 0.1:.2f}')


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
entry_selected_drink.grid(columnspan=3, row=2)

button_toonie = ttk.Button(frame_coffee, text='$2.00', command=button_toonie_click_handler).grid(column=0, row=3)
button_loonie = ttk.Button(frame_coffee, text='$1.00', command=button_loonie_click_handler).grid(column=1, row=3)
button_quarter = ttk.Button(frame_coffee, text='$0.25', command=button_quarter_click_handler).grid(column=2, row=3)
button_dime = ttk.Button(frame_coffee, text='$0.10', command=button_dime_click_handler).grid(column=3, row=3)

string_amount = tk.StringVar()
entry_amount = ttk.Entry(frame_coffee, width=40, textvariable=string_amount, state='readonly')
entry_amount.grid(columnspan=3, row=4)
string_amount.set("Amount Entered: $0.00")

root.mainloop()
