 
"""
  https://leetcode.com/problems/prison-cells-after-n-days/

    intuition / brute force

        prevPrison = cells
        curPrison = []
        
        for j in range(N): 
            prevPrison = curPrison if len(curPrison) > 0 else cells
            curPrison = []
            for i in range(8): 
                if i != 0 and i != 7 and prevPrison[i - 1] == prevPrison[i + 1]: 
                    print("i come here ", i, prevPrison[i-1], prevPrison[i], prevPrison[i+1])
                    curPrison.append(1)
                else: 
                    curPrison.append(0)
            
        
        return curPrison

        Running time: O(N), not ideal if N is big (which it seems like it could be)
        
        Key idea: (thanks https://www.youtube.com/watch?v=QmKUzTM92TA)
            Since we are only changing the values fo 6 cells between 0 and 1, we have 2^6 = 64 different total states; 
            after the 64 states, it will definitely repeat. So if N > 64, we don't need to re-generate some of the states again
            Thus, we can use a hashmap {key = cur state : value = next state} to optimize states
"""
 
def prisonAfterNDays(cells, N):    
    # helper function 
    def getNextDay(cells): 
        nextDayCells = [0] * len(cells)
        for i in range(1, len(cells) - 1): 
            nextDayCells[i] = 1 if cells[i-1] == cells[i+1] else 0
        
        return nextDayCells

    seenPrisons = {}

    while N > 0: 
        c = tuple(cells)
        if c in seenPrisons: 
            N %= seenPrisons[c] - N
        seenPrisons[c] = N

        if N >= 1: 
            N -= 1
            cells = getNextDay(cells)
        return cells
    

    

   

if __name__ == "__main__":
    res = prisonAfterNDays([1,0,0,1,0,0,1,0], 10000)
    print(res)