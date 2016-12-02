#This is my code for question 10. Given a sequence of numbers it returns
#the sub-sequence of maximum length which is in ascending order.

#Add the first number in the array to a. Then run a while loop that checks if the next item in the array is larger than the previous number, if it is, add it to a. if not check if it is larger than the number
#in b and add it to b. if the number is smaller that the numbers in both a and b then it should replace the shortest list and start again.

def sub_sequence(array):
    
  sub_sequence= [34,7,8,12,20,29,78,5,25,88,2,3]
  print(sub_sequence)
  a = []
  b = []

  for x in range( len(array) ):

    if x < len(array) - 1 and array[x] <= array[x+1]:   
      b.append(array[x])
      

    else:                           
      b.append(array[x])   
      

      if len(b) > len(a):
        

        a = b

      b = []

  
  print (a)
 
print(sub_sequence([34,7,8,12,20,29,78,5,25,88,2,3]))



