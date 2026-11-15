class Trie:
    def __init__(self, val):
        self.val = val
        # Children of this Trie Node which is another Trie instance
        self.children = {} # letter to child Trie Node
        self.end = False

class Solution:

    def add_dfs(self, node, word, i):
        # Adds to the trie the terminate character.
        if i >= len(word):
            node.children[''] = Trie('')
            node.end = True
            return 
        
        # Find which of the children match the letter
        letter = word[i]
        if letter in node.children:
            self.add_dfs(node.children[letter], word, i+1)
            return 
        
        # Else no children match, add a new child
        new_child = Trie(letter)
        node.children[letter] = new_child
        #print("added", letter, "for", word)
        self.add_dfs(new_child, word, i+1)

    
    def print_dfs(self, node, word, arr):
        if not node.children:
            word.append(node.val)
            res = ''.join(word)
            arr.append(res)
            word.pop()
            return 
        
        word.append(node.val)
        for child in node.children:
            self.print_dfs(child, word, arr)
        
        word.pop()

    def getNeighbors(self, board, r, c):
        ROW = len(board)
        COL = len(board[0])
        N = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        res = set()
        for n in N:
            if 0 <= n[0] and n[0] < ROW and 0 <= n[1] and n[1] < COL:
                res.add(n)
        return res
        
    def dfs(self, board, r, c, node, arr, visited, stack):
        # board: the array of letters to find our words in
        # r: row in board
        # c: col in board
        # node: current pointer to a node in our trie
        # arr: set of words we've found so far
        # visited: set of (r, c) we've visited before
        # stack: stack of letters of our current word that we have so far
        if (r, c) in visited:
            return 
        # Base case is when we are at a letter that is an end in the node
        board_elem = board[r][c]
        visited.add((r,c))

        if board_elem == node.val:
            stack.append(board_elem)
            if node.end:
                arr.add(''.join(stack))
            
            N = self.getNeighbors(board, r, c)
            for n in N:
                nr, nc = n
                letter = board[nr][nc]
                if letter in node.children:
                    child = node.children[letter]
                    self.dfs(board, nr, nc, child, arr, visited, stack)
            stack.pop()
        visited.remove((r,c))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Construct the Trie of words
        root = Trie('')
        for word in words:
            self.add_dfs(root, word, 0)

        #debug_arr = []
        #self.print_dfs(root, [], debug_arr)
        #print(arr)

        if len(board) == 0:
            return []

        arr = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                letter = board[r][c]
                if letter in root.children:
                    child = root.children[letter]
                    self.dfs(board, r, c, child, arr, set(), [])

        return list(arr)



        