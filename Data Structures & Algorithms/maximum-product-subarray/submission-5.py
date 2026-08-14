class Solution:
    def help(self, nums, memo, i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == j:
            return nums[i]
        
        left = self.help(nums, i+1, j)
        right = self.help(nums, i, j-1)

        if left > right:
            memo[(i, j)] = left
            return left
        else:
            memo[(i, j)] = right
            return right
            


    def maxProduct(self, nums: List[int]) -> int:

        # Find all zeros and split on zeros
        sub = []
        start = 0
        end = len(nums)
        for i in range(len(nums)):
            end = i
            if nums[i] == 0:
                if start < len(nums) and start < end:
                    sub.append(nums[start:end])
                start = end+1
        if start < len(nums):
            sub.append(nums[start:])
        print("sub", sub)    

        # For each subarray, find all negatives
        max_prod = 0 if len(sub) > 1 or (len(sub) == 1 and len(sub[0]) < len(nums)) else nums[0]
        for s in sub: 
            print("max_prod", max_prod)
            
            # Find all negative indices
            negs = []
            for i in range(len(s)):
                if s[i] < 0:
                    negs.append(i)
            print("compute subarray", s, "negs", negs)
            
            prod = 1
            if len(negs) % 2 == 0:
                for x in s:
                    prod *= x
                print("prod", prod)
            else:
                # We have the invariant that the greatest product will 
                # need to be contiguous prefix or suffix
                suf_start = negs[0] + 1
                suf_end = len(s)


                suf_prod = 1
                valid_range = False
                for i in range(suf_start, suf_end):
                    valid_range = True
                    suf_prod *= s[i]
                if not valid_range:
                    suf_prod = s[0]

                pre_start = 0
                pre_end = negs[-1]
                pre_prod = 1
                valid_range = False
                for i in range(pre_start, pre_end):
                    valid_range = True
                    pre_prod *= s[i]
                if not valid_range:
                    pre_prod = s[0]
                
                print("suf_prod", suf_prod, "pre_prod", pre_prod)
                prod = pre_prod if pre_prod > suf_prod else suf_prod

            if prod > max_prod:
                max_prod = prod
        return max_prod

                

        