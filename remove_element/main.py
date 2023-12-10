def naïve_approach(nums, val):
    # Loop through each element in nums
    for num in nums.copy():
        # If element is val
        if num == val:
            # Remove it
            nums.remove(num)
    return len(nums)
# O(n^2) time and O(n) space


def naïve_approach_v2(nums, val):
    # Repeat until no more val found
    while val in nums:
        # Remove first occurrence of val
        nums.remove(val)
    # Return length of modified list
    return len(nums)
# O(n^2) time and O(1) space


def naïve_approach_v3(nums, val):
    # recreate nums with only non-val elements
    nums[:] = [num for num in nums if num != val]
    return len(nums)
# O(n) time and O(n) space

    
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
    
    return pointer
# O(n) time and O(1) space = $$GET RICH$$
    

