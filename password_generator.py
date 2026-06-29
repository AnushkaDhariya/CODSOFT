import random
import string

print("========== PASSWORD GENERATOR ==========")

while True:

    length = int(input("Enter password length: "))

    characters = ""

    letters = input("Include Letters? (yes/no): ").lower()
    numbers = input("Include Numbers? (yes/no): ").lower()
    symbols = input("Include Symbols? (yes/no): ").lower()

    if letters == "yes":
        characters += string.ascii_letters

    if numbers == "yes":
        characters += string.digits

    if symbols == "yes":
        characters += string.punctuation

    if characters == "":
        print("Please select at least one option!")
        continue

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    if length >= 12:
        print("Password Strength: Strong")
    elif length >= 8:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Weak")

    choice = input("\nGenerate another password? (yes/no): ").lower()

    if choice != "yes":
        print("Thank You for using Password Generator!")
        break