#This script encrypts and decrypts files using the Fernet symmetric encryption method from the cryptography library.
#It requires the cryptography library to be installed. You can install it using pip:    pip install cryptography
#This script uses an object oriented approach to encrypt and decrypt files.
# The script requires the action to be performed, name of the file to perform operation and key file that contains the key
from cryptography.fernet import Fernet
import argparse

class FileCryptor:
    # Initialize the FileCryptor with the key file path and the key file
    def __init__(self, file_name, key_file):
        self.file_name = file_name
        self.key_file = key_file
    # Method loads the key fron the key file
    def load_key(key_file):
        with open(key_file, "rb"):
            return key_file.read()

    # Method to encrypt the file using the key
    def encrypt_file(self, file_name,key_file):
        key = open(key_file, "rb").read()
        f = Fernet(key)
        with open(file_name, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(file_name, "wb") as file:
            file.write(encrypted_data)
    # Method to decrypt the file using the key
    def decrypt_file(self, file_name,key_file):
        key = open(key_file, "rb").read()
        f = Fernet(key)
        with open(file_name, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(file_name, "wb") as file:
            file.write(decrypted_data)
    # Method to generate a new key and save it to the key file
    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)

if __name__ == "__main__":
    # Using argparse to handle arguments which includes what type of action to be performed and the file that needs to be encrypted or decrypted.
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files using Fernet symmetric encryption.")
    parser.add_argument("option", choices=["encrypt", "decrypt"], help="Action to perform: encrypt or decrypt")
    parser.add_argument("file", help="File to encrypt or decrypt")
    parser.add_argument("--key", help="Key file for encryption/decryption", default="key-file.key")

    args = parser.parse_args()

    option = args.option
    file_name = args.file
    key_file = args.key
    #Created fileCrypt object to perform the operations
    fileCrypt = FileCryptor(file_name,key_file)
    if option == "encrypt":
        fileCrypt.generate_key()
        fileCrypt.encrypt_file(file_name,key_file)
        print(f"File '{file_name}' encrypted successfully.")
    elif option == "decrypt":
        fileCrypt.decrypt_file(file_name,key_file)
        print(f"File '{file_name}' decrypted successfully.")
    else:
        print("Invalid option. Use 'encrypt' or 'decrypt'.")
        exit(1)  # Exit with an error code

