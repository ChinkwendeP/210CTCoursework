#This is my code for Q7

x = input("enter a number:")
def is_prime_number(x):     #My function checks to see if the number is divisible by any 
    if x >= 2:              #numbers between 2 and itself. If it is then it is not a prime.
        for y in range(2,x):
            if not ( x % y ):
                return True
    else:
	        return False   #divisible therefore not prime
print(str(x) + " is a prime number")

