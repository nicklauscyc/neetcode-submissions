class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            s[nums[i]] = s.get(nums[i], []) + [i]

        print(s)
        for i in range(len(nums)): 
            fill = target - nums[i]
            if fill == nums[i] and len(s[fill]) == 1:
                continue
            print(nums[i], fill)
            if fill in s: 
                print("fill in s")
                if i < s[fill][-1]:
                    return [i,s[fill][-1] ]
                else: 
                    return [s[fill][-1], i]
        