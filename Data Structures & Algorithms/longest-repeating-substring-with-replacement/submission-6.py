class Solution:
    def isValidWindow(self, s, k, l, r): 
        # interval is [l, r)
        freq = {}
        for i in range(l, r):
            freq[s[i]] = freq.get(s[i], 0) + 1
        print(freq)
        maxF = 0
        for [letter, f] in freq.items():  
            if f > maxF:
                maxF = f
        print((r-l)- maxF, k)
        return (r - l) - maxF <= k

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 1
        maxWin = 0 
        count = 0
        while r <= len(s) and l < r:
            isValid = self.isValidWindow(s, k, l, r)
            if isValid:
                print("valid", s[l:r])
            else:
                print("not valid", s[l:r])

            if isValid:
                size = r - l
                if size > maxWin: 
                    maxWin = size
                r += 1
            else: 
                l += 1

        return maxWin
        