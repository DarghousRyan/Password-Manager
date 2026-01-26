from cryptography.fernet import Fernet
import base64
import getpass
import hashlib

#Turns the Master Password into the key that locks and unlocks all stored passwords.
def get_key_from_password(master_password):
    digest = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

master_pwd = getpass.getpass("Enter master password: ") # Prompts the user for the master passwords and .getpass allows for the entry to be hidden as its typed. 
key = get_key_from_password(master_pwd)
fer = Fernet(key)

# One of three modes; Allows user to view passwords
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                user, encrypted = line.rstrip().split("|")
                print("User:", user, "| Password:", fer.decrypt(encrypted.encode()).decode())
    except FileNotFoundError:
        print("No passwords saved yet")
    except Exception:
        print("Wrong master password or corrupted data")

#One of three modes; Allows the user to add an Account Name & Password
def add():
    name = input("Account name: ")
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                user, pwd = line.rstrip().split("|")
                if user == name:
                    print(f"{name} has already been used, please try again")
                    return
    except FileNotFoundError:
        pass

    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

# One of three modes; Allows the user to remove an account by the correct Account Name and Password. 
def remove():
    name = input("Account name to remove: ")
    count = 0
    verify_pwd = getpass.getpass("Confirm password: ")

    found = False
    updated_lines = []
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                user, encrypted = line.rstrip().split("|")
                decrypted_pwd = fer.decrypt(encrypted.encode()).decode()

                if user == name and decrypted_pwd == verify_pwd:
                    found = True
                    continue
                else:
                    updated_lines.append(line)

        if not found:
            print("Account not found or password incorrect")
            return
            

        with open("passwords.txt", "w") as f:
            f.writelines(updated_lines)

        print(f"Account '{name}' removed successfully!")
        
    except FileNotFoundError:
        print("No passwords saved yet")
    except Exception:
        print("Wrong master password or corrupted data.")

#Where the user interacts
def main(): 
    while True:
        mode = input("Would you like to add, view, or remove passwords? (view / add / remove). Press q to quit? ").lower()
        if mode == "q":
            break;
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == "remove":
            remove()
        else:
            print("Invalid mode")
            continue

#Runs main()
if __name__ == "__main__":
    main()

