#This is Q4 of the 210CT Coursework.
#I am describing the run-time bouds of my
#algorithms from Q1 and Q2 using Big 0 Notation.

#Q1)
from random import *                   #(1)   
array=[5,3,8,6,1,9,2,7]                #(1)
print (array)                          #(1)


for x in range(0, len(array), 1):      #(n)  
   randa= randint(0, len(array)-1)     #(n)
   remove= array.pop(randa)            #(n) 
   array.append(remove)                #(n)  
print(array)                           #(1)

#(4n+4)
#Complexity- O(n)

#Q2)
import math                            #(1)
num=int(input("enter an integer?"))    #(1)
fnum=math.factorial(num)               #(1)
print(fnum)                            #(1)
counter=0                              #(1)
k=10                                   #(1)

while fnum % k == 0:                   #(n)
        counter = counter+1            #(n)
        k=k*10                         #(n) 
                                                             
print("your factorial has " + str(counter) + " trailing zeros")       #(1)

#(4n+7)
#Complexity - O(n)
