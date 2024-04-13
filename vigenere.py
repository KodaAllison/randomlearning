msg = input("Enter your message: ")
choice = input("Are you encrytping or decrypting this message?")
key = "lightningmcqueen"

def cipher(msg, key, mode=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = ' '
    key_index = 0
    #Iterate through user message
    for char in msg:
        #Accounting for spaces in the message
        if not char.isalpha():
            message += char
        else: 
            key_char = key[key_index % len(key)]
            key_index += 1
            shift = alphabet.index(key_char)
            index = alphabet.find(char)
            newIndex = (index + shift*mode) % len(alphabet)
            
            message += alphabet[newIndex]
            
    return message


def encryption(msg, key):
    return cipher(msg, key)


def decryption(msg, key):
    return cipher(msg,key, -1)

if choice.lower() in ("d", "decrypt", "decrypting", "decryption"):
    decrypt = decryption(msg,key)
    print(f'Decrypted message:',decrypt)  
elif choice.lower() in ("e", "encrypt", "encrypting", "encryption"):
    encrypt = encryption(msg,key)
    print(f'Encrypted message:',encrypt)
    print(f'key: ',key)
