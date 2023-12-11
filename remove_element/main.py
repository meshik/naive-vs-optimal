def naïve_approach(nums, val):
    # loop through each element in nums
    for num in nums.copy():
        # if element is val
        if num == val:
            # remove it
            nums.remove(num)  # O(n) runtime
    return len(nums)
# O(n) space
# O(n^2) time

def naïve_approach_v2(nums, val):
    # repeat until no more val found
    while val in nums:
        # remove an occurrence of val
        nums.remove(val)  # O(n) runtime
    # return length of modified list
    return len(nums)
# O(1) space
# O(n^2) time

def naïve_approach_v3(nums, val):
    # recreate nums with only non-val elements
    nums[:] = [num for num in nums if num != val]
    return len(nums)
# O(n) time :D
# O(n) space :'(
    
def optimal_approach(nums, val):
    # initialize pointer for nums
    pointer = 0
    
    # loop through each element in nums
    for num in nums:
        # if element is not val
        if num != val:
            # place it at the pointer
            nums[pointer] = num
            # increment pointer
            pointer += 1
    
    return pointer
# O(n) time and O(1) space = $$GET RICH$$
    

