#!/usr/bin/env python

maxKey = 26

def decryptMessage(key, ciphertext):
    plaintext = ''

    for symbol in ciphertext[0]:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                if num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                if num < ord('a'):
                    num += 26

            plaintext += chr(num)
        else:
            plaintext += symbol

    return plaintext

print('### Caesar Cipher Cracker ###')

key = raw_input('Input key (or input b for brute-force): ')

fromFile = raw_input('Ciphertext from file (y/n): ')

if fromFile == 'y':
    fileName = raw_input('Input file name: ')
    ciphertextFile = open(fileName)
    ciphertext = ciphertextFile.readlines()
    ciphertext = [''.join(ciphertext)]
else:
    ciphertextInput = raw_input('Input ciphertext: ')
    ciphertext = [ciphertextInput]
    

if key == 'b':
    for key in range(maxKey):
        plaintext = decryptMessage(-(key + 1), ciphertext)
        print('Key %s\t: %s' %(key + 1, plaintext))
else:
    key = int(key)
    plaintext = decryptMessage(-key, ciphertext)
    print('Key %s\t: %s' %(key,plaintext))
    
