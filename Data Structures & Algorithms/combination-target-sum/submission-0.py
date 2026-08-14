import copy
class Solution:
    def com(self, i, target, chosen):
        if target <= 0:
            return
        if i >= len(self.nums):
            return
        num = self.nums[i]
        mult = 0
        while target > 0:
            if mult > 0:
                if num <= target:
                    chosen.append(num) 
                    #print(i, target, "insert", num, chosen)
                target -= num
            self.com(i+1, target, chosen)
            mult += 1
        if target == 0:
            #print("result", i, target, chosen)
            self.all.append(copy.deepcopy(chosen))
        # clean up chosen:
        while chosen and chosen[-1] == num:
            chosen.pop()
            

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # How do I completely cover all combinations?
        # from k = 1 to target // k:
        # add k and recurse
        self.nums = nums
        self.all = []
        self.com(0, target, [])
        #print(self.all)
        return self.all

        