# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:55:28 2020

@author: Silverxenfx
"""
import random
import string
alpha=[chr(i) for i in range(97,123)]
monoalpha=[]

def init():
    for i in range(26):
        x=random.choice(string.ascii_letters)
        if(x not in monoalpha):
            monoalpha.append(x)
        else:
            y=random.choice(string.ascii_letters)
            monoalpha.append(y)
def main():
    choice=int(input("1. Encrypt\n2.Decrypt\nEnter choice: "))
    if(choice==1):
        plaintext=input("Enter Plain Text")
        encrypted=encrypt(plaintext)
        print("-------Output-------")
        print("Plain Text {}\nCipher {}".format(plaintext,encrypted))
        
         
    elif(choice==2):
        cipher=input("Enter Cipher Text")
        decrypted=decrypt(cipher)
        print("-------Output-------")
        print("Cipher {}\nPlain text {}".format(cipher,decrypted))
         
    else:
        return 
def encrypt(plaintext):
    plaintext=str(plaintext)
    encrypted=""
    for i in plaintext:
        encrypted+=monoalpha[alpha.index(i)]
    return encrypted
def decrypt(cipher):
    cipher=str(cipher)
    decrypted=""
    for i in cipher:
        decrypted+=alpha[monoalpha.index(i)]
    return decrypted

        
if __name__ == "__main__":
    init()
    main()       
