"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

def permute(nums):
  # consider every integer as a node in a tree
  # do DFS
  # some sort of backtracking recursive algorithm
  cur = []
  rem = nums[:]
  allPerm = []
  permutation(cur, rem, allPerm)
  return allPerm
  

def permutation(cur, remaining, allPerm): 
  # cur = array of currently selected element
  if len(remaining) == 0: 
    allPerm.append(cur)
  else: 
    for item in remaining:   
      curCopy = cur[:]
      curCopy.append(item)
      remCopy = remaining[:]
      remCopy.remove(item)
      permutation(curCopy, remCopy, allPerm)
    


if __name__ == "__main__":
    allPermutations = permute([1,2,3,4])
    print(allPermutations)