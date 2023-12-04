from typing import List

class Solution:
    # Define a method to group anagrams in a list of strings
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Define a dictionary that associates each lowercase letter with a prime number
        primes = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11,
                  'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
                  'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
                  'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
                  'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}

        # Initialize an empty dictionary to store the groups of anagrams
        ans = {}

        # Iterate through each string in the input list
        for s in strs:
            # Initialize a variable to store the product of prime factorization
            product = 1

            # Iterate through each character in the current string
            for char in s:
                # Multiply the product by the prime associated with the character
                product = product * primes[char]

            # Check if the product is already in the dictionary
            if product in ans:
                # If yes, append the string to the existing list
                ans[product].append(s)
            else:
                # If not, create a new list with the string
                ans[product] = [s]

        # Return the values (grouped anagrams) of the dictionary
        return ans.values()
