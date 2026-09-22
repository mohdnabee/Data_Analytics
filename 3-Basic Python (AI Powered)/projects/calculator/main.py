import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator - Nabeel")
root.geometry("300x400")
root.resizable(True, True)

# Entry field
entry = tk.Entry(
    root,
    font=("Arial", 20),
    borderwidth=5,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button click handler
def button_click(value):
    entry.insert(tk.END, value)

# Clear display
def clear_display():
    entry.delete(0, tk.END)

# Calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Frame for buttons
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            frame,
            text=text,
            font=("Arial", 16),
            command=calculate
        )
    else:
        btn = tk.Button(
            frame,
            text=text,
            font=("Arial", 16),
            command=lambda t=text: button_click(t)
        )

    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Clear button
clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 16),
    command=clear_display
)
clear_btn.pack(fill="both", padx=10, pady=5)

# Configure grid resizing
for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# Run app
root.mainloop()
