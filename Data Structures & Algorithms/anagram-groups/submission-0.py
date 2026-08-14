class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For each string, we sort the letters in lexicographic order
        # we maintain a dictionary of sorted letters (key) to all anagrams 
        # Finally, iterate over the dictionary to create the output 
        g = {}
        for s in strs: 
            k = ''.join(sorted(s))
            #print(k)
            if k in g: 
                g[k].append(s)
            else: 
                g[k] = [s]
        r = []
        for k, v in g.items():
            r.append(v)
        return r
