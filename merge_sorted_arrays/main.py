# arr1/arr2 are sorted integer arrays
# arr1 has enough space appended to hold arr2
# merge the arrays into arr1 in sorted order

def naive_approach1(arr1, arr2):
    for i in range(len(arr2)):
        arr1.append(arr2[i])
    return sorted(arr1)

def naive_approach2(arr1, arr2):
    arr1.extend(arr2)
    return sorted(arr1)

def optimal_approach(arr1, arr2):
    # get the length of integers
    m = len(arr1) - len(arr2)  # m is the number of integers in arr1
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