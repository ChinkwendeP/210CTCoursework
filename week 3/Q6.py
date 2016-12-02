#This is my code for Q6. It takes a sentence and outputs the reverse.
sentence=input("enter your sentence...")
sentence= sentence.lower()
if len(sentence) >0:
    print(sentence)
else:
    print ("empty")

reversed_sentence=sentence.split()                   #The split function stores each word in a list
reversed_sentence=reversed_sentence[::-1]       
n=reversed_sentence
n=" ".join(reversed_sentence)
print(n)





    
