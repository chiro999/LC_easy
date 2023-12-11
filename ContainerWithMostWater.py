from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Function to calculate the volume of water between two lines
        def amountWater(i, j):
            return min(height[i], height[j]) * (j - i)

        # Initialize the maximum water volume to 0
        maxWater = 0
        # Initialize two pointers, i at the beginning and j at the end
        i, j = 0, len(height) - 1

        # Continue the loop until the two pointers meet
        while i < j:
            # If the current water volume is greater than the maxWater, update maxWater
            if maxWater < amountWater(i, j):
                maxWater = amountWater(i, j)

            # Move the pointer with the smaller height towards the center
            # This is because moving the pointer with the larger height won't increase the volume
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        # Return the maximum water volume found
        return maxWater
