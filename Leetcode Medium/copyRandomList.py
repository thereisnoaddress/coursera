"""
Amazon SWE onsite 

https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # running time O(n^2), definitely not the best 
        # space O(n)
        
        dic = {}
        pointer = head

        # make a deep copy of all the nodes
        while pointer: 

            dic[pointer] = Node(pointer.val, None, None)

            pointer = pointer.next

        pointer = head

        # go through all the nodes and append next / random pointers, if they exist
        while pointer: 
            dic[pointer].next = dic[pointer.next] if pointer.next else None

            dic[pointer].random = dic[pointer.random] if pointer.random else None

            pointer = pointer.next

        return dic[head]
        

