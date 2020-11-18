import pickle

with open('phonebook1.pickle', 'rb') as fh:
    phoneBook = pickle.load(fh)

print("\nElectronic Phone Book\n=====================\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit\n")

# phoneBook = {}

def entry_lookup(name):
    if name in phoneBook.keys():
        entry_name = name
        entry_number = phoneBook.get(name)
        info = [entry_name, entry_number]
        msg = (f"Found entry for {info[0]}: {info[1]}\n")
        return msg
    else:
        msg = (f"\n{name} does not exist. Press 2 to set an entry.\n")
        return msg

def add_entry(name, number):
    phoneBook[name] = number
    msg = (f"Entry stored for {name}.\n")
    return msg

def delete_entry(name):
    if name in phoneBook.keys():
        del phoneBook[name]
        msg = (f"Deleted entry for {name}.\n")
        return msg
    else:
        msg = (f"{name} does not exist in phonebook.\n")
        return msg

def list_all():
    msg = ""
    for name in phoneBook:
        msg += (f"\nFound entry for {name}: {phoneBook[name]}\n")
    return msg

def done():
    with open('phonebook1.pickle', 'wb') as fx:
        pickle.dump(phoneBook, fx)
    msg = "\nBye.\n"
    return msg

while True:
    choice = int(input('What do you want to do (1-5)? '))
    if choice == 1:
        name = input("Name:  ") 
        print(entry_lookup(name))
    
    elif choice == 2:
        name = input("Name: ")
        number = input("Phone Number: ")
        print(add_entry(name, number))

    elif choice == 3:
        name = input("Name: ")
        print(delete_entry(name))

    elif choice == 4:
        print(list_all())
    
    elif choice == 5:
        print(done())
        with open('phonebook1.pickle', 'wb') as fx:
            pickle.dump(phoneBook, fx)
        break
    
    else:
        print("That is not a valid option!")






