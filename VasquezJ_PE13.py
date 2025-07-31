# script that allows users to store, retrieve, and display contacts

contact = {}  # Dictionary to store names and phone numbers
def enter_name():

    while True:
        print('\nDo you want to add a New contact, Search an existing contact, or Display all contacts?')
        print('Type New, Search, or Display: ', end='')
        choice = input().lower()

        if choice == 'new':
            print('\nADDING CONTACTS')
            name = input('Enter contact name: ')
            phone = input('Enter phone number: ')
            print(add_contacts(contact, name, phone))

        elif choice == 'search':
            print('\nSEARCHING FOR A CONTACT')
            name = input('Enter name to search: ')
            print(search_contact(contact, name))

        elif choice == 'display':
            print('\nDISPLAYING ALL CONTACTS:')
            print('Contact List:')
            for key, value in contact.items():
                print(f'{key} - {value}')
        else:  # handles mistyped input
            print('**Your choices are New, Search, or Display***')

def add_contacts(contact, name, phone): # function handles adding new contacts
    if name in contact:
        return "Name already in contact list.\n"
    else:
        contact[name] = phone
        return "Contact saved!\n"

def search_contact(contact, name):  # function handles searching exisiting contacts
    if name in contact:
        return f"Phone number: {contact[name]}\n"
    else:
        return "Login failed: Invalid credentials."

if __name__ == "__main__":  # statement defines the function that
    enter_name()            # begins when the script opens, begins at def enter_name

