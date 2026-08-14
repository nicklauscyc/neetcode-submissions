class Solution:


    def encode(self, strs: List[str]) -> str:
        ''' use 3 digits to determine the length of the string'''
        res = []
        for s in strs: 
            n = len(s)
            res.append(f"{n:03}")
            res.append(s)
        print(res)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0
     
        while i < n:  
            l = s[i:i+3]
            length = int(l)
            si = ""
            i = i+3
            if length: 
                si = s[i:i+length]
                i = i + length
            res.append(si)
            print(l, si)

        return res
        
