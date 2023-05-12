# Importing necessary modules
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Password generator function
def generate_password():
    # Define letters, numbers, and symbols to be used in generating the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Choose a random number of letters, symbols, and numbers to be used in generating the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine the letters, symbols, and numbers and shuffle them
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Join the elements of the password_list and insert the generated password in the password_entry field
    password = "".join(password_list)
    password_entry.insert(0, password)
    # Copy the generated password to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get the user inputs for website, email, and password
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Create a new dictionary with the input data
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if any fields are left empty
    if len(website) == 0 or len(password) == 0:
        # Show an error message if any field is empty
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Try to open the JSON file
            with open("data.json", "r") as data_file:
                # Load the old data from the JSON file
                data = json.load(data_file)
        except FileNotFoundError:
            # If the JSON file does not exist, create it and write the new data to it
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update the old data with the new data
            data.update(new_data)

            # Write the updated data to the JSON file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Clear the website and password entry fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        # Open the data file in read mode and load the data
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # If the data file is not found, show an error message
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        # If the website exists in the data, retrieve the email and password
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            # Show the email and password as a message box
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            # If the website does not exist in the data, show an error message
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Website Label and Entry
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")
website_entry.focus()

# Email/Username Label and Entry
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")
email_entry.insert(0, "denchikdron228@gmail.com")

# Password Label and Entry
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=10, pady=10)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2, padx=10, pady=10)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
