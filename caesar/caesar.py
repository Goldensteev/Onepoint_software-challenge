#!/usr/bin/env python
# -*- coding: utf-8 -*-

def caesar_cipher(message, shift):
    """
    this caesar cipher function encrypts a string using a shift value, 
    substituting each letter with a letter found by moving n places down 
    the alphabet 
    Args:
        message(str): a phrase or sentence, can contain whitespaces & punctuation, assumed all lowercase
        shift(int): an int used to shift the message
    Returns:
        translation(str): the message after the substitution cipher
    """
    translation = ""
    for letter in message:
        if letter.isalpha():
            unicode = ord(letter)
            translation += chr((unicode + shift - 97) % 26 + 97)
        else:
            translation+=letter
    return translation

if __name__ == '__main__':
    print(caesar_cipher("this is a test!!! it works!? zoinks", 1))
