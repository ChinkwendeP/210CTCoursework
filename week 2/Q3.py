#This is my code for Q3. It returns the highest perfect square which is
#less or equal to its parameter.

import math

a=float(input("enter an integer"))

if a==str:
      print("that is not an integer")
else:       
    b=a**2
    c=(int(a)**2)
    print( "the highest perfect square is " + str(c))

# I did this by simply converting any input into an int.
# This meant that by squaring it I would always recieve a perfect square.
