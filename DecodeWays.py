class Solution:
    def numDecodings(self, s: str) -> int:
        # Check if the first character is '0', indicating that the entire string cannot be decoded.
        if s[0] == '0':
            return 0

        # Initialize a dynamic programming array to store the number of ways to decode up to each index.
        dp = [0 for i in range(len(s) + 1)]
        
        # There is one way to decode an empty string.
        # There is also one way to decode a string of length 1 using a single-digit character.
        dp[0:2] = [1, 1]

        # Iterate through the string starting from the third character.
        for i in range(2, len(s) + 1):
            # If the current digit is between 1 and 9 (inclusive), add the ways to decode the previous string to the current index.
            if 0 < int(s[i - 1:i]) <= 9:
                dp[i] += dp[i - 1]

            # If the current and previous digits form a number between 10 and 26 (inclusive),
            # add the ways to decode the string two positions back to the current index.
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        # Return the last element of the dp array, which represents the total ways to decode the entire string.
        return dp[-1]
