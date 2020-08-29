class Solution:
    def findRedundantConnection(self, edges):
        collection = [0] * len(edges)
        
        def find(edge): 
            if collection[edge] == 0: 
                return edge
            return find(collection[edge])
                
        def union(e1, e2): 
            e1Root = find(e1)
            e2Root = find(e2)
            if e1Root == e2Root: 
                return False
            collection[e1Root] = e2Root
            return True
        
        for e1, e2 in edges: 
            if not union(e1 - 1, e2 - 1): 
                return [e1, e2]