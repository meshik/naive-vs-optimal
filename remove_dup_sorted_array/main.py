def naive_approach_v1(nums: list):
    # store unique elements
    unique_nums = []

    # iterate through the array
    for num in nums:
        # check if the element is not in unique_nums
        if num not in unique_nums:
            # add the element to unique_nums
            unique_nums.append(num)

    # set nums to unique_nums
    nums = unique_nums
    # return number of unique elements
    return len(unique_nums)
# time complexity: O(n^2) because of the 'in' operator
# space complexity: O(n) because of the unique_nums list


def naive_approach_v2(nums: list):
    # initialize index
    index = 0
    # loop through the whole array
    while index < len(nums) - 1:
        # Check if current and next elements are the same
        if nums[index] == nums[index + 1]:
            # remove the next element
            nums.pop(index + 1)
        else:
            # Move to the next element
            index += 1
    # Return the new length of nums
    return len(nums)
# time complexity: O(n^2) because of the pop method
# space complexity: O(1)


def optimal_solution(nums: list):
    # initialize 2 pointers:
    # track unique elements
    unique_pointer = 0
    # advance through the array
    advancing_pointer = 1

    # iterate through the array
    while advancing_pointer < len(nums):
        if nums[unique_pointer] != nums[advancing_pointer]:
            nums[unique_pointer + 1] = nums[advancing_pointer]
            unique_pointer += 1
        advancing_pointer += 1

    # +1 because of 0 indexing
    return unique_pointer + 1

# time complexity: O(n)
# space complexity: O(1)