from collections import defaultdict, deque
from typing import Optional


class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None

class TreeNode:
    def __init__(self , val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        res = list()

        queue = deque([root])

        while queue:
            size = len(queue)
            arr = list()

            for i in range(size):
                curr =  queue.pop()
                arr.append(curr.val)

                if curr.left != None:
                    queue.append(curr.left)
                if curr.right != None:
                    queue.append(curr.right)

            res.append(arr)

        return res

    def oddList(self , head : Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even = head.next
        e_head = even


        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = e_head
        return head


    def hasCycle(self , head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def stack_operation(self):

        stack = []

        stack.append(2)
        stack.append(4)
        stack.append(5)


        stack.pop()

        stack.pop()

        print(len(stack))

    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }


        for c in s :
            if c in valid.values():
                stack.append(c)
            elif c in valid:
                if not stack or stack[-1] != valid[c]:
                    return False
                stack.pop()

        return True


    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        res = float('inf')
        ballon = set("ballon")

        for char in text:
            if char in ballon:
                counts[char]+=1


        for ch in ballon:
            if ch == 'l' or ch == 'o':
                res = min(res , counts[ch]//2)
            else:
                res = min(res , counts[ch])

        return res



    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 0
        right = max(piles)
        res = right

        while left <= right:
            hour = 0
            mid = (left+right)//2

            for p in piles:
                hour += (p+mid-1)//2

            if hour < h :
                res=mid
                right = mid -1
            else:
                left = mid + 1

        return res