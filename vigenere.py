msg = input("Enter the message you'd like to encrypt: ")
key = "lightningmcqueen"

def cipher(msg, key, mode=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = ' '
    key_index = 0
    #Iterate through user message
    for char in msg:
        #Accounting for spaces in the message
        if not msg.isAlpha():
            message += char
        else: 
            key_char = key[key_index % len(key)]
            key_index += 1
            shift = alphabet.index(key_char)
            index = alphabet.find(char)
            newIndex = (index + shift*mode) % len(alphabet)
            
            message += alphabet[newIndex]
            
    return message

def encrypt(msg, key):
    return cipher(msg, key)

def decrypt(msg, key):
    return cipher(msg,key, -1)

