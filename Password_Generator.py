import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            password_result.config(text="Length must be at least 1.")
            return
    except ValueError:
        password_result.config(text="Invalid input. Please enter a number.")
        return

    # Generate the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    # Display the password
    password_result.config(text="Generated Password: " + password)

# Function to accept the generated password
def accept_password():
    user_name = name_entry.get()
    generated_password = password_result.cget("text")
    accepted_passwords.config(state="normal")
    accepted_passwords.insert(tk.END, f"{user_name}: {generated_password}\n")
    accepted_passwords.config(state="disabled")

# Function to reset the generated password
def reset_password():
    length_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    password_result.config(text="")
    accepted_passwords.config(state="normal")
    accepted_passwords.delete(1.0, tk.END)
    accepted_passwords.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x275+300+150")

# Create and configure the label for password length
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

# Create and configure the entry field for password length
length_entry = tk.Entry(root)
length_entry.pack()

# Create and configure the label for user's name
name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack()

# Create and configure the entry field for user's name
name_entry = tk.Entry(root)
name_entry.pack()

# Create and configure the generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Create and configure the result label
password_result = tk.Label(root, text="", wraplength=200)
password_result.pack()

# Create and configure the accept button
accept_button = tk.Button(root, text="Accept Password", command=accept_password)
accept_button.pack()

# Create and configure the reset button
reset_button = tk.Button(root, text="Reset", command=reset_password)
reset_button.pack()

# Create and configure the text widget for accepted passwords
accepted_passwords = tk.Text(root, height=5, width=30, state="disabled")
accepted_passwords.pack()

# Start the main event loop
root.mainloop()
