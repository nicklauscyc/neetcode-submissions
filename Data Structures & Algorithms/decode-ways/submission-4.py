class Solution:
    # 12 mins
    def help(self, s, i):
        if i in self.dp:
            return self.dp[i]
        # Base cases
        # 0 digit left
        if i == len(s):
            self.dp[i] = 1
            return 1

        # 1 digit left
        if i == len(s) - 1:
            if s[i] == "0":
                self.dp[i] = 0
                return 0
            else: 
                self.dp[i] = 1
                return 1
        # 2 or more digits left is the recursive case
        use_1_letter = 0
        use_2_letter = 0
        if s[i] in self.encodings: 
            use_1_letter = 1 * self.help(s, i+1)
        if s[i:i+2] in self.encodings:
            use_2_letter = 1 * self.help(s, i+2)
        self.dp[i] = use_1_letter + use_2_letter
        return use_1_letter + use_2_letter
        
    def numDecodings(self, s: str) -> int: 
        self.encodings = set()
        self.dp = {}
        for i in range(1, 27):
            self.encodings.add(str(i)) 
        return self.help(s, 0)

        