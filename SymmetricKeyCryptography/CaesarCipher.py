# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:17:11 2020

@author: Silverxenfx
"""
alpha=[chr(i) for i in range(97,123)]
def main():
    
    choice=int(input("1. Encrypt\n2.Decrypt\nEnter choice: "))
    if(choice==1):
        plaintext=input("Enter Plain Text")
        key=int(input("Enter Key value"))
        key=key%26
        encrypted=encrypt(plaintext,key)
        print("-------Output-------")
        print("Plain Text {}\nCipher {}".format(plaintext,encrypted))
        
    else:
        cipher=input("Enter Cipher Text")
        key=int(input("Enter Key value"))
        key=key%26
        decrypted=decrypt(cipher,key)
        print("-------Output-------")
        print("Cipher {}\nPlain text {}".format(cipher,decrypted))

def encrypt(plaintext,key):
    plaintext=str(plaintext)
    key=int(key)
    encrypted=""
    for i in plaintext:
        pointer=alpha.index(i)
        pointer=(pointer+key)%26
        encrypted+=alpha[pointer]
    return encrypted
def decrypt(cipher,key):
    
    cipher=str(cipher)
    key=int(key)
    decrypted=""
    
    for i in cipher:
        pointer=alpha.index(i)
        pointer=(pointer-key)
        if(pointer<0):
            decrypted+=alpha[26+pointer]
        else:
            decrypted+=alpha[pointer]
    
    return decrypted        

    
              
    
main()    
    