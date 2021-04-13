import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Coffee Machine')
root.geometry('400x300')

frame_coffee = ttk.Frame(root)
frame_coffee.pack(fill=tk.BOTH, expand=True)



root.mainloop()
