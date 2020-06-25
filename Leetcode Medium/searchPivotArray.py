"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
from math import *

def search(nums, target): 
    # do binary search based on the pivot 
    mid = len(nums) // 2

    if (nums[mid] == target): 
        return mid
    
    # if this is a pivot...
    if len(nums) != 1 and nums[mid+1] < nums[mid]: 
        if target >= nums[mid]: 
            search(nums[mid+1:], target)
        else: 
            search(nums[0:mid], target)
    else: 
        if target >= nums[mid]: 
            search(nums[0:mid], target)
        else: 
            search(nums[mid+1:], target)
    
    return -1

if __name__ == "__main__":
    res = search([4,5,6,7,0,1,2], 0)
    # mid = 3, low = 0, high = 7
    # if nums[mid] > target: 
    print(res)