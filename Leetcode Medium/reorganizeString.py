from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        idea: 
        - sort frequency using a hashmap 
        - add into maxheap
        - manipulate maxheap until it works
        """
        ansStr = ""
        
        freq = {}
        for char in S: 
            if char not in freq: 
                freq[char] = 1
            else: 
                freq[char] += 1
        
        h = []
        for key in freq: 
            heappush(h, (-freq[key], key))
        
        # while there are 2 or more characters
        while len(h) > 1: 
            f1, c1 = heappop(h)
            f2, c2 = heappop(h)
            
            ansStr += c1; ansStr += c2
            
            f1 += 1; f2 += 1
            if f1 < 0: 
                heappush(h, (f1, c1))
            if f2 < 0: 
                heappush(h, (f2, c2))
        
        if len(h) > 0: 
            finalFreq, finalChar = heappop(h)
            if -finalFreq > 1: 
                ansStr = ""
            else: 
                ansStr += finalChar
            
        return ansStr