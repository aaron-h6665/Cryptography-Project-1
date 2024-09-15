import random

def encode_message(num):    
    # Convert integer to a Unicode character
    unicode_char = chr(num)
    
    # Create a dynamic message with the Unicode character using an f-string
    message = f"The Unicode character for {num} is: {unicode_char}"
    
    # Encode the formatted string to UTF-8
    utf8_encoded_message = message.encode('utf-8')
    
    return message, utf8_encoded_message

num = random.randint(0, 1111000)

message, utf8_encoded_message = encode_message(num)
print(message)  
print(utf8_encoded_message)  
