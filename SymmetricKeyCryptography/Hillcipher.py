# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:29:52 2020

@author: Silverxenfx

Note it 3x3 Hill CIPHER Enter Value Accordingly
"""
import math
alpha=[chr(i) for i in range(97,123)]

key=input("Enter Key: ").lower()
plaintext=input("Enter Plain Text: ").replace(" ","").lower()
key_matrix=[]
plaintext_matrix=[]
pointer=0
len_plain=len(plaintext)
row_=column_=int(math.sqrt(len(key)))
if(len_plain%3!=0):
  for i in range(1,len_plain+1):
    if((len_plain+i)%3==0):
      plaintext=plaintext+(i*("x"))
      break




for i in range(row_):
  temp=list()                                             #Key Matrix
  for j in range(column_):
    temp.append(key[pointer])
    pointer+=1
  key_matrix.append(temp)

pointer=0
asd=len(plaintext)//row_
for i in range(asd):
  temp=list()                                             #plaintext Matrix
  for j in range(column_):
    temp.append(plaintext[pointer])
    pointer+=1
  plaintext_matrix.append(temp)

"""while(pointer<len(plaintext)):
  plaintext_matrix.append([plaintext[pointer],plaintext[pointer+1],plaintext[pointer+2]])
  pointer+=3
"""
pointer=-1
cipher_matrix=[]


for i in range(len(plaintext_matrix)):
  temp=[]
  for j in range(len(key_matrix)):
    sum_=0
    for k in range(len(key_matrix[j])):
      sum_+=alpha.index(key_matrix[j][k])*alpha.index(plaintext_matrix[i][k])
    temp.append(sum_%26)
  cipher_matrix.append(temp)

cipher=""
for i in range(len(cipher_matrix)):
  for j in range(len(cipher_matrix[i])):
    cipher+=alpha[cipher_matrix[i][j]]

print("CIPHER: ",cipher)
print(key_matrix)
"""------------------------------------------Decryption-----------------------------"""
for i in range(row_):
  for j in range(column_):                      #convertion key_matrix alphabets -> key_matrix integers
    key_matrix[i][j]=alpha.index(key_matrix[i][j])

print(key_matrix)
matrix=key_matrix
temp=[]
k=0
while(k<3):
  temp_=[matrix[0][k]]
  for i in range(1,3):#Rows

    for j in range(0,3):#cols
     if(k!=j):
       temp_.append(matrix[i][j])
  k+=1
  temp.append(temp_)


det=[]

for i in range(3):
  mul_=list()
  for j in range(1,3):
    k=1
    if(j%2==0):
      k=-1
    mul_.append(k*temp[i][j]*temp[i][4-(j-1)])
    #print(mul_)
  #print(sum(mul_))
  det.append((temp[i][0])*(sum(mul_)))
Determinant=0
for i in range(len(det)):
  k=1
  if(i%2!=0):
    k=-1
  Determinant+=k*det[i]
print(Determinant)

#--------------------------------------------------------------------
minor=[[],[],[]]
row=0
col=0
while(row<3 and col<3):
  temp=[]
  for i in range(3):
    if(row!=i):
      for j in range(3):
        if(col!=j):
          temp.append(matrix[i][j])
  minor[row].append((temp[0]*temp[3])-(temp[1]*temp[2]))
  if(col==2):
    col=0
    row+=1
  else:
    col+=1


for i in range(3):
  for j in range(3):
    minor[i][j]=((-1)**((i+1)+(j+1)))*minor[i][j]



for i in range(3):
  for j in range(3):
    print(minor[i][j],end=" ")
  print("")

print("  \n")

inverse=[]
for i in range(3):
  temp=[]
  for j in range(3):
    temp.append(minor[j][i])
  inverse.append(temp)

print(inverse)

if(Determinant<0):
  Determinant=26-Determinant

Determinant_=Determinant
for i in range(Determinant):
  if((i*Determinant)%26==1):
    Determinant_=i
    break
if(Determinant_!=Determinant):


      for i in range(3):
        for j in range(3):
          if(inverse[i][j]<0):
            inverse[i][j]=26+inverse[i][j]
          inverse[i][j]=(inverse[i][j]*Determinant)%26



      print(inverse)
      decrypt=""
      for i in range(len(cipher_matrix)):
        temp=[]
        for j in range(len(inverse)):
          sum_=0
          for k in range(len(inverse[j])):
            sum_+=(inverse[j][k])*(cipher_matrix[i][k])
          decrypt+=alpha[sum_%26]

      print("DECRYPTED: ",decrypt)
else:
  print("Multiplicative Inverse of Determinant not Possible")
