from cryptography.fernet import Fernet
import base64
import getpass
import hashlib


def get_key_from_password(master_password):
    digest = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

master_pwd = getpass.getpass("Enter master password: ")
key = get_key_from_password(master_pwd)
fer = Fernet(key)



'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key




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

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

 

while True:
    mode = input("Would you like to add a a new password or view exsisting ones (view and add), press q to quit? ").lower()
    if mode == "q":
        break;
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
