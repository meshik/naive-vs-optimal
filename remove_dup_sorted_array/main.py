def naïve_approach_v1(nums: list):
    # store unique elements
    unique_nums = []

    # iterate through the array
    for num in nums:
        if num not in unique_nums:
            # add 'num' to unique_nums
            unique_nums.append(num)

    # set nums to unique_nums
    nums = unique_nums
    # return number of unique elements
    return len(nums)
# time complexity: O(n^2) - loop + 'in' operator
# space complexity: O(n) -  unique_nums list


def naïve_approach_v2(nums: list):
    # initialize index
    index = 0
    
    # loop through the whole array
    while index < len(nums) - 1:
        
        if nums[index] == nums[index + 1]:
            # remove the duplicate
            nums.pop(index + 1)
        else:
            # keep advancing
            index += 1
            
    # return final length of 'nums'
    return len(nums)
# time complexity: O(n^2) - loop + 'pop' method
# space complexity: O(1) - perfect


def optïmal_solution(nums: list):
    # initialize 2 pointers:
    # track unique elements
    unique_p = 0
    # advance through the array
    advancing_p = 1

    # iterate through the array
    while advancing_p < len(nums):
        
        # check if pointed elements are the same
        if nums[unique_p] != nums[advancing_p]:
            # assign new element as the next unique
            unique_p += 1
            nums[unique_p] = nums[advancing_p]
            
        advancing_p += 1

    # +1 because of 0 indexing
    return unique_p + 1
# time complexity: O(n) - loop
# space complexity: O(1) - perfect
# life complexity: OH(YEA!)