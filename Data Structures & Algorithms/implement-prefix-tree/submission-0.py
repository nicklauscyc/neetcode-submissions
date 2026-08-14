class PrefixTree:
    # My prefix tree will have each node have a value that is exactly a character
    # The root will be an empty string just for generality
    class Node:
        def __init__(self):
            self.is_end = False
            self.children = {} # map of character to node
    def Print(self, node):
        for k in node.children:
            print(k)
            self.Print(node.children[k])
        
    def __init__(self):
        self.trie = self.Node()
        
    def insert(self, word: str) -> None:

        def dfs(node, word, i):
            if i == len(word):
                node.is_end = True
                return 
            if word[i] not in node.children: 
                node.children[word[i]] = self.Node()

            dfs(node.children[word[i]], word, i+1)

        dfs(self.trie, word, 0)  
        self.Print(self.trie)     

    def search(self, word: str) -> bool:
        def dfs(node, word, i):
            if i == len(word):
                return node.is_end
     
                

            #print("search", word[i], "in", [k for k in node.children])
            if word[i] in node.children: 
                return dfs(node.children[word[i]], word, i+1)
            #print("search return False")
            return False
        return dfs(self.trie, word, 0)

    def startsWith(self, prefix: str) -> bool:
        word = prefix
        def dfs(node, word, i):
            if i == len(word):
                return True # Found!
            #print("search", word[i], "in", [k for k in node.children])
            if word[i] in node.children: 
                return dfs(node.children[word[i]], word, i+1)
            return False
        return dfs(self.trie, word, 0)

        
        