class Solution:
    def findLCS(self, s1, s2, i, j):
        if (i, j) in self.dp:
            return self.dp[(i, j)]

        if i >= len(s1) or j >= len(s2): 
            return 0
        
        # Recursive case
        match = 0
        if s1[i] == s2[j]:
            match = 1 + self.findLCS(s1, s2, i+1, j+1)
        defer_i = self.findLCS(s1, s2, i+1, j)
        defer_j = self.findLCS(s1, s2, i, j+1)

        res = max(match, defer_i, defer_j)
        if res == match: 
            print("match", i, j, s1[i], s2[j])
        self.dp[(i,j)] = res
        return res

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = {}
        return self.findLCS(text1, text2, 0, 0)
  

        