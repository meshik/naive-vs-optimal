
def naive_approach_v1(nums):
    # store unique elements
    unique_nums = []

    for num in nums:
        # check if the element is not in unique_nums
        if num not in unique_nums:
            # add the element to unique_nums
            unique_nums.append(num)
            
    # Replace initial elements of nums with unique elements
    nums[:len(unique_nums)] = unique_nums
    # Return the number of unique elements
    return len(unique_nums)


def optimal_solution(nums: list):
    unique_pointer = 0
    advancing_pointer = 1

    while advancing_pointer < len(nums):
        if nums[unique_pointer] != nums[advancing_pointer]:
            nums[unique_pointer + 1] = nums[advancing_pointer]
            unique_pointer += 1
        advancing_pointer += 1

    return unique_pointer + 1