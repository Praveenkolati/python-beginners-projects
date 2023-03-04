text = input('Enter your text: ')
s = int(input('Enter your shift value: '))


def decrypt(text, s):
    """
    It takes a string and shifts each character by the value of s
    
    :param text: the text to be decrypted
    :param s: The string to be encrypted
    """
    result = ''
# Looping through the text and assigning each character to the variable char.
    for i in range(len(text)):
        char = text[i]
# Checking if the character is uppercase and then shifting it by the value of s.
        if (char.isupper()):
            result += chr((ord(char)-s-65) % 26+65)
# Checking if the character is a space and then adding it to the result.
        elif char == ' ':
            result += char
# Checking if the character is lowercase and then shifting it by the value of s.
        else:
            result += chr((ord(char)-s-97) % 26+97)
    return result


print('Cipher: ', decrypt(text, s))
