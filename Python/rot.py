import random
import math
import string



def main():
    encrypt_or_decrpty = input('do you want to encrypt or decrypt: ')
    user_word = input('what is your word: ')
    if encrypt_or_decrpty == encrypt:
        print(encrypt(user_word))
    else:
        print(decypt(user_word))



def encrypt(text):

    alphabet = string.ascii_lowercase
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'

    output = ''
    for char in text:
        index = alphabet.find(char)
        output += alphabet_rotated[index]
    return output

def decypt(text):
        alphabet         = 'nopqrstuvwxyzabcdefghijklm'
        alphabet_rotated = string.ascii_lowercase
        output = ''
        for char in text:
            index = alphabet.find(char)
            output += alphabet_rotated[index]
        return output
if __name__ == '__main__':
    main()
