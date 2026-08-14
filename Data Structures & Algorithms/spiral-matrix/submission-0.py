class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        s = [] 
        R = len(matrix)
        C = len(matrix[0])
        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)
        order = [right, down, left, up] 
        minR = 0 
        maxR = R
        minC = 0 
        maxC = C 
        move = 0
        r = 0 
        c = 0
        while len(s) < R * C:  
            #print(r, c)
            s.append(matrix[r][c])
            dr, dc = order[move]
            if not (minR <= r + dr and r + dr < maxR):
                # hit bottom or top bounding box
                if move == 1:
                    # was moving down
                    maxC -= 1
                if move == 3:
                    # was moving up
                    minC += 1
                move = (move + 1) % len(order)
            elif not (minC <= c + dc and c + dc < maxC): 
                # hit left or right bouding box
                if move == 0: 
                    # was moving right 
                    minR += 1
                if move == 2: 
                    # was moving left
                    maxR -= 1
                move = (move + 1) % len(order) 
            dr, dc = order[move]
            r = r + dr
            c = c + dc
        return s
            
            

        