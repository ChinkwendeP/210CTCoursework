#This is my code for Q8. It removes vowels from a sentence.

Vowels=('a', 'e', 'i', 'o', 'u')          #define the vowels in a list
s=input("enter a sentence...")
s=s.lower()                               #allows my to only define my vowels in lowercase

new_sentence=""
for letter in s:
    if letter not in Vowels:              #My for loop checks through each letter and only prints 
         new_sentence+= letter            #it if it is not a vowel
    print(new_sentence)


    
    
