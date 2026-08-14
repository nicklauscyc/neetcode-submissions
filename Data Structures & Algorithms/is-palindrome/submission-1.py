class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1 - l
        count = n
        while l < r:
            #print(l,r)
            if not re.match('[a-zA-Z0-9]', s[l].lower()):
                l += 1
                continue
            if not re.match('[a-zA-Z0-9]', s[r].lower()):
                r -= 1
                continue
     
            #print(s[l].lower(), s[r].lower())
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        