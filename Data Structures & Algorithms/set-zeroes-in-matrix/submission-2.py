class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])

        # s is the tombstone, a unique fingerpint to mark zeros
        s = 0
        for r in range(R):
            for c in range(C):
                    s += matrix[r][c]
       
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    for row in range(R):
                        if matrix[row][c]:
                            matrix[row][c] = s
                    for col in range(C):
                        if matrix[r][col]:
                            matrix[r][col] = s
           
        #for r in range(R):
        #    print(matrix[r])


        for r in range(R):
            for c in range(C):  
                if matrix[r][c] == s:
                    matrix[r][c] = 0     

        
        
        