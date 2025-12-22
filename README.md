# Password-Manager
This Python program is a password manager that securely stores and retrieves account passwords using Fernet encryption. A master password is hashed with SHA-256 to generate an encryption key. Passwords are encrypted before being saved to a file and can only be decrypted with the correct master password.


How to run
  1. Clone the repository:
  - "git clone https://github.com/yourusername/password-manager.git"
  - "cd password-manager"
    
  2. Install Dependencies:
  - "pip install cryptography"
    
  3. Run:
  - "python main.py"
     
**Technologies Used**
  - Python 3
  - cryptography
     (Fernet)
  - hashlib 
  - base64
  - getpass

  
