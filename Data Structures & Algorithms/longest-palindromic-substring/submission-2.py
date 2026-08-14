class Solution:
    # 15 min
    def isPal(self, s, l, r):
        if (l, r) in self.dp:
            return self.dp[(l,r)]

        # Out of bounds check
        if not (0 <= l and l <= r and r < len(s)):
            self.dp[(l,r)] = False
            return False
        # Base case
        if l == r:
            self.dp[(l,r)] = True
            return True
        if l == r - 1:
            self.dp[(l,r)] = s[l] == s[r]
            return s[l] == s[r]
        
        # Recursive case
        if s[l] != s[r]:
            self.dp[(l,r)] = False
            return False
        self.dp[(l,r)] = self.isPal(s, l + 1, r - 1)
        return self.dp[(l,r)]

    def longestPalindrome(self, s: str) -> str:
        
        maxL = 0
        maxR = 0
        self.dp = {}
        for l in range(len(s)):
            for r in range(l+1, len(s)):
                print(l, r)
                if self.isPal(s, l, r):
                    print("ispal")
                    if r - l > maxR - maxL:
                        maxL = l
                        maxR = r

        return s[maxL:maxR+1]

