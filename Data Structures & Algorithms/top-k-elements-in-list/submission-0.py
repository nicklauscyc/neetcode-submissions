class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        

        l = sorted(freq.items(), key=lambda x : x[1], reverse=True)
        
        #print(l)
        r = []
        i = 0
        while i < k:
            r.append(l[i][0])
            i += 1
        return r


        