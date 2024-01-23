import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize contact list
        self.contacts = []

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets for contact details
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Phone Number:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.root, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        view_button.grid(row=5, column=0, columnspan=2, pady=10)

        search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        search_button.grid(row=6, column=0, columnspan=2, pady=10)

        update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        update_button.grid(row=7, column=0, columnspan=2, pady=10)

        delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone Number are required.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = "\n".join([f"{contact['Name']} - {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
        if search_term:
            results = [contact for contact in self.contacts
                       if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]]
            if results:
                contact_list = "\n".join([f"{contact['Name']} - {contact['Phone']}" for contact in results])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter Name or Phone Number:")
        if search_term:
            results = [contact for contact in self.contacts
                       if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]]
            if results:
                # Display the first matching contact for simplicity
                contact = results[0]

                # Prompt user for updated details
                updated_name = simpledialog.askstring("Update Name", f"Current Name: {contact['Name']}\nNew Name:")
                updated_phone = simpledialog.askstring("Update Phone", f"Current Phone: {contact['Phone']}\nNew Phone:")
                updated_email = simpledialog.askstring("Update Email", f"Current Email: {contact['Email']}\nNew Email:")
                updated_address = simpledialog.askstring("Update Address", f"Current Address: {contact['Address']}\nNew Address:")

                # Update contact details
                contact["Name"] = updated_name if updated_name else contact["Name"]
                contact["Phone"] = updated_phone if updated_phone else contact["Phone"]
                contact["Email"] = updated_email if updated_email else contact["Email"]
                contact["Address"] = updated_address if updated_address else contact["Address"]

                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter Name or Phone Number:")
        if search_term:
            results = [contact for contact in self.contacts
                       if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]]
            if results:
                # Display the first matching contact for simplicity
                contact = results[0]
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
