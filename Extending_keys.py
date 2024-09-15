import re
from text_to_binary import text_to_binary

alpha_num = r"[^a-zA-Z0-9]"
message = input("Enter a Message: ")

while True:
    password = input("Enter a Password: ")

    if re.search(alpha_num, password):
        print("Invalid Password. Please only use alphanumeric characters (a-z, A-Z, 0-9).")
    else:
        print("Password accepted.")
        break  

def expand_to_key(password, message):
    binary_message = text_to_binary(message)
    binary_password = text_to_binary(password)

    while len(binary_password) < len(binary_message):
        binary_password = binary_password * 2

    if len(binary_password) > len(binary_message):
        binary_password = binary_password[0: len(binary_message)]
    
    return binary_password, binary_message

if __name__ == "__main__":
    binary_key, binary_message = expand_to_key(password, message)
    # if the message is 'a' (01100001), and the key is 'x' (01111000)
    print("Your key should be: 01111000, and is " + binary_key) 
    print("Testing that the length of the key matches the length of the binary form of the message: " + str((len(binary_message) == len(binary_key))))