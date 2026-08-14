class Solution:
    def help(self, wSet, s, i) -> bool:
        if i in self.memo:
            return self.memo[i]
        if i == len(s):
            self.memo[i] = True
            return True
        for j in range(i+1, len(s)+1):
            #print(s[i:j], "in wSet", s[i:j] in wSet)
            if s[i:j] in wSet:
                res = self.help(wSet, s, j)
                if res:
                    self.memo[i] = True
                    return True
        self.memo[i] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memo table will be indices i in s, indicating if it's possible
        # to form the word s[i:] from words in wordDict
        wSet = set()
        self.memo = {}
        for w in wordDict:
            wSet.add(w)

        #print("wSet", wSet)
        return self.help(wSet, s, 0)