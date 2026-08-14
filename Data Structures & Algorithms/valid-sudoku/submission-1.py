class Solution:

    # Checks a row of numbers
    def checkRow(self, n, board, startRow):
        seen = set()
        allowed = set(map(str, [1,2,3,4,5,6,7,8,9]))
        for col in range(n): 
            elem = board[startRow][col]
            if elem == ".":
                continue

            if elem not in allowed:
                print(elem, "not in allowed")
                return False
            
            if elem in seen:
                print(elem, "in seen")
                return False
            seen.add(board[startRow][col])
        return True

    # Checks a column of numbers
    def checkCol(self, n, board, startCol):
        seen = set()
        allowed = set(map(str, [1,2,3,4,5,6,7,8,9]))
        for row in range(n): 
            elem = board[row][startCol] 
            if elem == ".":
                continue
            if elem not in allowed:
                return False
            
            if elem in seen:
                return False
            seen.add(elem)
        return True

    # Checks a 3x3 square 
    def checkSquare(self, board, startRow, startCol):
        print("checkSquareCalled", startRow, startCol)
        seen = set()
        allowed = set(map(str, [1,2,3,4,5,6,7,8,9]))
        for row in range(startRow, startRow+3):
            for col in range(startCol, startCol+3):
                elem = board[row][col]

                if elem == ".":
                    continue
                print(elem)
                if elem not in allowed:
                    return False
                if elem in seen: 
                    return False
                seen.add(elem)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for r in range(n):
            for c in range(n):
                print(board[r][c], end=" ")
            print()
        
        for i in range(n):
            if not self.checkRow(n, board, i):
                print("row", i , "false")
                return False
            if not self.checkCol(n, board, i):
                print("col", i, "false")
                return False
            
            if i % 3 == 0:
                for c in range(3):
                    if not self.checkSquare(board, i, c*3):
                        print("square", i, "false")
                        return False
        return True


     
        