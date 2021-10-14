def caesar_cipher(message, shift):
    """
    this caesar cipher function encrypts a string using a shift value, 
    substituting each letter with a letter found by moving n places down 
    the alphabet 
    Args:
        message(string): a phrase or sentence, can contain whitespaces & punctuation, assumed all lowercase
        shift(int): an int used to shift the message
    """
    translation = ""
    for letter in message:
        if letter.isalpha():
            unicode = ord(letter)
            translation += chr((unicode + shift - 97) % 26 + 97)
        else:
            translation+=letter
    return translation