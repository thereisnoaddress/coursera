class Solution:
    def findCircleNum(self, M):
        
       
        
        def find(x): 
            if circles[x] == x: 
                return circles[x]
            return find(circles[x])
        
        def union(a, b): 
            leaderA = find(a)
            leaderB = find(b)
            
            circles[leaderB] = leaderA
        
        circles = list(range(len(M)))
        for i in range(len(M)): 
            for j in range(i): 
                if M[i][j]: 
                    union(i, j)

        return len(set(find(i) for i in range(len(M))))
        
        