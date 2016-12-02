#This is my code for Q9.Its an adaptation of the binary search algorithm which
#highlights wheather a number is in a given range in the list.
def binarySearch(alist,lower,higher):       #instead of having one variable after alist you need two   
    first=0                                 # assign the start and end of the search
    last=len(alist)-1                       #If my while loop returns found then the value is not in the parameters.
    found=False                     

    while first<=last and not found:        #If first is greater than last then there is no more integers to search.
        midpoint= (first+last)//2
        if alist[midpoint] <=higher and alist[midpoint]>= lower:     #checks if the midpoint is between my parameters
            found= True
        else:                                   #if the range is higher than the midpoint the search needs to move down to the left
            if alist[midpoint] >= higher:       #to the lower half else do the oposite.
                last = midpoint-1
            else:                       
                first =midpoint +1

    return found                                 

testlist = [0,1,2,8,13,17,19,32,42, ]
print(binarySearch(testlist, 7,10))
print(binarySearch(testlist, 14,117))
