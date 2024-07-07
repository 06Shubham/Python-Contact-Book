Explanation:

    Tkinter GUI Setup: We create a main window (root) and various widgets such as labels, entry fields (Entry), buttons (Button), a listbox (Listbox), and a label (Label) to display contact details.

    Functions:

        add_contact: Handles adding a new contact to the contacts dictionary, updates the GUI listbox, clears entry fields, saves contacts to contacts.txt, and displays a success message.

        update_contact_list: Clears and updates the contact_listbox with names from the contacts dictionary.

        show_contact_details: Retrieves and displays contact details when a contact name is selected from the contact_listbox.

        clear_entries: Clears the entry fields (name_entry, number_entry, email_entry).

        load_contacts and save_contacts: Functions to load contacts from and save contacts to contacts.txt file using basic file I/O. eval() is used cautiously here for simplicity to read/write Python dictionaries to/from file, but for production code, consider using JSON or other safe serialization methods.