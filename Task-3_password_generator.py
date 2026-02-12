import random
import string
def generate_password():
    print("PASSWORD GENERATOR")
    length=int(input("Enter desired password length: "))

    print("Select password complexity:")
    print("1. Only Letter")
    print("2. Letter+Numbers")
    print("1. Letter+Numbers+Symbols")

    choice=input("Enter choice(1/2/3): ")
    letters= string.ascii_letters
    numbers= string.digits
    symbols= string.punctuation

    if choice=="1":
        characters= letters
    elif choice=="2":
        characters= letters+numbers
    elif choice=="2":
        characters= letters+numbers+symbols
    else:
        print("Invalid choice. Using default: Letters+Numbers")
        characters = letters+numbers
    password= ''.join(random.choice(characters) for _ in range(length))
    print("/n Generated Password: ",password)
if __name__=="__main__":
    generate_password()
