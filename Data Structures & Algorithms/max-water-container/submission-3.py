class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        maxWater = 0 
        turn = 0
        while l < r: 
            # only advance if greater
            #print(l , r, heights[l], heights[r])
            height = min(heights[l], heights[r])
            water = height * (r - l)
            if water > maxWater: 
                maxWater = water
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1

        return maxWater
        