# -*- coding: utf-8 -*-
"""python_quick_look.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IQynlewbtOqzsOgH2lyMabHPt0p9qmMi

even or odd
"""

number = int(input("Enter any number: "))
if(number%2==0):
  print("The number is even")
else:
  print("The number is odd")
input("press enter to exit")

"""Example Password"""

password="williams"
for i in range(3):
  pwd= input("enter the password: ")
  j=2
  if(pwd==password):
    print("welcome")
    break
  else:
    print("wrong password, chances left",j-i)
    continue
print("try next time")

"""Factorial"""

#for loop
fact =1
num = int(input("Enter any number: "))
for i in range(1,(num+1)):
  fact = fact*i
print("The factorial of",num,"is",fact)

#while loop
fact = 1
num = int(input("Enter any number: "))
i=1
while(i<=num):
  fact=fact*i
  i+=1
print("The factorial of",num,"is",fact)

"""Exponential Program"""

2**3

3**2

pow(2,3)

pow(3,2)

num = int(input("enter the number: "))
exp = int(input("enter the exponent: "))
result = 1
for i in range(1,(exp+1)):
  result *=num
print("The result is: ",result)

"""Delay Time Example"""

#example 1
import time
print("image1")
time.sleep(3)
print("image2")
time.sleep(3)
print("image3")

#example 2
import time
for a in range(1,11):
  print('\n')
  time.sleep(2)
  for b in range(1,11):
    print(a,"x",b,"=",a*b)

"""Small Assignment"""

for a in range(1,11):
  print('\n')
  input()
  for b in range(1,11):
    print(a,"x",b,"=",a*b)
