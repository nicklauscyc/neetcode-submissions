class Solution:
    # 8 min
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # let n be length of nums 
        n = len(nums)
        # build a prefix product array where p[i] = product of a_0 * ... * a_(i-1)
        p = []
        cum = 1
        for i in range(n):
            if i > 0:
                cum *= nums[i-1]
            p.append(cum)
        #print(p)

        # build a suffix product array where s[i] = product of a_(i+1) * ... * a_(n-1)
        s = [0 for i in range(n)]
        cum = 1
        for j in range(n-1, -1, -1):
            if j < n-1:
                cum *= nums[j+1]
            s[j] = cum
        #print(s)

        res = []
        for i in range(n):
            res.append(p[i]*s[i])

        return res