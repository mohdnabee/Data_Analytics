import pyperclip 
import os 

FILE_NAME = "passwords.txt"

def save_password():
   website = input("Enter the website: ")
   pasword = input("Enter the password: ")
   with open(FILE_NAME, "a") as f:
       f.write(f"{website} <||> {pasword}\n")


def get_password():
     website = input("Enter the website: ")
     with open(FILE_NAME, "r") as f:
         for line in f: 
             if website in line: 
                 password = line.split("<||>")[1]
                 pyperclip.copy(password)
                 print(line)
                 break
         else:
             print("Password not found.")

def main():
    while True:
        print("Password Manager")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            save_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")


main()