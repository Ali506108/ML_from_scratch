from collections import defaultdict, deque
from typing import Optional, List
from abc import ABC , abstractclassmethod

import numpy as np
from mpmath.functions.signals import sigmoid


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

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """

        :param nums: [1,1,2,1,1]
        :param k: 3
        :return: 2

        why is the solution is 2 ? because only 2 sub-arrays is -> [1,1,2,1] and [1,2,1,1]

        1
        after 1 - 3 = -2

        """
        hmap = {0:1}
        c_num = 0
        res = 0

        for num in nums:
            c_num+=num%2

            if (c_num-k) in hmap:
                res += hmap.get(c_num-k)

            hmap[c_num] = hmap.get(c_num , 0 )+1

        return res

    def forward_prop(self):
        x = np.array([[200,17]])

        w1_1 = np.array([1,2])
        b1_1 = np.array([-1])

        z1_1 = np.dot(x,w1_1)+b1_1
        a1_1 = sigmoid(z1_1)

        w1_2 = np.array([-3,4])
        b1_2 = np.array([1])

        z1_2 = np.dot(w1_2 , x)+b1_2

        a1_2 = sigmoid(z1_2)

        w1_3 = np.array([5,-6])
        b1_3 = np.array([2])


        z1_3 = np.dot(w1_3 , x) + b1_3
        a1_3 = sigmoid(z1_3)


        a1 = np.array([a1_1,a1_2,a1_3])


        w2_1 = np.array([-7,8,9])
        b2_1 = np.array([3])

        z2_1 = np.dot(w2_1 , a1)+b2_1

        a2_1 = sigmoid(z2_1)

        return a2_1




    def dailyTemperatures(self , temperatures : list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []

        for i , temp in enumerate(temperatures) :

            while stack and temperatures[stack[-1]]<temp:
                prev_ind = stack.pop()
                ans[prev_ind] = i - prev_ind
            stack.append(i)

        return ans

    def isValid(self , str) -> bool:
        stack = []
        hmap = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        for c in str:
            if c in hmap:
                t_e = stack.pop() if stack else '#'
                if hmap[c] != t_e:
                    return False
            else:
                stack.append(c)

        return not stack

    def simplifyPath(self, path: str) -> str:
        """

        :param path: /home/
        :return: /home
        """

        stack = []
        components = path.split('/')

        for c in components:
            if c == "" or c == ".":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
                else:
                    stack.append(c)


        return "/"+"/".join(stack)

    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()

        for n in nums:
            if n in hset:
                return True
            hset.add(n)

        return False


    def mat_multiple(self):
        A = np.array([[1,-1,0.1] ,
                      [2,-2,0.2]
                      ])

        AT = np.array([[1,2],
                       [-1,-2],
                       [0.1,0.2]])

        AT = A.T

        W = np.array([[3,5,7,9],
                      [4,6,8,0]
                      ])

        Z = np.matmul(AT,W)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted(s)

        sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True



    def dense(self , a_in , w,b):
        units = w.shape
        a_out = np.zeros(units)

        for j in range(units):
            w = w[:,j]
            z = np.dot(w,a_in) + b[j]
            a_out = g(z)

        return a_out

    def sequential(self , x):
        a1 = self.dense(x,w1,b1)
        a2 = self.dense(x,w3,b2)
        a3 = self.dense(x,w3,b3)

        return a3


    def vector(self):
        X = np.array[[200,17]]
        W = np.array([[1,-3,5],
                      [-2,4,-6],
                      [-1,1,2]])

        def dense(A_in,W,B):
            Z = np.matmul(A_in,W)+B
            A_out = g(Z)

            return A_out

    def classical_dense(self , a_in , w,b , g):
        units = w.shape
        a_out =  np.zeros(units)

        for j in range(units):
            w = w[:,j]
            z = np.dot(w,a_in) + b
            a_out[j] = g(z)

        return a_out

    def vector_dense(self ,a_in , w,b , g ):
        z = np.matmul(a_in , w)+b
        a_out = g(z)
        return a_out


class PreprocessingStrategy(ABC):
    @abstractclassmethod
    def transform(self , data: np.ndarray) -> np.ndarray:
        pass

class StandartScaler(PreprocessingStrategy):
    def transform(self , data: np.ndarray) -> np.ndarray:
        return (data - np.min(data , axis=0)) / (np.max(data,axis=0) - np.min(data,axis=0))

class FeaturePipeline:
    def __init__(self , strategy : PreprocessingStrategy):
        self.strategy = strategy

    def process(self , raw_data: np.ndarray) -> np.ndarray:
        return self.strategy.transform(raw_data)

