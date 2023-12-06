def naïve_approach(nums, val):
    nums[:] = [num for num in nums if num != val]
    return len(nums)
    # time complexity: O(n) because we iterate through the list once
    
def optimal_approach(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums[i] = nums[-1]
            nums.pop()
        else:
            i += 1
    return len(nums)
    # time complexity: O(n) because we iterate through the list once
    

