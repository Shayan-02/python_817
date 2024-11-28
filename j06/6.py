import tkinter as tk
from tkinter import messagebox


# Function to perform the calculations
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)


# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for display
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button values
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("C", 4, 0),
    ("0", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
]

# Create buttons dynamically
for text, row, col in buttons:
    if text == "=":
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_equal)
    elif text == "C":
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_clear)
    else:
        button = tk.Button(
            root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t)
        )
    button.grid(row=row, column=col)

# Run the app
root.mainloop()
