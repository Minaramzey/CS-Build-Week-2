#https://leetcode.com/problems/contains-duplicate/
# https://leetcode.com/submissions/detail/385865181/ !SUBMISSION!
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

# https://leetcode.com/problems/add-two-numbers/
# https://leetcode.com/submissions/detail/385820939/ !SUBMISSION!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def getNum(ll):
            temp = []
            node = ll 
            while node is not None:
                temp.append(str(node.val))
                node = node.next
            return int("".join(temp))
        
        num = str(getNum(l1) + getNum(l2))
        new_num = list(num)
        
        new_ll = ListNode(new_num[-1])
        temp = new_ll
        for num in new_num[1::-1]:
            temp.next = ListNode(int(num))
            temp = temp.next
            
        return new_ll
