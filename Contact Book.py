import tkinter as tk
from tkinter import messagebox

# Function to handle adding a new contact
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()

    if not name or not number:
        messagebox.showwarning("Error", "Please enter both Name and Number.")
        return

    if name in contacts:
        messagebox.showwarning("Error", f"Contact '{name}' already exists.")
        return

    contacts[name] = {'Number': number, 'Email': email}
    update_contact_list()
    save_contacts()
    clear_entries()
    messagebox.showinfo("Success", f"Contact '{name}' added successfully.")

# Function to update the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

# Function to display selected contact details
def show_contact_details(event):
    try:
        index = contact_listbox.curselection()[0]
        name = contact_listbox.get(index)
        details = contacts[name]
        details_label.config(text=f"Name: {name}\nNumber: {details['Number']}\nEmail: {details['Email']}")
    except IndexError:
        pass

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Function to load contacts from file
def load_contacts():
    try:
        with open('contacts.txt', 'r') as f:
            contacts = eval(f.read())
    except FileNotFoundError:
        contacts = {}
    return contacts

# Function to save contacts to file
def save_contacts():
    with open('contacts.txt', 'w') as f:
        f.write(str(contacts))

# Initialize tkinter window
root = tk.Tk()
root.title("Contact Book")

# Initialize contacts dictionary
contacts = load_contacts()

# Create and pack widgets
tk.Label(root, text="Name:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, sticky='w', padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

contact_listbox = tk.Listbox(root, width=40, height=10)
contact_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
contact_listbox.bind('<<ListboxSelect>>', show_contact_details)

details_label = tk.Label(root, text="", width=40, height=10, relief=tk.GROOVE)
details_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Load existing contacts into the listbox
update_contact_list()

# Run the tkinter main loop
root.mainloop()
