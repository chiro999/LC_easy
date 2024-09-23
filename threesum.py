from typing import List

class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array
        ans = []
        for i, num in enumerate(nums):
            if i >= 1 and nums[i-1] == nums[i]:  # Skip duplicates
                continue
            l, r = i + 1, len(nums) - 1  # Two pointers: left and right
            while l < r:
                total = num + nums[l] + nums[r]
                if total > target:
                    r -= 1  # Move the right pointer left to reduce total
                elif total < target:
                    l += 1  # Move the left pointer right to increase total
                else:
                    ans.append([num, nums[l], nums[r]])  # Found a triplet
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:  # Avoid duplicates
                        l += 1
        return ans
