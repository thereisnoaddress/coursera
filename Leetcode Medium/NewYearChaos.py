"""
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.
Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if  and  bribes , the queue will look like this: .
Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!
Function Description
Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
minimumBribes has the following parameter(s):
q: an array of integers
Input Format
The first line contains an integer , the number of test cases.
Each of the next  pairs of lines are as follows: 
- The first line contains an integer , the number of people in the queue 
- The second line has  space-separated integers describing the final state of the queue.
Constraints


Output Format
Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.
Sample Input
2
5
2 1 5 3 4
5
2 5 1 3 4
Sample Output
3
Too chaotic
"""

# Complete the minimumBribes function below.
def minimumBribes(q):
    totalBribes = 0

    # check which positions have been bribed
    for i in range(len(q)): 
        # if bribed more than 2 times 
        if q[i] > i + 3: 
            # illegal bribe
            print("Too chaotic", q[i], i)
            return False
        # else: 
        #     # legal bribe
        #     numBribes = q[i] - i - 1
        #     totalBribes += numBribes
        #     print("normal", q[i], i, numBribes)

        # check if the one number before q[i] are greater
        # this is because if q wants to bribe p in [o p q], the farthest q can get is 0
        # since q can only bribe twice
        # thus [o q p] -> [q o p]
        #
        # for every number that's between the range of (j - 1, i - 1), we check if it's larger than q[i]

        for j in range(max(0, q[i] - 2), i): 
            if q[j] > q[i]: 
                totalBribes += 1
    
    print(totalBribes)


            

if __name__ == "__main__":
    # minimumBribes([2,1,5,3,4])
    minimumBribes([1,2,5,3,7,8,6,4])
    # 1 2 3 4 5 6 7 8
    # 1 2 3 5 4 6 7 8   5 += 1
    # 1 2 5 3 4 6 7 8   5 += 1
    # 1 2 5 3 6 4 7 8   6 += 1
    # 1 2 5 3 6 7 4 8   7 += 1
    # 1 2 5 3 6 7 8 4   8 += 1
    # 1 2 5 3 7 6 8 4   7 += 1
    # 1 2 5 3 7 8 6 4   8 += 1
    # 5 -> 2, 6 -> 1, 7 -> 2, 8 -> 2