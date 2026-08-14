class Solution:
    # 6 min no hint
    def isAnagram(self, s: str, t: str) -> bool:
        S = {}
        T = {}
        for a in s:
            S[a] = S.get(a, 0) + 1

        for a in t: 
            T[a] = T.get(a, 0) + 1
        
        print(S)
        print(T)
        for kS, vS in S.items():
            vT = T.get(kS, 0)
            if vT != vS: 
                return False
        if len(S) != len(T): 
            return False
        return True
        