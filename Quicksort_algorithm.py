def partition(numbers,i,k):

    
    l =0
    h = 0
    midpoint = 0
    pivot = 0
    temp = 0
    done= False
    

    midpoint= i + (k-i)//2
    pivot= numbers[midpoint]

    l = i
    h = k

    while not done:

        while numbers[l] < pivot:
            l += 1

        while pivot < numbers[h]:
            h -= 1

        if l >= h:
            done = True
        else:
            temp= numbers[l]
            numbers[l] = numbers[h]
            numbers[h] = temp

            l += 1
            h -= 1

    return h
        
def quicksort(numbers, i, k):
    j = 0
    

    if i >= k:
        return 

    else:
        j = partition(numbers,i,k)

        quicksort(numbers,i,j)
        quicksort(numbers, j + 1,k)

        

if __name__== "__main__":
    myList = [1002,5,15,84,97,84,5]


    quicksort(myList,0,len(myList)-1)
    print(myList)

    

        
