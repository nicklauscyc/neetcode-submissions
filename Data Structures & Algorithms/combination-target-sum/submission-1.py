import copy
class Solution:
    # Since you are recursively backtracking, you want to partition the lower calls such that 
    # all combinations are covered.
    # use a lower recursion call as a loop
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        all = []
        def dfs(nums, i, target, l):
            if target == 0: 
                all.append(copy.deepcopy(l))
                return 
            if i >= len(nums) or target < 0: 
                return 
            
            l.append(nums[i])
            dfs(nums, i, target - nums[i], l)
            l.pop()
            dfs(nums, i+1, target, l)
        dfs(nums, 0, target, [])
        return all
