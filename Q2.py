#This is my code for Q2. It countd the number of trailing zeros in a factorial.
import math                           
num=int(input("enter an integer?"))   
fnum=math.factorial(num)        
print(fnum)
counter=0                             
k=10
while fnum % k == 0:            #If a number contains a trailing zero it should divide by 10 and give a remainder of zero. 
        counter = counter+1     #This while loop keeps a count of how many times the number can be divided by zero.
        k=k*10
        
print("Your factorial has " + str(counter) + " trailing zeros")

