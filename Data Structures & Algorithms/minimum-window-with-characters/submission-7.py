class Solution:
    def satisfy(self, l, r):
        # checks self.s[l,r) if it satisfies characters in t
        schar2count = {}
        for schar in self.s[l:r]:
            schar2count[schar] = schar2count.get(schar, 0) + 1

        # set containment logic to compare frequencies
        for tchar, count in self.tchar2count.items():
            if count > schar2count.get(tchar, 0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        self.s = s
        self.tchar2count = {}
        for tchar in t:
            self.tchar2count[tchar] = self.tchar2count.get(tchar, 0) + 1


        l = 0
        r = 1

        minR = len(s) + 1
        minL = 0

       

        while r <= len(s):
            # Expanding step
            while not self.satisfy(l, r) and r <= len(s):
                r += 1
            
            # Trimming step
            while self.satisfy(l, r):
                l += 1
            l -= 1

           

            # Update min window
            if r - l < minR - minL:
                minR = r
                minL = l
  

            l += 1 # Trigger the next iteration R to advance

        if minR - minL > len(s):
            return ""
        return s[minL:minR]

        