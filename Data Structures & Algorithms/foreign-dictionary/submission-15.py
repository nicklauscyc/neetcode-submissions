class Solution:
    def findParent(self, node, parent, seen):
        if node in seen:
            return False
        seen.add(node)

        print("parent in findParent", parent)
        if not parent[node]:
            return node
        
        for p in parent[node]:
            return self.findParent(p, parent, seen)

    def postOrd(self, node, children, tree, seen, acc_seen):
        # Does a postOrd traversal on graph "children", returns
        # True and a tree of valid ordering in tree, False otherwise
        # 'seen' is to search for cycles on this traversal
     
        # cycle detection is inord
        print('postOrd', node, seen)
        if node in seen:
            # cycle
            print(node, "in seen")
            return False

        if node in acc_seen:
            print(node, "in acc_seen", acc_seen, "but seen", seen)
            return True

        acc_seen.add(node)
        if node not in children:
            print(node, "not in children!")
        if not children[node]:
            # base case
            print(node, "in base case")
            tree.append(node)
            return True
        
        seen.add(node)
        for child in children[node]:
            res = self.postOrd(child, children, tree, seen, acc_seen)
            if not res:
                return res
        tree.append(node)
        print(node, "tree", tree)
        seen.remove(node)
        return True
        
    def foreignDictionary(self, words: List[str]) -> str:
        # Generate graph
        children = {}
        parent = {}
        if len(words) == 1:
            return words[0]
        for i in range(len(words) - 1):
            j = i + 1
            lw = words[i]
            rw = words[j]
            k = 0
            has_diff = False
            while k < len(lw) and k < len(rw):
                l = lw[k]
                r = rw[k]

                if l not in children:
                    children[l] = set()
                if r not in children:
                    children[r] = set()
                
                if l not in parent:
                    parent[l] = set()
                if r not in parent:
                    parent[r] = set()

                if l == r:
                    k += 1
                    continue
                has_diff = True
                children[l].add(r)
                parent[r].add(l)
                break
            longer = lw if len(lw) > len(rw) else rw
            while k < len(longer):
                l = longer[k]
                if l not in children:
                    children[l] = set()
                if l not in parent:
                    parent[l] = set()
                k += 1
            

            if not has_diff and len(lw) > len(rw): 
                return ""
        
        for p, c in children.items():
            print(p, "->", c)

        acc_seen = set()
        solns = []
        for p in children:
            if p in acc_seen:
               continue
            # find the parent first
            par = self.findParent(p, parent, set())
            print(p, "has parent", par)
            if not par:
                return ""
            p = par
            tree = []

            res = self.postOrd(p, children, tree, set(), acc_seen)
            print("discover", p, tree, "res", res)
            if not res:
                return ""
            tree.reverse()
            solns.append("".join(tree))
        

        return "".join(solns)


        