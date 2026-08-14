class Solution:
    # 20 mi
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # flip along major diagonal
        for r in range(n):
            for c in range(r, n):
                if r == c:
                    continue
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # flip along the vertical axis
        for r in range(n):
            for c in range(n // 2):
                matrix[r][c], matrix[r][n-1-c]  = matrix[r][n-1-c], matrix[r][c]
  


 
        