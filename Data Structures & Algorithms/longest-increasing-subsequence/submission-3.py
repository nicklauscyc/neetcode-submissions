class Solution:
    def help(self, nums, i, n, prev_max):
        if (prev_max, i) in self.memo:
            return self.memo[(prev_max, i)]
        if i == n-1:
            if prev_max < nums[i]:
                return 1
            return 0
        

        elem = nums[i]
        if prev_max < elem:
            # I can choose to include elem in my sequence or not
            include = 1 + self.help(nums, i+1, n, elem)
            not_include = self.help(nums, i+1, n, prev_max)

            # return the max
            greater = max(include, not_include)
            self.memo[(prev_max, i)] = greater
            return greater
        
        res = self.help(nums, i+1, n, prev_max)
        self.memo[(prev_max, i)] = res
        return res
        

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memo = {}
        return self.help(nums, 0, len(nums), -1001)
        