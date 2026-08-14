class Solution:
    # Think about building up a string with brute force 
    # and then realize that there is a simpler way with 2 pointers
    # and then realize that we need some strong invariants to help 
    # us reason about the loops
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter2index = {}
        # Iterate over the string and keep track of the 
        # max length substring so far. 
        maxLength = 0
        left = 0
        # each substring will span index [left, right)
        for i in range(len(s)):
            letter = s[i]

            # invariant is that on this iteration, we want 
            # to keep this letter in our substring if possible.

            # invariant [left, right)
            right = i + 1
            if letter in letter2index and left <= letter2index[letter]: 
                # recompute left and right indices
                left = letter2index[letter] + 1

            print(letter, left, right)
            length = right - left
            if length > maxLength:
                maxLength = length
           
            # Update letter2index
            letter2index[letter] = i
        
        return maxLength

        