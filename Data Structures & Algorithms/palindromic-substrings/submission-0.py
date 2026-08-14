class Solution:
    def isPal(self, s, l, r):
        if (l, r) in self.memo:
            return self.memo[(l,r)]
            
        if l == r:
            self.memo[(l,r)] = True
            return True
        if l == r - 1:
            self.memo[(l,r)] = s[l] == s[r]
            return s[l] == s[r]
        if s[l] != s[r]:
            self.memo[(l,r)] = False
            return False
        res = self.isPal(s, l+1, r-1)
        self.memo[(l,r)] = res
        return res

    def countSubstrings(self, s: str) -> int:
        self.memo = {}
        c = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    c += 1
        return c



        