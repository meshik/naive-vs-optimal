def naïve_approach(nums, val):
    
    # Initialize an empty list for non-val elements
    non_val_elements = []
    
    # Loop through each element in nums
    for num in nums:
        # If element is not val, add it to non_val_elements
        if num != val:
            non_val_elements.append(num)
    
    # Copy non-val elements back to nums
    nums[:len(non_val_elements)] = non_val_elements
    
    # Return the count of non-val elements
    # return len(non_val_elements)
    
    

    ########################################
    for num in nums:
        if num == val:
            nums.remove(num)
    
    ########################################
    for num in nums.copy():
        if num == val:
            nums.remove(num)
    
    ########################################
    nums[:] = [num for num in nums if num != val]
    
    return len(nums)

    
def optimal_approach(nums, val):
    # Initialize start index for the modified array
    pointer = 0
    
    # Loop through each element in nums
    for num in nums:
        # If element is not val
        if num != val:
            # Place it at the pointer index
            nums[pointer] = num
            # Increment pointer index
            pointer += 1
    
    # Return the count of elements not equal to val
    return pointer

    

