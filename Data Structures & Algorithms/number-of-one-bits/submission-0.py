class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        l = n
        while l > 0:
            if l % 2 == 1:
                count += 1
            l >>= 1
        return count

        