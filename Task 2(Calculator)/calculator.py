import tkinter as tk

def click(button_text):
    if button_text == '=':
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == 'C':
        entry.delete(0, tk.END)  # Clear the entry
    else:
        entry.insert(tk.END, button_text)  # Add button text to entry

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x600")
root.config(bg="#f0f0f0")

# Entry widget to display calculations
entry = tk.Entry(root, font=('Arial', 24), bg="#ffffff", bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button configuration
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons and place them in the grid
row_val = 1
col_val = 0
for button in buttons:
    btn = tk.Button(root, text=button, padx=10, pady=10, font=('Arial', 16), bg="#87CEEB",
                    command=lambda b=button: click(b))
    btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make the grid responsive
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()
