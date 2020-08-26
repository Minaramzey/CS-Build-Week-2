# https://leetcode.com/problems/two-sum/
# https://leetcode.com/submissions/detail/382433283/ !SUBMISSION!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for i, j in enumerate(nums):
            if target - j in cache:
                return [cache[target - j], i]
            cache[j] = i

# https://leetcode.com/problems/implement-queue-using-stacks/
# https://leetcode.com/submissions/detail/386805915/ !SUBMISSION!

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        return self.queue.pop(0)


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.queue):
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()