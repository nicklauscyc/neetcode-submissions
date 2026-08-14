class Node: 
    def __init__(self, val=""):
        self.val = val
        self.children = {} # letter to nodes of those letters

class WordDictionary:

    def __init__(self):
        # The root will represent an empty character
        self.root = Node()
    
    def _addWord(self, word, prevNode, i):
        if i < 0 or i >= len(word): 
            # End character
            prevNode.children[""] = None
            return
        letter = word[i]

        # Recursive case
        currNode = None

        # add 
        if letter not in prevNode.children:  
            currNode = Node(val=letter)
            prevNode.children[letter] = currNode
        else:
            currNode = prevNode.children[letter]
        
        self._addWord(word, currNode, i+1)

    def addWord(self, word: str) -> None:
        self._addWord(word, self.root, 0)

    def _search(self, word: str, prevNode: Node, i: int):
        if i < 0 or i >= len(word):
            return "" in prevNode.children
        
        # Dont think about the . first 
        letter = word[i]
        if letter != ".":
            currNode = prevNode.children.get(letter, None)
            if not currNode:
                return False
            return self._search(word, currNode, i+1)
        else: 
            for _, child in prevNode.children.items(): 
                if not child: 
                    continue # Don't recurse on string end markers
                if self._search(word, child, i+1): 
                    return True
            return False

    def search(self, word: str) -> bool:
        return self._search(word, self.root, 0)
        
