class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        swap = 0
        n = len(matrix)
        # flip along major diagonal
        for r in range(n):
            for c in range(r, n):
                if r == c:
                    continue
                swap = matrix[r][c] 
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = swap

        # flip along the vertical axis
        for r in range(n):
            for c in range(n // 2):
                swap = matrix[r][c]
                matrix[r][c] = matrix[r][n-1-c]
                matrix[r][n-1-c] = swap


 
        