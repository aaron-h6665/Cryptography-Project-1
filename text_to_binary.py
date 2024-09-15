def text_to_binary(text):
    return text.encode("utf-8")

def binary_to_text(text):
    return text.decode("utf-8")

if __name__ == "__main__":
    print(text_to_binary("catch"))
    print(binary_to_text(text_to_binary("catch")))


"""
def text_to_binary(text):
    for chr in text:
        chr = chr.encode("utf-8")
        binary_format = ':'.join(f'{byte:08b}' for byte in chr)
        list_chrs.append(binary_format)
        print(binary_format, end = ' ')
"""
"""
def text_to_binary(text):
    binary_string = ""
    for chr in text:
        chr = chr.encode("utf-8")
        binary_format = ''.join(f'{byte:08b}' for byte in chr)
        list_chrs.append(binary_format)
        binary_string += binary_format
        #print(binary_format, end = '')
    return binary_string

new_list = []
def binary_to_text(list_chrs):
    for chr in list_chrs:
        chrs = []
        temp = chr.split(":")
        for bit in temp:
            f = int(bit, 2)
            chrs.append(f)
        chrs = bytes(chrs)
        new_list.append(chrs)

    for chr in new_list:
        print(chr.decode('utf-8'), end = '')

if __name__ == "__main__":
    print(text_to_binary("catch"))
    binary_to_text(list_chrs)

#text = "你好，世界"
"""

"""
def text_to_binary(text):
    for chr in text:
        chr = chr.encode("utf-8")
        binary_format = ':'.join(f'{byte:08b}' for byte in chr)
        print(binary_format, end = ' ')
    return binary_format
"""

