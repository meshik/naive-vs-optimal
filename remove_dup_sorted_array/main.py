def naïve_approach_v1(sins: list):
    # store unique elements
    unique_sins = []

    # iterate through the array
    for sin in sins:
        if sin not in unique_sins:
            # add 'sin' to unique_sins
            unique_sins.append(sin)

    # set sins to unique_sins
    sins = unique_sins
    # return number of unique elements
    return len(sins)
# time complexity: O(n^2) - loop + 'in' operator
# space complexity: O(n) -  unique_sins list


def naïve_approach_v2(sins: list):
    # initialize index
    index = 0
    
    # loop through the whole array
    while index < len(sins) - 1:
        
        if sins[index] == sins[index + 1]:
            # remove the duplicate
            sins.pop(index + 1)
        else:
            # keep advancing
            index += 1
            
    # return final length of 'sins'
    return len(sins)
# time complexity: O(n^2) - loop + 'pop' method
# space complexity: O(1) - perfect


def optïmal_solution(sins: list):
    # initialize 2 pointers:
    # track unique elements
    unique_p = 0
    # advance through the array
    advancing_p = 1

    # iterate through the array
    while advancing_p < len(sins):
        
        # check if pointed elements are the same
        if sins[unique_p] != sins[advancing_p]:
            # assign new element as the next unique
            unique_p += 1
            sins[unique_p] = sins[advancing_p]
            
        advancing_p += 1

    # +1 because of 0 indexing
    return unique_p + 1
# time complexity: O(n) - loop
# space complexity: O(1) - perfect
# life complexity: OH(YEA!)