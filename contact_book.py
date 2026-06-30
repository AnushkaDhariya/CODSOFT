contact_book = {}

while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact_book[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added Successfully!")

    elif choice == "2":
        if len(contact_book) ==0:
            print("No Contacts Available!")
        else:
            print("\n----- CONTACT LIST -----")
            for name, details in contact_book.items():
                print(f"\nName  : {name}")
                print(f"Phone   : {details['Phone']}")
                print(f"Email   : {details['Email']}")
                print(f"Address : {details['Address']}")

    elif choice == "3":
        search = input("Enter Name: ")

        if search in contact_book:
            print("\nContact Found!")
            print(contact_book[search])
        else:
            print("Contact Not Found!")

    elif choice == "4":
        update = input("Enter Name to Update: ")

        if update in contact_book:
            contact_book[update]["Phone"] = input("New Phone: ")
            contact_book[update]["Email"] = input("New Email: ")
            contact_book[update]["Address"] = input("New Address: ")
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        delete = input("Enter Name to Delete: ")

        if delete in contact_book:
            del contact_book[delete]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "6":
        print("Total Contacts:", len(contact_book))

    elif choice == "7":
        print("Thank You for using Contact Book")
        break

    else:
        print("Invalid Choice!Please Try Again.")