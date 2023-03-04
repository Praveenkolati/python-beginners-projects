text = input('Enter your text: ')
s = int(input('Enter the shift value: '))


def encrypt(text, s):
    """
    This function takes a string and a shift value and returns a string that is the original string
    shifted by the shift value.

    :param text: the text to be encrypted
    :param s: the shift value
    """
    result = ''
# Looping through the length of the text.
    for i in range(len(text)):
        # Taking the character at the index of i and assigning it to the variable char.
        char = text[i]
# Checking if the character is uppercase and if it is, it adds it to the result.
        if (char.isupper()):
            result += chr((ord(char)+s-65) % 26+65)
# Checking if the character is a space and if it is, it adds it to the result.
        elif char == " ":
            result += char
# Taking the character and adding the shift value to it.
        else:
            result += chr((ord(char)+s-97) % 26+97)
    return result


print('Cipher: ', encrypt(text, s))
