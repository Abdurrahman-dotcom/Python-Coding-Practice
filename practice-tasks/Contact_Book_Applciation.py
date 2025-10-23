def display_menu():
    print('Contact Book Menu:')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Edit Contact')
    print('4. Delete Contact')
    print('5. List All Contacts')
    print('6. Exit')

def add_contact(contact_book):
    # Ask for the name
    name = input()

    # Check if contact exists
    if name in contact_book:
        print("Contact already exists!")
    else:
        # Get the other details
        phone = input()
        email = input()
        address = input()

        # Add to dictionary
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        print("Contact added successfully!")

def view_contact(contact_book):

    name = input()
    if name in contact_book:
        print(f'Name: {name}')
        print(f'Phone: {contact_book[name]["phone"]}')
        print(f'Email: {contact_book[name]["email"]}')
        print(f'Address: {contact_book[name]["address"]}')
    else:
        print('Contact not found!')

def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        phone = input()
        if phone:
             contact_book[name]['phone'] = phone
        email = input()
        if email:
            contact_book[name]['email'] = email
        address = input()
        if address:
            contact_book[name]['address'] = address
        print('Contact updated successfully!')
    else:
        print('Contact not found!')

def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        contact_book.pop(name)
        print('Contact deleted successfully!')
    else:
        print('Contact not found!')
        
def list_all_contacts(contact_book):
    if not contact_book:
        print('No contacts available.')
    else:
        for names in contact_book:
            print(f'Name: {names}')
            print(f'Phone: {contact_book[names]["phone"]}')
            print(f'Email: {contact_book[names]["email"]}')
            print(f'Address: {contact_book[names]["address"]}')
            print('')

contact_book={}
while True:
    display_menu()    
    index = int(input())    
    if index == 1:
        add_contact(contact_book)
    elif index == 2:
        view_contact(contact_book)
    elif index == 3:
        edit_contact(contact_book)
    elif index == 4:
        delete_contact(contact_book)
    elif index == 5: 
        list_all_contacts(contact_book)
    else:
        break       

