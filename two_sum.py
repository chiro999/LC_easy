def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    
    Approach: Use a dictionary to store numbers and their indices.
    Iterate through the list, calculate the complement, 
    and check if the complement exists in the dictionary.
    
    Args:
    nums (List[int]): Input list of integers
    target (int): Target sum
    
    Returns:
    List[int]: Indices of the two numbers that add up to target
    """
    num_dict = {}  # Dictionary to store numbers and their indices
    
    for index, num in enumerate(nums):
        complement = target - num  # Calculate the complement required to reach the target
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], index]  # Return indices of the two numbers
        
        num_dict[num] = index  # Add the number and its index to the dictionary
    
    return None  # If no solution is found

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
