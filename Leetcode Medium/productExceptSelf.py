"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

def productExceptSelf(nums):
    # nums = [1,2,3,4]
    # arr = [1, 1, 2, 6]
    # rev = [24,12,8,6]
    # Output = [24,12,8,6]
    # idea: multiply by sum of previous sums, forward and backward
    arr = []
    forwardMultiplier = 1
    backwardMultiplier = 1

    for i in range(len(nums)):
        arr.append(forwardMultiplier)
        forwardMultiplier *= nums[i]
    
    for i in range(len(nums)-1, -1, -1): 
        arr[i] *= backwardMultiplier
        backwardMultiplier *= nums[i]

    return arr

        

if __name__ == "__main__":
    productExceptSelf([1,2,3,4])