# Functions
def add_contact(contacts, name, phone_number, email):
    new_contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "favorite": False
    }
    contacts.append(new_contact)
    return

def list_contacts(contacts):
    print("\nContacts:")
    for indice, contact in enumerate(contacts, start=1):
        status = "☆" if contact["favorite"] else " "
        print(f"{indice} - {contact['name']} - {contact['phone_number']} - {contact['email']} - {status}")
    return
        

def edit_contact(contacts, indice, edit_option):
    new_indice = indice - 1
    if new_indice >= 0 or new_indice < len(contacts):
        if edit_option == 1:
            new_name = input("\nEnter the new name: ")
            contacts[new_indice]["name"] = new_name
        elif edit_option == 2:
            new_phone_number = int(input("\nEnter the new phone number: "))
            contacts[new_indice]["phone_number"] = new_phone_number
        elif edit_option == 3:
            new_email = input("\nEnter the new email: ")
            contacts[new_indice]["email"] = new_email
        print("\nContact edited successfully!")
        return
    else:
        print("\nInvalid contact!")
        return

def mark_unmark_favorite_contact(contacts, indice):
    new_indice = indice - 1
    if new_indice >= 0 or new_indice < len(contacts):
        if contacts[new_indice]["favorite"]:
            contacts[new_indice]["favorite"] = False
        else:
            contacts[new_indice]["favorite"] = True
        print("\nContact marked/unmarked as favorite successfully!")
    return

def see_favorites(contacts):
    print("\nFavorites:")
    for indice, contact in enumerate(contacts, start=1):
        if contact["favorite"]:
            print(f"{indice} - {contact['name']} - {contact['phone_number']} - {contact['email']}")
    return  

def delete_contact(contacts, indice):
    new_indice = indice - 1
    if new_indice >= 0 or new_indice < len(contacts):
        contacts.pop(new_indice)
        print("\nContact deleted successfully!")
    return      





# Main
contacts = []
while True:
    print("\nWelcome to Contact Manager!")
    print("1 - Add Contact")
    print("2 - List Contacts")
    print("3 - Edit Contact")
    print("4 - Mark/Unmark as Favorite")
    print("5 - See Favorites")
    print("6 - Delete Contact")
    print("7 - Exit")

    option = int(input("\nChoose an option: "))

    if option == 1:
        name = input("\nEnter the contact name: ")
        phone_number = int(input("Enter the contact phone number: "))
        email = input("Enter the contact email: ")
        add_contact(contacts, name, phone_number, email)
        print("\nContact added successfully!")
    elif option == 2:
        list_contacts(contacts)
    elif option == 3:
        list_contacts(contacts)
        indice = int(input("\nChoose the contact to edit: "))
        print("\nWhat information do you want to edit?")
        print("\n1 - Name\n2 - Phone Number\n3 - Email")
        edit_option = int(input("\nChoose an option: "))
        edit_contact(contacts, indice, edit_option)
    elif option == 4:
        list_contacts(contacts)
        indice = int(input("\nChoose the contact to mark/unmark as favorite: "))
        mark_unmark_favorite_contact(contacts, indice)
    elif option == 5:
        see_favorites(contacts)
    elif option == 6:
        list_contacts(contacts)
        indice = int(input("\nChoose the contact to delete: "))
        delete_contact(contacts, indice)
    elif option == 7:
        break
