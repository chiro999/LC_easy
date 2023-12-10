from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Define a recursive function with memoization using lru_cache
        @lru_cache(maxsize=None)
        def dp(i, j):
            # Base case: If either string is fully processed, return 0
            if i >= len(text1) or j >= len(text2):
                return 0
            
            # If characters at the current indices match
            if text1[i] == text2[j]:
                i += 1
                j += 1
                # Increment both indices and add 1 to the result
                return 1 + dp(i, j)
            else:
                # If characters don't match, consider two cases:
                # 1. Skip one character in text1 and recur
                # 2. Skip one character in text2 and recur
                return max(dp(i + 1, j), dp(i, j + 1))

        # Start the recursion with initial indices (0, 0)
        return dp(0, 0)
