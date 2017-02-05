def alphabet_position(letter):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    return alphabet.index(letter.lower())

def rotate_character(char, rot):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    if char.isalpha() == False:
        return char
    x = (alphabet_position(char) + rot) % 26
    new_char = alphabet[x]
    if char == char.upper():
        new_char = new_char.upper()
    return new_char

def encrypt(text, rot):
    new_text = ""
    for x in text:
        x = rotate_character(x, rot)
        new_text = new_text + x
    return new_text
