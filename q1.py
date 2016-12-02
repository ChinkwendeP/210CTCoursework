#This is my code for Q1. It randomly shuffles an array of integers

from random import *               
array=[5,3,8,6,1,9,2,7]
print (array)


for x in range(0, len(array), 1):        
   randa= randint(0, len(array)-1)      #rand int returns a random integer in the list
   remove= array.pop(randa)             #removes the integer that has just been generated
   array.append(remove)                 #This adds the integer back into the array 
print(array)


#rational behind my implementaion- My code works by removing an integer and adding it back to the array one at a time.
#my function does this the number of times(the size of the array) e.g if the array is 6 integers long my for loop
#will run 6 times which ensures any sized array is shuffled adequately.


