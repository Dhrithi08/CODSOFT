import tkinter as tk
import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Please choose a length of at least 4.")
        else:
            password = generate_password(length)
            result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Length entry
length_label = tk.Label(root, text="Enter Password Length (at least 4):", bg="#f0f0f0", font=('Arial', 14))
length_label.pack(pady=10)

length_entry = tk.Entry(root, font=('Arial', 14), width=5)
length_entry.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate Password", font=('Arial', 14), bg="#87CEEB", command=on_generate)
generate_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=('Arial', 14))
result_label.pack(pady=10)

# Run the application
root.mainloop()
