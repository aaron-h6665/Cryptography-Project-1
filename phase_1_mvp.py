import base64

def get_password():
    while True:
        password = input("Enter an alphanumeric string: ")
        
        #check if the password only containers alphanumeric components and is not null
        if password.isalnum() or len(password) != 0:
            return password
        else:
            print("Invalid password. Please enter a password with only 0-9, a-z, A-Z.")

def get_filename():
    #user-inputs the desired file
    filename = input("What is the name of the file? ")
    return filename

def get_message():
    while True:
        try:
            filename = get_filename()

            #to be able to read all unicode characters
            with open(f'{filename}', 'r', encoding='utf-8') as file:
                message = file.read()

            return message, filename
        #in case they misstyped
        except FileNotFoundError:
            print("File not found. Please enter a valid filename.")

message, stored_filename = get_message()
password = get_password()

def text_to_binary(text):
    return text.encode("utf-8")

def binary_to_text(text):
    return text.decode("utf-8")

def one_time_pad(message, password):
    #convert the alphanumeric password into binary
    password = text_to_binary(password)

    #make the password the same length as the binary message
    while len(password) < len(message):
        password = password * 2

    if len(password) > len(message):
        key = password[0: len(message)]

    #XOR each byte one by one, using the zip function which makes lists
    encrypted_message = bytes(byte_a ^ byte_b for byte_a, byte_b in zip(message, key))

    return encrypted_message

def encrypt(message, password):
    binary_message = text_to_binary(message)
    encrypted_message = one_time_pad(binary_message, password)

    #convert the encrypted message to base64
    encrypted_message_base64 = base64.b64encode(encrypted_message)

    #save the file as a binary file so that we don't run into any problems
    with open('encrypted_message.txt', 'wb') as file:
        file.write(encrypted_message_base64)

    return encrypted_message, encrypted_message_base64


def decrypt(password):
    with open('encrypted_message.txt', 'rb') as file:
        encrypted_message_base64 = file.read()
        encrypted_message = base64.b64decode(encrypted_message_base64)

        decrypt_message_binary = one_time_pad(encrypted_message, password)
        decrypted_message = binary_to_text(decrypt_message_binary)

    return decrypted_message

encrypt(message, password)
print(decrypt(password))


"""
temp_byte_list = []
    temp_chr_list = binary_message_formatted.split(' ')
    temp_chr_list.pop()
    for chr in temp_chr_list:
        byte = chr.split(':')
        temp_byte_list.append(byte)

    binary_key = binary_key_formatted.replace(":", "")
    binary_key = binary_key.replace(" ", "")
    binary_message = binary_message_formatted.replace(":", "")
    binary_message = binary_message.replace(" ", "") 
"""

"""
    print(decrypted_message_binary)
    print(temp_byte_list)

    i = 0 
    for chr in temp_byte_list:
        for _ in range(len(chr) - 1):
            decrypted_message_binary = decrypted_message_binary[0: 9*i+8] + ":" + decrypted_message_binary[9*i+8:]
            i += 1
        decrypted_message_binary = decrypted_message_binary[0: 9*i+8] + " " + decrypted_message_binary[9*i+8: ]
        i += 1
    
    print(decrypted_message_binary)
    
    new_list = []

    for chr in list_chrs:
        chrs = []
        temp = chr.split(":")
        for bit in temp:
            f = int(bit, 2)
            chrs.append(f)
        chrs = bytes(chrs)
        new_list.append(chrs)
"""

"""
    encrypted_message = int(binary_message, 2) ^ int(binary_key, 2)
    encrypted_message = bin(encrypted_message)[2:].zfill(len(binary_key))
"""

"""
    i, j = 0, 0
    for chr in temp_byte_list:
        for byte in range(len(chr) - 1):
            encrypted_message = encrypted_message[0: 9*i+8] + ":" + encrypted_message[9*i+8:]
            i += 1
        encrypted_message = encrypted_message[0: 9*i+8] + " " + encrypted_message[9*i+8: ]
        i += 1
"""

"""
    for chr in text:
        chr = chr.encode("utf-8")
        binary_format = ':'.join(f'{byte:08b}' for byte in chr)
        #list_chrs.append(binary_format)
        binary_string += binary_format
        binary_string += " "
        #print(binary_format, end = '')
    return binary_string
    """
