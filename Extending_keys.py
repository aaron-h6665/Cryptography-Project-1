from text_to_binary import text_to_binary

message = "jofdasjopfjsdapof"

def get_password():
    while True:
        password = input("Enter an alphanumeric string: ")
        
        #check if the password only containers alphanumeric components and is not null
        if password.isalnum() or len(password) != 0:
            return password
        else:
            print("Invalid password. Please enter a password with only 0-9, a-z, A-Z.")

def expand_to_key(password, message):
    binary_message = text_to_binary(message)
    key = text_to_binary(password)

    while len(key) < len(binary_message):
        key = key * 2

    if len(key) > len(binary_message):
        key = key[0: len(binary_message)]
    
    return key, binary_message

if __name__ == "__main__":
    key, binary_message = expand_to_key(get_password(), message)
    # if the message is 'a' (01100001), and the key is 'x' (01111000)
    print(key) 
    print("Testing that the length of the key matches the length of the binary form of the message: " + str((len(binary_message) == len(key))))



"""
alpha_num = r"[^a-zA-Z0-9]"
message = input("Enter a Message: ")

while True:
    password = input("Enter a Password: ")

    if re.search(alpha_num, password):
        print("Invalid Password. Please only use alphanumeric characters (a-z, A-Z, 0-9).")
    else:
        print("Password accepted.")
        break  
"""