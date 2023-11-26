# merge & sort the arrays into arr1

def naive_approach(arr1, arr2):
    # get the none-zero elements in arr1
    m = len(arr1) - len(arr2)
    # copy arr2 to the end of arr1
    arr1[m:] = arr2
    # sort everything
    arr1.sort()

def optimal_approach(arr1, arr2):
    # get the length of integers
    m = len(arr1) - len(arr2) 
    n = len(arr2)
    
    # start from the end of each array
    while m > 0 and n > 0:
        if arr1[m-1] > arr2[n-1]:
            arr1[m+n-1] = arr1[m-1]
            m -= 1
        else:
            arr1[m+n-1] = arr2[n-1]
            n -= 1
            
    # copy remaining elements, if any
    arr1[:n] = arr2[:n]